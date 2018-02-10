#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bs4

soup = bs4.BeautifulSoup(open('data.html'), 'lxml')

# print(soup.prettify())

# print(soup.title)

# print(soup.body)

# print(soup.body.b)

# print(soup.body.p)

tag = soup.find_all('a')

print(tag[1])

print(soup.head)
