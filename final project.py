from typing import List, Tuple
from bs4 import BeautifulSoup
import requests
import unittest
import sqlite3
import json
import os



def get_data_from_website(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    nutrition_tags = soup.find_all('div', class_='d-flex')
    nutrition_lst = []
    header_tags=soup.find_all('h1', class_='h2')  
    for tag in header_tags:
        nutrition_lst.append(tag.text.strip())
    for tag in nutrition_tags:
        nutrition_lst.append(tag.text.strip())
    nutrition_lst.pop(1)
    return nutrition_lst[0:25]


obj1=get_data_from_website('https://lesserevil.com/collections/organic-popcorn/products/dark-chocolate-himalayan-pink-salt')
obj2=get_data_from_website('https://lesserevil.com/collections/organic-popcorn/products/avocado-licious-organic-popcorn?variant=28241948573789')
obj3=get_data_from_website('https://lesserevil.com/collections/organic-popcorn/products/classic-cheddah-organic-popcorn')
obj4=get_data_from_website('https://lesserevil.com/collections/organic-popcorn/products/himalayan-pink-salt-organic-popcorn')


def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def setUpdc_popcornTable(data, cur, conn):
    cur.execute("DROP TABLE IF EXISTS dc_popcorn")
    cur.execute("CREATE TABLE dc_popcorn (id INTEGER PRIMARY KEY, popcorn_type TEXT, nutrition_fact TEXT, nutrition_number TEXT)")
    id=0
    popcorn_type=data[0]
    for item in data[1:]:
        position=item.find('\n')
        if position != -1:
            item=item[0:position]
        digit_postion=0
        for letter in item:
            digit_postion+=1
            if letter.isdigit():
                break
        nutrition_fact=item[0:digit_postion-2]
        id+=1
        nutrition_number=item[digit_postion-1:]
        cur.execute("INSERT INTO dc_popcorn (id, popcorn_type , nutrition_fact , nutrition_number ) VALUES (?,?,?,?)",(id, popcorn_type , nutrition_fact , nutrition_number))
    conn.commit()


def setUpav_popcornTable(data, cur, conn):
    cur.execute("DROP TABLE IF EXISTS av_popcorn")
    cur.execute("CREATE TABLE av_popcorn (id INTEGER PRIMARY KEY, popcorn_type TEXT, nutrition_fact TEXT, nutrition_number TEXT)")
    id=0
    popcorn_type=data[0]
    for item in data[1:]:
        position=item.find('\n')
        if position != -1:
            item=item[0:position]
        digit_postion=0
        for letter in item:
            digit_postion+=1
            if letter.isdigit():
                break
        nutrition_fact=item[0:digit_postion-2]
        id+=1
        nutrition_number=item[digit_postion-1:]
        cur.execute("INSERT INTO av_popcorn (id, popcorn_type , nutrition_fact , nutrition_number ) VALUES (?,?,?,?)",(id, popcorn_type , nutrition_fact , nutrition_number))
    conn.commit()


def setUpch_popcornTable(data, cur, conn):
    cur.execute("DROP TABLE IF EXISTS ch_popcorn")
    cur.execute("CREATE TABLE ch_popcorn (id INTEGER PRIMARY KEY, popcorn_type TEXT, nutrition_fact TEXT, nutrition_number TEXT)")
    id=0
    popcorn_type=data[0]
    for item in data[1:]:
        position=item.find('\n')
        if position != -1:
            item=item[0:position]
        digit_postion=0
        for letter in item:
            digit_postion+=1
            if letter.isdigit():
                break
        nutrition_fact=item[0:digit_postion-2]
        id+=1
        nutrition_number=item[digit_postion-1:]
        cur.execute("INSERT INTO ch_popcorn (id, popcorn_type , nutrition_fact , nutrition_number ) VALUES (?,?,?,?)",(id, popcorn_type , nutrition_fact , nutrition_number))
    conn.commit()

def setUphim_popcornTable(data, cur, conn):
    cur.execute("DROP TABLE IF EXISTS him_popcorn")
    cur.execute("CREATE TABLE him_popcorn (id INTEGER PRIMARY KEY, popcorn_type TEXT, nutrition_fact TEXT, nutrition_number TEXT)")
    id=0
    popcorn_type=data[0]
    for item in data[1:]:
        position=item.find('\n')
        if position != -1:
            item=item[0:position]
        digit_postion=0
        for letter in item:
            digit_postion+=1
            if letter.isdigit():
                break
        nutrition_fact=item[0:digit_postion-2]
        id+=1
        nutrition_number=item[digit_postion-1:]
        cur.execute("INSERT INTO him_popcorn (id, popcorn_type , nutrition_fact , nutrition_number ) VALUES (?,?,?,?)",(id, popcorn_type , nutrition_fact , nutrition_number))
    conn.commit()

cur, conn = setUpDatabase('popcorn_database')
setUpdc_popcornTable(obj1, cur, conn)
setUpav_popcornTable(obj2, cur, conn)
setUpch_popcornTable(obj3, cur, conn)
setUphim_popcornTable(obj4, cur, conn)

dc_carb=cur.execute("SELECT nutrition_number FROM dc_popcorn WHERE nutrition_fact= 'Total Cabohydrate'")
print(dc_carb)

