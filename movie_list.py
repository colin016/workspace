#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-11 16:38:19
# @Author  : colin liao (colinliao@126.com)
# @Link    : ${link}
# @Version : $Id$

import os
import sys
import io
import requests
from bs4 import BeautifulSoup


def getHtmlText(url):
	try:
	    r = requests.get(url, timeout=30)
	    r.raise_for_status()
	    r.encoding = 'gb2312'
	    #print(r.text)
	    return r.text

	except:
		print('some error')

def getContent(url):

	comments = []

	try:
		data = getHtmlText(url)
		soup = BeautifulSoup(data, 'lxml')
		#print(soup.title)

		ulTag = soup.find('ul', attrs={'class':'picList clearfix'})

		liTags = ulTag.find_all('li')

		print(liTags[0])
		
		for li in liTags:
			comment['name'] = li.find('a', attrs={'class':'aPlayBtn'}).text.strip()
			print(comment['name'])

	except:
		print('error')


def main(url):
    sys.stdout = io.TextIOWrapper(
        sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

    getContent(target_url)


target_url = 'http://dianying.2345.com/top/'

if __name__ == '__main__':
    main(target_url)
