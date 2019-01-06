#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: github.com/batimusprime
File: IMDB Top 250 Watcher / scrape.py
Purpose: Scrape IMDB website, return top 250 movie list as organized structure
Date: 1/5/2019

"""
from bs4 import BeautifulSoup

#create empty list
mov_list = []

#create BS object
soup = BeautifulSoup(open('source.html'), 'html.parser')

#parse object for list of TD elements with class titleColumn
mov_list = soup.find_all('td', { 'class' : 'titleColumn' })

#open file for writing            
output_file= open('output.txt','w+')

#iterate over list, selecting a elements, then text in between that element's tags
for mov in mov_list:
    output_file.write(mov.a.text +  ', ' + mov.span.text +  ', \n')
    
#close file
output_file.close()