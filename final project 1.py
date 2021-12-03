from typing import ItemsView, List, Tuple
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
    return name_info, type_info,  money_info,  review_info,  location_info


def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def setup_restaurantstable(data, cur, conn):
    cur.execute("DROP TABLE IF EXISTS restaurants_table")
    cur.execute("CREATE TABLE restaurants_table (id INTEGER PRIMARY KEY, name TEXT, type TEXT, money TEXT, review TEXT, location TEXT)")
    id=0
    count=0
    #while count <=25:
    final_list=[]
    for item in data:
        final_list.append(item)
    for i in range(len(final_list)):
        for item in range(len(final_list[i])):
            name = final_list[0][item]
            type=final_list[1][item]
            money=final_list[2][item]
            review=final_list[3][item]
            location=final_list[4][item]
            id+=1
            cur.execute("INSERT OR IGNORE INTO restaurants_table (id, name, type, money, review, location) VALUES (?,?,?,?,?,?)",(id, name, type,money,review,location))
        conn.commit()
    
cur, conn = setUpDatabase('restaurants_database')
web=get_data_from_website('https://www.opentable.com/lists/top-100-2021')
setup_restaurantstable(web, cur, conn)



      