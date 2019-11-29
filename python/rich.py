import requests
import pymysql
import time
import random
from bs4 import BeautifulSoup
import chardet
import pdfplumber
import fitz
import re
import os
import sys
import urllib3
import rich_2word

ca = urllib3.PoolManager()
urllib3.disable_warnings()
db = pymysql.connect("203.64.84.94", "Fish", "851217", "project105")
#db = pymysql.connect("localhost", "root", "97462835", "project105")
cur = db.cursor()
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

def pdf2pic(path):
    # 使用正则表达式来查找图片
    checkXO = r"/Type(?= */XObject)"
    checkIM = r"/Subtype(?= */Image)"
    # 打开pdf
    doc = fitz.open(path)
    # 图片计数
    imgcount = 0
    lenXREF = doc._getXrefLength()
    # 遍历每一个对象
    for i in range(1, lenXREF):
        # print(i)
        # 定义对象字符串
        text = doc._getXrefString(i)
        isXObject = re.search(checkXO, text)
        # 使用正则表达式查看是否是图片
        isImage = re.search(checkIM, text)
        # 如果不是对象也不是图片，则continue
        if not isXObject or not isImage:
            continue
        imgcount += 1
    return imgcount


def rich_html(soup, i):

    d = {}
    ma = 0
    div = None
    divv = None
    al = soup.find("article")
    if al != None:
        divv = al
    else:
        ps = soup.find_all('p')
        if ps != None:
            for p in ps:
                div = p.find_parent("div")
                if div!=None:
                    #print(div)
                    if div in d:
                        d[div] = d[div] + 1
                    else:
                     d[div] = 0
            #print(d)
                for dd in d:
                    if d[dd] >= ma:
                        divv = dd
                        ma = d[dd]
            #divv=div
    if divv==None:
        divv=soup
    if divv != None:
        im = divv.find_all("img")
        cim = len(im)
        for g in im:
            try:
                if int(g.get("height")) < 100 and int(g.get("width")) < 100:
                    cim = cim - 1
            except:
                continue

        ta = divv.find_all("table")
        if ta == -1 or ta == None:
            ta = {}

        vi = soup.find_all("iframe")
        if vi == -1 or vi == None:
            vi = {}
        cvi = len(vi)
        for v in vi:
            try:
                if int(v.get("height")) <= 200 or int(v.get("width")) <= 400:
                    cvi = cvi - 1
            except:
                continue

        a = divv.find_all("a")
        if a == -1 or a == None:
            a = {}

        if cim > 5:
            x1 = 1
        else:
            x1 = cim / 5

        if len(ta) > 8:
            x2 = 1
        else:
            x2 = len(ta) / 8

        if cvi > 1:
            x3 = 1
        else:
            x3 = cvi

        if len(a) > 20:
            x4 = 1
        else:
            x4 = len(a) / 20
        ri = 0
        ri = 1.925 * (x1 + x2) + 3.15 * x3 + 3 * x4
        print(i, cim, len(ta), cvi, len(a), ri)
        sql2 = "UPDATE disease_t SET rich = '%f' WHERE id = '%d'" % (ri, i)
        try:
            cur.execute(sql2)
            db.commit()
        except:
            db.rollback()


def rich_pdf(u, i):
    r = requests.get(u)
    pdf = r.content
    with open("C:/105專題/105316126/a.pdf", "wb") as f:
    #with open("C:/Users/user/Desktop/105專題/pdf/a.pdf", "wb") as f:
        f.write(pdf)
    f.close()
    t = 0
    #im = 0 
    #with pdfplumber.open("C:/Users/user/Desktop/105專題/pdf/a.pdf",password='') as pdf:
    with pdfplumber.open("C:/105專題/105316126/a.pdf",password='') as pdf:
        print(len(pdf.pages))
        for ind in range(len(pdf.pages)):
            page = pdf.pages[ind]
            t = t + len(page.extract_tables())
    pdf.close()

    path = r"C:/105專題/105316126/a.pdf"

    m = pdf2pic(path)
    if m > 5:
        x1 = 1
    else:
        x1 = m / 5

    if t > 8:
        x2 = 1
    else:
        x2 = t / 8
    ri = 0
    ri = 1.925 * (x1 + x2)
    sql2 = "UPDATE disease_t SET rich = '%f' WHERE id = '%d'" % (ri, i)
    try:
        cur.execute(sql2)
        db.commit()
    except:
        db.rollback()
    print(i, t, m, ri)


# main
def rich(st,en):
    for i in range(st,en):
        sq4 = "SELECT url FROM disease_t WHERE id='%d'" % (i)
        try:
            cur.execute(sq4)
            res = cur.fetchall()
            u = res[0][0]
        except:
            db.rollback()

        if u != None:
            #pd = u.find("pdf")
            try:
                if u.endswith(".pdf"):
                    print(u)
                    rich_pdf(u, i)
                else:
                    html = getweb(u)
                    if html != None:
                        soup = BeautifulSoup(html, 'html.parser')
                        rich_html(soup, i)
            except:
                continue
    db.close()
    rich_2word.rich_voc(st,en)
#rich_2word.rich_voc(534,568)
rich(1,30)