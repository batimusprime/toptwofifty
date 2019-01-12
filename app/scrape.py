#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: github.com/batimusprime
File: IMDB Top 250 Watcher / scrape.py
Purpose: Scrape IMDB website, return top 250 movie list as organized structure
Date: 1/5/2019
#https://www.imdb.com/search/title?groups=top_250&sort=user_rating
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen
page = urlopen('https://www.imdb.com/search/title?groups=top_250&sort=user_rating')