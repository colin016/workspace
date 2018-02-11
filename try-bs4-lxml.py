#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bs4

soup = bs4.BeautifulSoup(open('data.html'), 'lxml')

print(soup.prettify())

# print(soup.title)

# print(soup.body)

# print(soup.body.b)

# print(soup.body.p)

tag = soup.find_all('a')

# print(tag[1])

# print(soup.head)

print(tag[0]['id'])

print(tag[0].text)

print(tag[0].text.strip())

print(tag[0].get_text())

print(tag[1].text)

print(tag[1].text.strip())

print(tag[1].get_text())

print(tag[2].text)

print(tag[2].text.strip())

print(tag[2].get_text())

for i in range(0, 3):
	print(i)