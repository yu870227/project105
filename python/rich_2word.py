import requests
import pymysql
import pdfplumber
import chardet
from bs4 import BeautifulSoup
import readablenogoogle

#db = pymysql.connect("203.64.84.94", "Fish", "851217", "project105")
#db = pymysql.connect("localhost", "root", "97462835", "project105")
#cur = db.cursor()
def getweb(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
    htmlpage = requests.get(url, headers=headers, verify=False,timeout=5)
    chardit = chardet.detect(htmlpage.content).get('encoding')
    if chardit == "Windows-1252":
        htmlpage.encoding = 'big5'
    if chardit == "Windows-1254":
        htmlpage.encoding = 'utf-8'
    if htmlpage.status_code != 200:
        print("invalid url", htmlpage.status_code)
        return None
    else:
        return htmlpage.text

def rich2word(index,text):
    db = pymysql.connect("203.64.84.94", "Fish", "851217", "project105")
    cur = db.cursor()
    count=0
    for vocid in range(41976):
        v=""
        sqlvoc="SELECT voc FROM vocabulary_2word WHERE id='%d'"%(vocid)
        try:
            cur.execute(sqlvoc)
            v = cur.fetchall()[0][0]
        except:
            db.rollback()
        if len(v)!=0:
            has=text.find(v)
            if has!=-1:
                #print(v)
                count=count+1
    print(index,count)
    return count

def rich_2word_calculation(articlelen,cou):
    x=(articlelen-100)/10000
    y=(cou-20)/440
    if x>1:
        x=1
    elif x<0:
        x=0
    
    if y>1:
        y=1
    elif y<0:
        y=0
    
    if x==0:
        x1=0
    else:
        x1=y/x

    print(cou,x,y,x1)
    return x1

def upsql(di,ri):
    db = pymysql.connect("203.64.84.94", "Fish", "851217", "project105")
    cur = db.cursor()
    num=None
    sql3="SELECT rich FROM disease_t WHERE id='%d'"%(di)
    try:
        cur.execute(sql3)
        num=cur.fetchall()[0][0]
    except:
        db.rollback()
    if num!=None:
        newrich=0.65*num+(0.35*ri)
        sql2="UPDATE disease_t SET rich2 = '%f' WHERE id = '%d'" % (newrich,di)
        try:
            cur.execute(sql2)
            db.commit()
        except:
            db.rollback()

def rich_voc(st,en):
    for i in range(st,en):
        db = pymysql.connect("203.64.84.94", "Fish", "851217", "project105")
        #db = pymysql.connect("localhost", "root", "97462835", "project105")
        cur = db.cursor()
        #avg=0
        keycou=0
        #print(i)
        u=None
        sq4 = "SELECT url FROM disease_t WHERE id='%d'" % (i)
        try:
            cur.execute(sq4)
            u = cur.fetchall()[0][0]
        except:
            db.rollback()
    
        if u!=None:
            #pp=u.find("pdf")
            if u.endswith(".pdf"):
                try:
                    r = requests.get(u)
                    pdf = r.content
                    with open("C:/105專題/105316126/a.pdf", "wb") as f:
                        f.write(pdf)
                    f.close()
                    a=""
                    with pdfplumber.open("C:/105專題/105316126/a.pdf",passeord='') as pdf:
                        #print(len(pdf.pages))
                        for ind in range(len(pdf.pages)):
                            page = pdf.pages[ind]
                            text = page.extract_text()
                            # print(text)
                            if isinstance(text,str):
                                a = a + text
                            for table in page.extract_tables():
                                for line in table:
                                    # print(line)
                                    if isinstance(line,list):
                                        for li in line:
                                            if isinstance(li,str):
                                                a=a+li
                                    else:
                                        a = a + line
                    pdf.close()
                    keycou=rich2word(i,a)
                    ri2=rich_2word_calculation(len(a),keycou)
                    upsql(i,ri2)
                except:
                    continue
            else:
                try:
                    html = getweb(u)
                    if html != None:
                        soup = BeautifulSoup(html, 'html.parser')
                        eve = u.find("everydayhealth")
                        mohw = u.find("mohw.gov")
                        if eve != -1 or mohw != -1:
                            h1 = soup.find("article")
                            if h1 != -1:
                                #c = 1
                                a = h1.text

                        else:
                            h1 = soup.find_all("p")
                            if h1 != -1:
                                #print("2")
                                #c = 2
                                a = ""
                                for h2 in h1:
                                    a = a + h2.text
                            else:
                                h1 = soup.find("article")
                                if h1 != -1:
                                    #print("1")
                                    a = h1.text
                        keycou=rich2word(i,a)
                        ri2=rich_2word_calculation(len(a),keycou)
                        upsql(i,ri2)
                except:
                    continue
    readablenogoogle.readable(st,en)
                