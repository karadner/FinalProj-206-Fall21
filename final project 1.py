from typing import List, Tuple
from bs4 import BeautifulSoup
import requests
import unittest
import sqlite3
import json
import os
import matplotlib
import matplotlib.pyplot as plt

#restaurantname, typefood, money symbol, reviews, location
def get_data_from_website(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    name_tags = soup.find_all('h2')
    type_tags=soup.find_all('div', class_='overview__3pYsRoNl')
    review_tags=soup.find_all('div', class_='ratingReviews__33xaxtwo')
    location_tags=soup.find_all('div',class_='address__28bKEZcw')
    name_info = []
    type_info=[]
    money_info=[]
    review_info=[]
    location_info=[]
    for tag in name_tags:
        for sub_tag in tag:
            for tagg in sub_tag:
                name_info.append(tagg)
    for tag in type_tags:
        for sub_tag in tag:
            for tagg in sub_tag:
                if str(tagg)[0].isalpha():
                    type_info.append(tagg)
    for tag in type_tags:
        for sub_tag in tag:
            for tagg in sub_tag:
                if str(tagg).startswith('$'):
                    money_info.append(tagg)
    for tag in review_tags:
        for sub_tag in tag:
            for tagg in sub_tag:
                for taggg in tagg:
                    if str(taggg)[0].isdigit():
                        review_info.append(taggg)
    for tag in location_tags:
        for sub_tag in tag:
            for tagg in sub_tag:
                location_info.append(tagg)
    print(name_info, type_info,  money_info,  review_info,  location_info)

get_data_from_website('https://www.opentable.com/lists/top-100-2021')
        #for sub_tag in tag:
            #for sub_tags in sub_tag:
                #if '\n' not in sub_tags:
                    #collect_info.append(sub_tags)
    #sub_list=[]
   # count=0
   # for i in range(len(collect_info)):
     #   sub_list.append(collect_info[i])
      #  count+=1
       # if count % 3==0:
       #     final_info_lst.append(sub_list)
          #  sub_list=[]
    #return final_info_lst

#def setUpDatabase(db_name):
    #path = os.path.dirname(os.path.abspath(__file__))
    #conn = sqlite3.connect(path+'/'+db_name)
   # cur = conn.cursor()
    #return cur, conn

#def setup_movietable(data, cur, conn):
  #  cur.execute("CREATE TABLE movie_table (id INTEGER PRIMARY KEY, title TEXT, year TEXT)")
  #  id=0
   # count=0
   ## while count <=25:
     #   for item in data[1:]:
      #  position=item.find('\n')
      #  if position != -1:
            #item=item[0:position]
       # digit_postion=0
       # for letter in item:
       #     digit_postion+=1
       ##     if letter.isdigit():
       #         break
       # nutrition_fact=item[0:digit_postion-2]
       # id+=1
       # nutrition_number=item[digit_postion-1:]
       # if dtaa in table:
       #     continue
        #else:
       # #    cur.execute("INSERT INTO dc_popcorn (id, nutrition_fact , nutrition_number ) VALUES (?,?,?)",(id, nutrition_fact , nutrition_number))
         #   count+=1
    #conn.commit()
    

        


print(get_data_from_website('https://www.imdb.com/list/ls055592025/'))
      