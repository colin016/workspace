#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-11 10:25:57
# @Author  : colin liao (colinliao@126.com)
# @Link    : ${link}
# @Version : $Id$

import requests
from bs4 import BeautifulSoup


def get1_html(url):
    try:
        r = requests.get(url, timeout=30)
        # print(r.content)
        r.raise_for_status()

        # 这里我们知道百度贴吧的编码是utf-8，所以手动设置的。爬去其他的页面时建议使用：
        # r.endcodding = r.apparent_endconding
        r.encoding = 'utf-8'
        print(r.text)
        return r.content
    except:
        return " ERROR "

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        # 这里我们知道百度贴吧的编码是utf-8，所以手动设置的。爬去其他的页面时建议使用：
        # r.endcodding = r.apparent_endconding
        r.encoding = 'utf-8'
        return r.text
    except:
        return " ERROR "

def get_content(url):
    # 初始化一个列表来保存所有的帖子信息：
    # print('get_content started')

    comments = []
    # 首先，我们把需要爬取信息的网页下载到本地
    html = get_html(url)

    soup = BeautifulSoup(html, 'lxml')

    liTags = soup.find_all('li', attrs={'class': ' j_thread_list clearfix'})


    # 通过循环找到每个帖子里的我们需要的信息：
    for li in liTags:
        # 初始化一个字典来存储文章信息
        comment = {}

        # 使用try except，防止爬虫找不到信息而停止运行
        try:
            # 开始筛选信息，保存到字典中
            comment['title'] = li.find(
                'a', attrs={'class': 'j_th_tit '}).text.strip()
            print(content['title'])

            comment['link'] = "http://tieba.baidu.com" + \
                li.find('a', attrs={'class': 'j_th_tit '})['href']
            print(content['link'])

            comment['author'] = li.find(
                "span", sttrs={'class': 'tb_icon_author '}).text.strip()
            print(comment['author'])

            comment['time'] = li.find(
                'span', sttrs={'class': 'pull-right is_show_create_time'}).text.strip()
            print(comment['time'])

            comment['reply_num'] = li.find(
                'span', sttrs={'class': 'threadlist_rep_num center_text'}).text.strip()
            print(comment['reply_num'])

            comments.append(comment)

        except:
            print('something wrong')

    return comments





def main(base_url, deep):
    url_list = []
    for i in range(0, deep):
        url_list.append(base_url + '&pn=' + str(50 * i))
        print(url_list[i])

    for url in url_list:
        get_content(url)

base_url = 'http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8'

deep = 1

if __name__ == '__main__':
    main(base_url, deep)
