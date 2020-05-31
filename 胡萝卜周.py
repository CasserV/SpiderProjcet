# -*- coding:utf-8 -*-

import csv
import time
import requests
from lxml import etree


URL = 'http://www.carrotchou.blog/page/{}'
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Connection': 'keep-alive',
    'Cookie': 'UM_distinctid=1706a4e3ca5516-02ae0099469b1e-3c604504-1fa400-1706a4e3ca6322; CNZZDATA1261216155=1067907455-1582326658-https%253A%252F%252Fwww.baidu.com%252F%7C1582330570'
}


def spider_app(url, header):
    content_list1 = []
    for num in range(1,4):
        url_new=url.format(num)
        req = requests.get(url_new, header)
        html = etree.HTML(req.content)
        title = html.xpath('.//div[@class="content"]/article//h2/a/text()')
        content_url = html.xpath('.//div[@class="content"]/article//h2/a/@href')
        delivery_time = html.xpath('.//div[@class="content"]/article/p/time//text()')
        for x, y, z in zip(title, delivery_time, content_url):
            dict1={'名称':x,'发布时间':y,'网址':z}
            content_list1.append(dict1)
    return content_list1

def save_content(content_list):
    with open(r'e:\资源\胡萝卜周' + time.strftime('%Y-%m-%d', time.localtime()) + '.csv', 'w', encoding='gbk',
              newline='')as f:
        cr = csv.DictWriter(f, fieldnames=['名称', '发布时间', '网址'])
        cr.writeheader()
        cr.writerows(content_list)
        print('胡萝卜周·下载，已完成')


if __name__ == '__main__':
    content_list=spider_app(URL, HEADER)
    save_content(content_list)
