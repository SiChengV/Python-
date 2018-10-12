import re
import urllib.request
import json
import pymysql
import random, datetime
import bs4
import requests
import subprocess
import time

def getHtmlText():                                          #  获取网页
    try:
        url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2016.html'
        r = requests.get(url, timeout = 30)
        r.raise_for_status()                                # 如果请求网页失败则产生异常信息
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def fillUnivList(ulist, html):                            # 获取数据并将数据填入列表
    soup = bs4.BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printUnivList(ulist):                                    # 输出列表
    print("{:^10}\t{:^20}\t{:^10}".format('排名','学校','分数'))
    for each in ulist:
        print("{:^10}\t{:^20}\t{:^10}".format(each[0], each[1], each[2]))

def main():
    uinfo = []
    html = getHtmlText()
    fillUnivList(uinfo, html)
    printUnivList(uinfo)


main()
