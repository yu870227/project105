import requests
import random
import pymysql
from bs4 import BeautifulSoup
import time
import pdfplumber
import datetime
import re
import chardet
import random
import time
import rich
import fitz
import sys

def getwebpage(url):
    #your bot 0.1
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
    elif htmlpage.status_code == 200:
        return htmlpage.text

def all_crea(search):
    site = "https://www.google.com/search?q="+search+"&tbs=qdr:y19&ei=e9fPXKq7B-WSr7wP8PeB0Ag&start=0&sa=N&ved=0ahUKEwjq5OnNpobiAhVlyYsBHfB7AIo4FBDy0wMIeg&biw=691&bih=838"
    db = pymysql.connect("203.64.84.94", "Fish", "851217", "project105")
    #db = pymysql.connect("localhost", "root", "97462835", "project105")
    cur = db.cursor()
    a = "天前"
    b = "小時前"
    c = "分鐘前"
    d = "年月日"
    Today = datetime.date.today()
    ty = Today.year
    tm = Today.month
    td = Today.day

    sqlid="SELECT * FROM disease_t  ORDER BY id DESC LIMIT 0 , 1"

    try:
        cur.execute(sqlid)
        starid=cur.fetchall()
        starid=starid[0][0]
    except:
        db.rollback()


    html = getwebpage(site)
    for j in range(15):
        if html != None:
            soup = BeautifulSoup(html, 'html.parser')
            urlitems = soup.find_all("div", class_="g")
            for st1 in urlitems:
                st2 = st1.find("a")
                if st2 != None:
                    st3 = st2.find("h3")
                    if st3 != None:
                        st4 = st2.get('href')
                        # a=st4.find("&sa")
                        # st4=st4[7:a]
                        su = st4.find('youtube')
                        if su == -1:
                            st5 = st4.replace('%26', "&")
                            st6 = st5.replace("%3D", "=")
                            st7 = st6.replace("%3F", "?")
                            st8 = st7.replace("%25", "%")

                i = st1.find("span", class_="f")
                if i != None:
                    i = "".join(i)
                    i = i.replace("-", "")
                    ss = re.findall(r"([0-9]+)", i)
                    cc = re.findall(r"([\u4e00-\u9fa5]+)", i)
                    str1 = "".join(cc)
                    str2 = "".join(ss)
                    if str1 == d:  # 年月日
                        s = i[7]
                        if s == "月":
                            tmm = int(i[5:7])
                            tyy = int(i[0:4])
                        else:
                            tyy = int(i[0:4])
                            tmm = int(i[5:6])

                    elif str1 == a:  # 天
                        if td - int(str2) == 0:
                            tmm = int(tm - 1)
                            tyy = int(ty)

                        elif td - int(str2) < 0:
                            tmm = int(tm - 1)
                            tyy = int(ty)

                        else:
                            tmm = int(tm)
                            tyy = int(ty)

                    elif str1 == b:  # 小時
                        if int(str2) == 24:
                            td = td - 1
                            if td == 0:
                                tmm = int(tm - 1)
                                tyy = int(ty)
                            else:
                                tmm = int(tm)
                                tyy = int(ty)

                        else:
                            tmm = int(tm)
                            tyy = int(ty)

                    elif str1 == c:  # 分鐘
                        tmm = int(tm)
                        tyy = int(ty)
                        #print(i)
                Score = (ty - tyy) * 12 - (tmm - tm)
                if Score > 120:
                    y = 0 * 10
                elif Score == 0:
                    y = 1 * 10
                elif Score <= 120:
                    y = (1 - (((ty - tyy) * 12 - (tmm - tm)) * 0.00833)) * 10

                if st3 != None:
                    if su == -1:
                        #print("\n" + st3.text)
                        #print(st8)
                        if i!=None:
                            i=str(tyy)+"年"+str(tmm)+"月"
                            #print(i)
                            sql = "INSERT INTO disease_t (name,readable,rich,timely,url,date) VALUES ('%s','%f','%f','%f','%s','%s')"% (st3.text,0 , 0, y, st8, i)
                            try:
                                cur.execute(sql)
                                db.commit()
                            except:
                                db.rollback()
                        elif i==None:
                            print("none")
                            i="Null"
                            tyy=0
                            tmm=0
                            y=0
                            sql = "INSERT INTO disease_t (name,readable,rich,timely,url,date) VALUES ('%s','%f','%f','%f','%s','%s')"% (st3.text,0 , 0, y, st8, i)
                            try:
                                cur.execute(sql)
                                db.commit()
                            except:
                                db.rollback()

            print("第" + str(j) + "頁")
            nextpage = soup.find("a", id="pnnext")
            if nextpage != None:
                ul = nextpage.get("href")
                nexturl = "https://www.google.com" + ul
                #print(nexturl)
                t = random.randint(20, 50)
                time.sleep(t)
                html = getwebpage(nexturl)
            else:
                break

    sqlid="SELECT * FROM disease_t  ORDER BY id DESC LIMIT 0 , 1"

    try:
        cur.execute(sqlid)
        endid=cur.fetchall()
        endid=endid[0][0]
    except:
        db.rollback()

    db.close()
    rich.rich(starid,endid)
    #readable.readable(starid,endid)



if __name__=='__main__':
    print(sys.argv)
    all_crea(sys.argv[1])
