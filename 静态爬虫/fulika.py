#-*- coding:utf-8 -*-

import requests
from lxml import etree
import time
import csv
URL='http://www.fulika.net/page/1'


HEADER={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
}
def url_spider():
    spider_list=[]
    req=requests.get(URL,headers=HEADER).content
    page_html=etree.HTML(req)
    href=page_html.xpath('/html/body/section/div[2]/div/article/a/@href')
    title=page_html.xpath('/html/body/section/div[2]/div/article/header/h2/a/@title')
    time=page_html.xpath('/html/body/section/div[2]/div/article/p[1]/time/text()')
    for x,y,z in zip(title,time,href):
         spider_list.append({'名称':x,'发布时间':y,'网址':z})
    return  spider_list

def save_spider(spider_list):
    with open(r'e:/资源/fulika'+time.strftime('%Y-%m-%d',time.localtime())+'.csv','w',encoding='gb2312',newline='',errors='ignore')as f:
        cv=csv.DictWriter(f,fieldnames=['名称','发布时间','网址'])
        cv.writeheader()
        cv.writerows(spider_list)

if __name__ == '__main__':
    save_spider(url_spider())
    print('falika·下载，已完成')
    # print(url_spider())