# -*-coding:utf-8-*-
import requests
from lxml import etree
import csv
import datetime

LEARN_URL = 'https://52sharing.cn/category/learning-materials'
BOOK_URL = 'https://52sharing.cn/category/book'
MODEL_URL = 'https://52sharing.cn/category/templet'
HOT_URL = 'https://52sharing.cn/category/hot'

URL_TITLE_LIST = [LEARN_URL, BOOK_URL, MODEL_URL, HOT_URL]
LIST1 = []

HEADER = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'referer': 'https://52sharing.cn/',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'}


def url_spider(URL):
    req = requests.get(URL, headers=HEADER)
    req_Html = etree.HTML(req.text)
    req_Href = req_Html.xpath('/html/body/section/div[2]/div/article//header/h2/a/@href')
    req_Title = req_Html.xpath('/html/body/section/div[2]/div/article//header/h2/a/@title')
    req_Time = req_Html.xpath('/html/body/section/div[2]/div/article//p/span[2]/text()')

    for x, y, z in zip(req_Title, req_Time, req_Href):
        dict1 = {'名称': x, '发布时间': y, '网址': z}
        LIST1.append(dict1)

    with open("e:/资源/" + '吾爱分享' + str(datetime.date.strftime(datetime.datetime.today(), '%Y-%m-%d')) + '.csv', 'w',
              newline='', errors='ignore')as f:
        writer_file = csv.DictWriter(f, fieldnames=['名称', '发布时间', '网址'])
        writer_file.writeheader()
        writer_file.writerows(LIST1)

if __name__ == '__main__':
    for url in URL_TITLE_LIST:
        url_spider(url)
    print('吾爱分享·下载，已完成')
