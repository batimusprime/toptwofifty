# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 16:04:09 2019

@author: Batimus
"""

from bs4 import BeautifulSoup
import re
#bs object as list

#create empty list
mov_list = []
from urllib.request import urlopen
page = urlopen('https://www.imdb.com/search/title?groups=top_250&sort=user_rating')
#create BS object
soup = BeautifulSoup(page, 'html.parser')
#define movie list
#parse object for list of TD elements with class titleColumn
mov_list = soup.find_all('h3', { 'class' : 'lister-item-header' })


#extract position

for mdate in mov_list:
    s = mdate.span.text
    f = re.sub(r'[^\w]', ' ', s)
    print(f)  
    #remove the period
    

#extract name


#extract date
