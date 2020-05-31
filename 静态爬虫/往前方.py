# _*_ coding:utf-8 _*_

import requests
from lxml import etree
import csv
import time
import os

URL = 'http://qianfangzy.com/'
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}
content = []
req = requests.get(URL, headers=HEADER)
html = etree.HTML(req.content)
title = html.xpath('//div[@class="content"]//h2/a[@title]/text()')
times = html.xpath('//div[@class="content"]//p[@class="meta"]//time//text()')
html1 = html.xpath('//div[@class="content"]//h2/a[@target="_blank"]/@href')

for x, y, z in zip(title, times, html1):
    dict1 = {'标题': x, '发布时间': y, '网址': z}
    content.append(dict1)
if not os.path.isdir(r'e:\资源'):
    os.mkdir(r'e:\资源')
with open('e:\资源\往前方' + time.strftime('%Y-%m-%d', time.localtime()) + '.csv', 'w',errors='ignore', newline='') as f:
    wr = csv.DictWriter(f, fieldnames=['标题', '发布时间', '网址'])
    wr.writeheader()
    wr.writerows(content)
print('往前方·下载，已完成')
