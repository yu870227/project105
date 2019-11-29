import pdfplumber
import requests
import pymysql
import rr
from bs4 import BeautifulSoup
import chardet

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'}
#headers = {'User-agent': 'your bot 0.1'}

def getweb(url):
    htmlpage = requests.get(url, headers=headers, verify=False,timeout=5)
    print(chardet.detect(htmlpage.content))
    a = chardet.detect(htmlpage.content).get('encoding')
    print(a)
    if a == "Windows-1254":
        htmlpage.encoding = "utf8"
    elif a == "Windows-1252":
        htmlpage.encoding = "big5"
    else:
        htmlpage.encoding = a

    if htmlpage.status_code != 200:
        print("error:", htmlpage.status_code)
        return None
    else:
        return htmlpage.text

def readable(a,b):

    for i in range(a, b):
        db = pymysql.connect("203.64.84.94", "Fish", "851217", "project105")
        #db = pymysql.connect("localhost", "root", "97462835", "project105")
        cur = db.cursor()
        f=open('C:/105專題/105316126/googlesearchid.txt','w')
        f.write(str(i))
        f.close()
        sql = " SELECT url FROM disease_t WHERE id='%d'" % (i)
        try:
            a = ""
            cur.execute(sql)
            res = cur.fetchall()
            u = res[0][0]
            if u.endswith(".pdf"):
                try:
                    print(i)
                    r = requests.get(u)
                    pdf = r.content
                    with open("C:/105專題/105316126/a.pdf", "wb") as f:
                    #with open("C:/Users/user/Desktop/105專題/pdf/a.pdf", "wb") as f:
                        f.write(pdf)
                    f.close()

                    with pdfplumber.open("C:/105專題/105316126/a.pdf") as pdf:
                    #with pdfplumber.open("C:/Users/user/Desktop/105專題/pdf/a.pdf") as pdf:
                        print(len(pdf.pages))
                        for ind in range(len(pdf.pages)):
                            page = pdf.pages[ind]
                            text = page.extract_text()
                            a = a + text
                            for table in page.extract_tables():
                                for line in table:
                                    a = a + line

                    rr.ree(a,i)
                    pdf.close()
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
                                a = h1.text

                        else:
                            h1 = soup.find_all("p")
                            if h1 != -1:
                                print("2")
                                a = ""
                                for h2 in h1:
                                    a = a + h2.text
                            else:
                                h1 = soup.find("article")
                                if h1 != -1:
                                    print("1")
                                    a = h1.text
                        rr.ree(a,i)
                except:
                    continue
        except:
            db.rollback()

        db.close()

#readable(297,367)