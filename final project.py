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
    for tag in nutrition_tags:
        nutrition_lst.append(tag.text.strip())  
    return nutrition_lst[1:26]


obj1=get_data_from_website('https://lesserevil.com/collections/organic-popcorn/products/avocado-licious-organic-popcorn?variant=28241948573789')
obj2=get_data_from_website('https://lesserevil.com/collections/organic-popcorn/products/avocado-licious-organic-popcorn?variant=28241948573789')
obj3=get_data_from_website('https://lesserevil.com/collections/organic-popcorn/products/classic-cheddah-organic-popcorn')
obj4=get_data_from_website('https://lesserevil.com/collections/organic-popcorn/products/himalayan-pink-salt-organic-popcorn')


def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def setUpPopcornTable(data, cur, conn):
    cur.execute("DROP TABLE IF EXISTS Popcorn")
    cur.execute("CREATE TABLE Popcorn (id INTEGER PRIMARY KEY, popcorn_type TEXT, nutrition_fact TEXT, nutrition_number REAL)")
    
    print(data)
    id=0
    for item in data:
        position=item.find('\n')
        if position ==-1:
            nutrition_fact=item
            nutrition_number=item
        else:
            nutrition_fact=item[0:position]
            nutrition_number=item[0:position]

        id+=1
        popcorn_type='avocado-licious'
            

       
       # cur.execute("INSERT INTO Popcorn (id, popcorn_type , nutrition_fact , nutrition_number ) VALUES (?,?,?,?)",(id, popcorn_type , nutrition_fact , nutrition_number))
   # conn.commit()
cur, conn = setUpDatabase('popcorn_database')
setUpPopcornTable(obj1, cur, conn)