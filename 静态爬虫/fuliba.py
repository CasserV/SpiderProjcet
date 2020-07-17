# -*- coding:utf-8 -*-
import requests
from lxml import etree
import csv
import time
HEADER = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
             'Referer':'https://fulibus.net/page/3',
             'Accept-Language':'zh-CN,zh;q=0.9'
}
list1=[]
reqs=requests.get('https://fulibus.net/',headers=HEADER)
html=etree.HTML(reqs.content)
href=html.xpath('//div[@class="content"]/article[@class]/a[@target]/@href')
title=html.xpath('/html/body/section/div[1]/div/article/header/h2/a/text()')
time1=html.xpath('//div[@class="content"]//p[@class]//time/text()')
title1=[]
for t in title:
    t1=t.encode('utf-8').decode('utf-8')#iso-8859-1
    title1.append(t1)
for w,x,y in zip(title1,time1,href):
    dict1={'名称':w,'发布时间':x,'网址':y}
    list1.append(dict1)
with open('e:/资源/'+'福利吧'+time.strftime(format("%Y-%m-%d"),time.localtime())+'.csv','w',encoding='gb2312',errors='ignore',newline='')as f:
    writer=csv.DictWriter(f,fieldnames=['名称','发布时间','网址'])
    writer.writeheader()
    writer.writerows(list1)
print('福利吧·下载，已完成')

