# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 22:56:12 2019

@author: Batimus
"""
from bs4 import BeautifulSoup

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
print('1/6: Movie list created')

#extract movie name
def movie_name_extractor(mov_list):
    temp_name_list = []
    for name in mov_list:
        temp_name_list.append(name.a.text)
    print('2/6: Movie names extracted')
    return temp_name_list

movie_name_list = movie_name_extractor(mov_list)

#extract movie date

def movie_date_extractor(mov_list):
    temp_date_list = []
    for m_date in mov_list:
        temp_date_list.append(m_date.span.text)
    print('3/6: Movie dates extracted')

    return temp_date_list

movie_date_list = movie_date_extractor(mov_list)


#function zips name and date
def zip_function(name, m_date):
    temp_list = zip(name, m_date)
    print('4/6: Movies and dates zipped')
    return temp_list

#create list of tuples containing name and date
final_list = zip_function(movie_name_list,movie_date_list)

#open file
output_file= open('output.txt','w+')
print('5/6: Preparing to write to file')
#write tuples to file
for l,d in final_list:
    output_file.write(l + ' : ' + d + ', \n')
#close file
output_file.close()
print('6/6: Output.txt created, process complete')

