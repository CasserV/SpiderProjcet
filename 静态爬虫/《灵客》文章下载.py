#!/usr/bin/env python
# coding: utf-8

import requests
from lxml import etree
import os
import time


URL_LIST=[]#存放爬取链接


HEADER={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'cookie': 'Hm_lvt_15b06446a3f9b54a04ddbcc6490f2060=1607677019; Hm_lpvt_15b06446a3f9b54a04ddbcc6490f2060=1607677255'
}


req_Href=[]
req_Title=[]
for title_Url in URL_LIST:
    req=requests.get(title_Url,headers=HEADER)
    req_Html=etree.HTML(req.content)
    req_Href+=req_Html.xpath('/html/body/div/div[4]/div/div/main/article/div[1]/blockquote/p/span/a/@href')
    req_Title+=req_Html.xpath('/html/body/div/div[4]/div/div/main/article/div[1]/blockquote/p/span/a/text()')
    req_Href+=req_Html.xpath('/html/body/div/div[4]/div/div/main/article/div[1]/blockquote/p/a/@href')
    req_Title+=req_Html.xpath('/html/body/div/div[4]/div/div/main/article/div[1]/blockquote/p/a/span/text()')


for x,y in zip(req_Href,req_Title):
    if os.path.exists('e:\\'+'文件夹名'+'\\'+y+'.txt'):
        pass
    else:
        req_Con=requests.get(x,headers=HEADER)
        con_Html=etree.HTML(req_Con.content)
        page_Content=con_Html.xpath('/html/body/div/div[4]/div/div/main/article/div/p/text()')
        with open('e:\\a\\'+y+'.txt','w',encoding='utf-8',errors='ingore') as f:
            for con_Line in page_Content:
                f.write(con_Line+'\n')
        time.sleep(1)





