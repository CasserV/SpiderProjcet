# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

URL = 'https://language.chinadaily.com.cn/audio_cd'
HEADER = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",

}


def parse_catalogue(url):
    req = requests.get(url, headers=HEADER)
    bs = BeautifulSoup(req.content, 'lxml')
    a = bs.find_all('a', target='_blank', shape="rect")[3]
    for x in a:
        html1 = 'http:' + a['href']
        p_tag, title = parse_content(html1)
        save_content(p_tag, title)


def parse_content(url):
    reqs = requests.get(url)
    bs_content = BeautifulSoup(reqs.content, 'lxml')
    div_tag = bs_content.find_all('div', class_='mian_txt')
    title = bs_content.find('span', class_='main_title1').text
    for x in div_tag:
        p_tag = x.find_all('p')
        return p_tag, title


def save_content(p_tag, title):
    with open('e:/资源/' + title + ".txt", 'w', encoding='gb18030') as f:
        f.write(title.center(100) + '\n')
        for y in p_tag:
            f.write('\t' + re.sub('Find more audio news on the China Daily app.','',y.text)+'\n')

if __name__ == '__main__':
    parse_catalogue(URL)
    print('ChinaDaily·当日新闻下载，已完成')
