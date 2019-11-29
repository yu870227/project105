import requests
from bs4 import BeautifulSoup
import re
import pymysql
import random
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'}


def getweb(url):
    time.sleep(100)
    htmlpage = requests.get(url, headers=headers,timeout=5)
    if htmlpage.status_code != 200:
        print(htmlpage.status_code)

    else:
        return htmlpage.text


def ree(u, gu):
    print(gu)

    db = pymysql.connect("203.64.84.94", "Fish", "851217", "project105")
    #db = pymysql.connect("localhost", "root", "97462835", "project105")
    cur = db.cursor()
    c3 = []
    c1 = u.split('，')
    for i in range(len(c1)):
        c2 = c1[i].split(' ')
        c3.extend(c2)

    c2 = []
    for i in range(len(c3)):
        c1 = c3[i].split('。')
        c2.extend(c1)

    c1 = []
    for i in range(len(c2)):
        c3 = c2[i].split('？')
        c1.extend(c3)

    c3 = []
    for i in range(len(c1)):
        c2 = c1[i].split('!')
        c3.extend(c2)

    c2 = []
    for i in range(len(c3)):
        c1 = c3[i].split('；')
        c2.extend(c1)

    snum = 0
    scount = 0

    for z in range(len(c2)):

        c2[z] = c2[z].replace('\n', '')
        st = re.sub("[\s+\.\!\/_,$%^*()+\"\']+|[+——！★◎：X:《》【】，。？、～~@#￥%……&*（）「」]+", "", c2[z])

        for j in range(len(st) - 1):

            print(st[j:j + 2],gu)
            if st[j:j + 1].encode('UTF-8').isalpha() or st[j + 1:j + 2].encode('UTF-8').isalpha():

                continue

            else:
                sql2 = " SELECT value FROM googlesearch_t WHERE name='%s'" % (st[j:j + 2])

                try:

                    cur.execute(sql2)
                    nu = cur.fetchall()
                    print(len(nu))
                    if len(nu) == 0:
                        key = '"' + st[j:j + 2] + '"'
                        res = "https://www.google.com.tw/search?q=" + key
                        html = getweb(res)
                        if html != None:
                            soup = BeautifulSoup(html, 'html.parser')
                            st1 = soup.find("div", id="resultStats")
                            a = st1.text.find("項")
                            st2 = st1.text[3:a]
                            st2 = st2.replace(",", "")

                            n3 = int(st2)
                            db.ping()
                            sql3 = "INSERT INTO googlesearch_t(name,value) VALUES ('%s','%d')" % (st[j:j + 2], n3)
                            try:
                                cur.execute(sql3)
                                db.commit()
                            except:
                                db.rollback()

                        t = random.randint(20, 50)
                        time.sleep(t)

                    else:
                        n3 = int(nu[0][0])

                    print(n3)

                    if n3 >= 100000000:
                        x3 = 1
                    elif n3 <= 5000000:
                        x3 = 0
                    else:
                        x3 = (n3 / 10000) / 9500 - 0.0526315789

                    snum = snum + x3

                    scount = 1 + scount

                except:

                    db.rollback()
    db.ping()
    sqlreadable="SELECT readable FROM disease_t WHERE id='%d'"%(gu)
    try:
        cur.execute(sqlreadable)
        res = cur.fetchall()
        u = res[0][0]
    except:
        db.rollback()

    y3 = snum / scount
    a1 = u+(0.35 * y3) * 10
    print(gu, a1)

    nea=(a1-5.25)/2.3
    if nea>1:
        nea=1
    elif nea<0:
        nea=0

    sql4 = "UPDATE disease_t SET readable = '%f',norreadable='%f' WHERE id = '%d'" % (a1,nea*10, gu)
    try:
        cur.execute(sql4)
        db.commit()
    except:
        db.rollback()

    db.close()

