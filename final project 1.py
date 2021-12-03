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

def calculate_average(cur, conn):
    cur.execute("SELECT type, money FROM restaurants_table")
    info=cur.fetchall()
    type_count=0
    money_count=0
    for item in info:
        if item[0]=="American":
            type_count+=1
            money_count+=len(item[1])
    american_average=money_count/type_count
    for item in info:
        if item[0]=="Contemporary American":
            type_count+=1
            money_count+=len(item[1])
    contemp_amer_average=money_count/type_count
    for item in info:
        if item[0]=="Italian":
            type_count+=1
            money_count+=len(item[1])
    italian_average=money_count/type_count
    for item in info:
        if item[0]=="Afghan":
            type_count+=1
            money_count+=len(item[1])
    afghan_average=money_count/type_count
    for item in info:
        if item[0]=="French":
            type_count+=1
            money_count+=len(item[1])
    french_average=money_count/type_count
    for item in info:
        if item[0]=="Southwest":
            type_count+=1
            money_count+=len(item[1])
    southwest_average=money_count/type_count
    for item in info:
        if item[0]=="Contemporary French":
            type_count+=1
            money_count+=len(item[1])
    contemp_french_average=money_count/type_count
    for item in info:
        if item[0]=="Tapas / Small Plates":
            type_count+=1
            money_count+=len(item[1])
    tapas_average=money_count/type_count
    for item in info:
        if item[0]=="French American":
            type_count+=1
            money_count+=len(item[1])
    french_amer_average=money_count/type_count
    for item in info:
        if item[0]=="Seafood":
            type_count+=1
            money_count+=len(item[1])
    sea_average=money_count/type_count
    for item in info:
        if item[0]=="Winery":
            type_count+=1
            money_count+=len(item[1])
    winery_average=money_count/type_count
    for item in info:
        if item[0]=="Steakhouse":
            type_count+=1
            money_count+=len(item[1])
    steakhouse_average=money_count/type_count
    for item in info:
        if item[0]=="Greek":
            type_count+=1
            money_count+=len(item[1])
    greek_average=money_count/type_count
    for item in info:
        if item[0]=="Fusion / Eclectic":
            type_count+=1
            money_count+=len(item[1])
    fusion_average=money_count/type_count
    for item in info:
        if item[0]=="Mediterranean":
            type_count+=1
            money_count+=len(item[1])
    medit_average=money_count/type_count
    for item in info:
        if item[0]=="Vietnamese":
            type_count+=1
            money_count+=len(item[1])
    viet_average=money_count/type_count
    for item in info:
        if item[0]=="Peruvian":
            type_count+=1
            money_count+=len(item[1])
    peru_average=money_count/type_count
    for item in info:
        if item[0]=="Mexican":
            type_count+=1
            money_count+=len(item[1])
    mexican_average=money_count/type_count
    for item in info:
        if item[0]=="Steak":
            type_count+=1
            money_count+=len(item[1])
    steak_average=money_count/type_count
    for item in info:
        if item[0]=="Sushi":
            type_count+=1
            money_count+=len(item[1])
    sushi_average=money_count/type_count
    for item in info:
        if item[0]=="Fish":
            type_count+=1
            money_count+=len(item[1])
    fish_average=money_count/type_count
    for item in info:
        if item[0]=="Traditional French":
            type_count+=1
            money_count+=len(item[1])
    trad_french_average=money_count/type_count
    for item in info:
        if item[0]=="Farm-to-table":
            type_count+=1
            money_count+=len(item[1])
    farm_average=money_count/type_count
    for item in info:
        if item[0]=="Croatian":
            type_count+=1
            money_count+=len(item[1])
    croatian_average=money_count/type_count
    for item in info:
        if item[0]=="Speakeasy":
            type_count+=1
            money_count+=len(item[1])
    speak_average=money_count/type_count
    
    final_str=american_average, italian_average, contemp_amer_average, afghan_average, french_average, southwest_average, contemp_french_average, tapas_average, french_amer_average, sea_average, winery_average, steakhouse_average, greek_average, fusion_average, steak_average, medit_average, viet_average, peru_average, mexican_average, sushi_average, fish_average, trad_french_average, farm_average, croatian_average, speak_average
    final_list=[]
    final_list.append(final_str)

    with open('restaurants.txt', 'w') as f:
        for item in info:
            for i in range(len(final_list)):
               f.writelines('The average cost of ' + str(item[0][i]) + 'type of restaurant is $' + str(final_list[i]) + ".")
               f.write('\n')
    f.close()

    # type_dict={}
    # money_dict={}
    # final_dict={}
    # count_money=0
    # for item in info:
    #     if item[0] not in type_dict:
    #         type_dict[item[0]]=0
    #     type_dict[item[0]]+=1
    #     if item[0]==item[0]:
    #         dollar=len(item[1])
    #         count_money+=dollar
    #         money_dict[item[0]]=count_money
    #         #print(count_money)
    #     #final_dict[item[0]]=count_money/type_dict[item][1]
    # #print(final_dict)


cur, conn = setUpDatabase('restaurants_database')
web=get_data_from_website('https://www.opentable.com/lists/top-100-2021')
setup_restaurantstable(web, cur, conn)
calculate_average(cur,conn)





      