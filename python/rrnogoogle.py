import requests
from bs4 import BeautifulSoup
import re
from langdetect import detect
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

    # print(u)

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

    co = 0
    row = 0
    k = 0
    cn = 0
    en = 0
    e = 0

    for z in range(len(c2)):
        c2[z] = c2[z].replace('\n', '')
        st = re.sub("[\s+\.\!\/_,$%^*()+\"\']+|[+——！★◎：X:《》【】，。？、～~@#￥%……&*（）「」]+", "", c2[z])
        co = co + len(st)

        if len(st) > 0:
            row = row + 1

        for sti in range(len(st)):
            try:
                if detect(st[sti:sti+1]) == 'ko':
                    k = k + 1

                elif detect(st[sti:sti+1]) == 'zh-tw':
                    k = k + 1

                elif detect(st[sti:sti+1]) == 'zh-cn':
                    cn = cn + 1

                elif st[sti:sti+1].isalpha():
                    en = en + 1
                else:
                    e = e + 1
            except:
                continue
    avg=0
    if row!=0:
        avg = co / row

    if avg >= 26.31:
        y1 = 0
    elif avg <= 9.77:
        y1 = 1
    else:
        y1 = -0.057 * avg + 1.5

    x2 = 0.35 * (en / co) + 0.15 * (cn / co) + 0.5 * (e / co)
    y2 = -2 * x2 + 1
    a1 = (0.2 * y1 + 0.45 * y2 ) * 10
    print(gu, a1)

    nea=(a1-5.25)/2.3
    if nea>1:
        nea=1
    elif nea<0:
        nea=0

    db.ping()
    sql4 = "UPDATE disease_t SET readable = '%f',norreadable='%f' WHERE id = '%d'" % (a1,nea*10, gu)
    try:
        cur.execute(sql4)
        db.commit()
    except:
        db.rollback()

    db.close()