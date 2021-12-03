from typing import ItemsView, List, Tuple
from bs4 import BeautifulSoup
import requests
import unittest
import sqlite3
import json
import os
import matplotlib
import matplotlib.pyplot as plt
import random

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

def create_table(cur,conn):
    cur.execute("DROP TABLE IF EXISTS restaurants_table")
    cur.execute("CREATE TABLE restaurants_table (id INTEGER PRIMARY KEY, name TEXT, type TEXT, money TEXT, review TEXT, location TEXT)")
def setup_restaurantstable(data, cur, conn):
    id=0
    count=0
    final_list=[]
    for item in data:
        final_list.append(item)
    cur.execute("SELECT name FROM restaurants_table")
    names=cur.fetchall()
    name_list=[]
    for tup in names:
        name_list.append(tup[0])
    cur.execute("SELECT id FROM restaurants_table")
    ids=cur.fetchall()
    id_list=[]
    for tup in ids:
        id_list.append(int(tup[0]))
    try:
        id=max(id_list)
    except:
        id=0
        create_table(cur,conn)
    while count <25:
        if id>=100:
            break
        for i in range(id,id+25):
            if final_list[0][i] not in name_list:
                name = final_list[0][i]
                type=final_list[1][i]
                money=final_list[2][i]
                review=final_list[3][i]
                location=final_list[4][i]
                id+=1
                count+=1
                cur.execute("INSERT OR IGNORE INTO restaurants_table (id, name, type, money, review, location) VALUES (?,?,?,?,?,?)",(id, name, type,money,review,location))    
        conn.commit() 

# def calculate_average(column, cur, conn):
#     cur.execute("SELECT review, money FROM restaurants_table orn ON dc_popcorn.nutrition_fact=av_popcorn.nutrition_fact JOIN ch_popcorn ON dc_popcorn.nutrition_fact=ch_popcorn.nutrition_fact JOIN gold_popcorn ON dc_popcorn.nutrition_fact=gold_popcorn.nutrition_fact JOIN sweet_popcorn ON dc_popcorn.nutrition_fact=sweet_popcorn.nutrition_fact JOIN oh_popcorn ON dc_popcorn.nutrition_fact=oh_popcorn.nutrition_fact JOIN wh_popcorn ON dc_popcorn.nutrition_fact=wh_popcorn.nutrition_fact WHERE dc_popcorn.nutrition_fact=?", (fact, ))
#     columns=cur.fetchall()

    
cur, conn = setUpDatabase('restaurants_database')
web=get_data_from_website('https://www.opentable.com/lists/top-100-2021')
setup_restaurantstable(web, cur, conn)




      