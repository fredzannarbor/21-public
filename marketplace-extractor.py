# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 19:41:44 2016

@author: fred
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(open("/home/fred/Dropbox/Downloads/21mktoct.html"))

BeautifulSoup('<span class="price-amount">')
spans = soup.find_all('span', attrs={'class':'price-amount'})
for span in spans:
    print(span.string)


titles = soup.find_all('h3', attrs={'class':'data-market-endpoint-title'})
for title in titles:
    print(title.string)

sources=soup.findAll('a',{"data-keyword":True})
for source in sources:
    print(source['data-keyword'])

titles = soup.find_all('a', attrs={'class':'data-market-project-url'})
for title in titles:
    print(title.string)

codes = soup.find_all('code', attrs={'class': 'data-market-quickbuy'})
for code in codes:
    print(code.string)

#for link in soup.find_all('a'):
 #   print(link.get('href'))