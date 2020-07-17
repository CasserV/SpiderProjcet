#-*- coding:utf-8 -*-

import requests
from lxml import etree
import json
HEADER={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'refer':'https://www.bbwc.cn/',
    'origin':'https://www.bbwc.cn'
}

URL='https://content-cdn-bb.bbwc.cn/slateInterface/v10/app_1/web/tag/articleListByLevel?datatype=2&limited=3&hasPic=1&level=0'
req=requests.get(URL,headers=HEADER)
json1=json.loads(req.content)
# html=etree.HTML(req.content)
# div=html.xpath("//div[@class='contain top']/div/a")
title=json1['articletag'][0]['article']
url=json1['articletag'][0]['article']

for x,y in zip(title,url):
    print(x['title'],y['weburl'])
# print(title,url)


