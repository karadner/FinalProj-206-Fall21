from typing import List, Tuple
from bs4 import BeautifulSoup
import requests
import unittest
import sqlite3
import json
import os
import matplotlib
import matplotlib.pyplot as plt


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
    return nutrition_lst[0:14]


obj1=get_data_from_website('https://lesserevil.com/collections/organic-popcorn/products/dark-chocolate-himalayan-pink-salt')
obj2=get_data_from_website('https://lesserevil.com/collections/organic-popcorn/products/avocado-licious-organic-popcorn?variant=28241948573789')
obj3=get_data_from_website('https://lesserevil.com/collections/organic-popcorn/products/classic-cheddah-organic-popcorn')
obj4=get_data_from_website('https://lesserevil.com/collections/organic-popcorn/products/himalayan-pink-salt-organic-popcorn')
obj5=get_data_from_website('https://lesserevil.com/collections/organic-popcorn/products/himalayan-gold-organic-popcorn')
obj6=get_data_from_website('https://lesserevil.com/collections/organic-popcorn/products/himalayan-sweetness-organic-popcorn?variant=28201424355421')
obj7=get_data_from_website('https://lesserevil.com/collections/organic-popcorn/products/oh-my-ghee-organic-popcorn')
obj8=get_data_from_website('https://lesserevil.com/collections/organic-popcorn/products/white-chocolate-matcha')

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

def setUpgold_popcornTable(data, cur, conn):
    cur.execute("DROP TABLE IF EXISTS gold_popcorn")
    cur.execute("CREATE TABLE gold_popcorn (id INTEGER PRIMARY KEY, popcorn_type TEXT, nutrition_fact TEXT, nutrition_number TEXT)")
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
        cur.execute("INSERT INTO gold_popcorn (id, popcorn_type , nutrition_fact , nutrition_number ) VALUES (?,?,?,?)",(id, popcorn_type , nutrition_fact , nutrition_number))
    conn.commit()

def setUpsweet_popcornTable(data, cur, conn):
    cur.execute("DROP TABLE IF EXISTS sweet_popcorn")
    cur.execute("CREATE TABLE sweet_popcorn (id INTEGER PRIMARY KEY, popcorn_type TEXT, nutrition_fact TEXT, nutrition_number TEXT)")
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
        cur.execute("INSERT INTO sweet_popcorn (id, popcorn_type , nutrition_fact , nutrition_number ) VALUES (?,?,?,?)",(id, popcorn_type , nutrition_fact , nutrition_number))
    conn.commit()

def setUpoh_popcornTable(data, cur, conn):
    cur.execute("DROP TABLE IF EXISTS oh_popcorn")
    cur.execute("CREATE TABLE oh_popcorn (id INTEGER PRIMARY KEY, popcorn_type TEXT, nutrition_fact TEXT, nutrition_number TEXT)")
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
        cur.execute("INSERT INTO oh_popcorn (id, popcorn_type , nutrition_fact , nutrition_number ) VALUES (?,?,?,?)",(id, popcorn_type , nutrition_fact , nutrition_number))
    conn.commit()

def setUpwh_popcornTable(data, cur, conn):
    cur.execute("DROP TABLE IF EXISTS pink_popcorn")
    cur.execute("DROP TABLE IF EXISTS wh_popcorn")
    cur.execute("CREATE TABLE wh_popcorn (id INTEGER PRIMARY KEY, popcorn_type TEXT, nutrition_fact TEXT, nutrition_number TEXT)")
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
        cur.execute("INSERT INTO wh_popcorn (id, popcorn_type , nutrition_fact , nutrition_number ) VALUES (?,?,?,?)",(id, popcorn_type , nutrition_fact , nutrition_number))
    conn.commit()


cur, conn = setUpDatabase('popcorn_database')
setUpdc_popcornTable(obj1, cur, conn)
setUpav_popcornTable(obj2, cur, conn)
setUpch_popcornTable(obj3, cur, conn)
setUphim_popcornTable(obj4, cur, conn)
setUpgold_popcornTable(obj5, cur,conn)
setUpsweet_popcornTable(obj6, cur, conn)
setUpoh_popcornTable(obj7,cur, conn)
setUpwh_popcornTable(obj8, cur, conn)

def popcorn_join(fact, cur, conn):
    new_lst=[]
    cur.execute("SELECT dc_popcorn.nutrition_number, him_popcorn.nutrition_number,av_popcorn.nutrition_number, ch_popcorn.nutrition_number, gold_popcorn.nutrition_number, sweet_popcorn.nutrition_number, oh_popcorn.nutrition_number, wh_popcorn.nutrition_number FROM dc_popcorn JOIN him_popcorn ON dc_popcorn.nutrition_fact = him_popcorn.nutrition_fact JOIN av_popcorn ON dc_popcorn.nutrition_fact=av_popcorn.nutrition_fact JOIN ch_popcorn ON dc_popcorn.nutrition_fact=ch_popcorn.nutrition_fact JOIN gold_popcorn ON dc_popcorn.nutrition_fact=gold_popcorn.nutrition_fact JOIN sweet_popcorn ON dc_popcorn.nutrition_fact=sweet_popcorn.nutrition_fact JOIN oh_popcorn ON dc_popcorn.nutrition_fact=oh_popcorn.nutrition_fact JOIN wh_popcorn ON dc_popcorn.nutrition_fact=wh_popcorn.nutrition_fact WHERE dc_popcorn.nutrition_fact=?", (fact, ))
    facts=cur.fetchall()
    for facttt in facts:
        new_lst.append(facttt)
    sum=0
    count=0
    for item in new_lst:
        for num in item:
            if num[-2:]=='mg':
                units='mg'
                num=float(num[:-2])
            else:
                units='g'
                num=float(num[:-1])
            sum+=num
            count+=1
    average=sum/count
    return [fact, average, units]

carbs=popcorn_join('Total Carbohydrate', cur,conn)
sodium=popcorn_join('Sodium', cur, conn)
calcium=popcorn_join('Calcium', cur, conn)
chol=popcorn_join('Cholesterol', cur, conn)
fib=popcorn_join('Dietary Fiber', cur, conn)
potassium=popcorn_join('Potassium', cur, conn)
fat=popcorn_join('Saturated Fat', cur, conn)
protein=popcorn_join('Protein', cur, conn)


calc=carbs, sodium, calcium, chol, fib, potassium, fat, protein

final_list=[]
final_list.append(calc)



with open('nutrition.txt', 'w') as f:
    for middle_list in final_list:
        for sub_list in middle_list:
            f.writelines('The average ' + str(sub_list[0]) + ' count is ' + str(sub_list[1]) + sub_list[2])
            f.write('\n')
f.close()



fig=plt.figure(figsize=(15,5))
matplotlib.rc('xtick', labelsize=9) 
matplotlib.rc('ytick', labelsize=9)
names=['Sodium (mg)','Potassium (mg)', 'Total Carbohydrate (g)', 'Calcium (mg)', 'Dietary Fiber (g)', 'Saturated Fat (g)', 'Protein (g)', 'Cholesterol (mg)']
averages=[sodium[1], potassium[1], carbs[1], calcium[1], fib[1], fat[1], protein[1], chol[1]]
positions=[0,1,2,3,4,5,6,7]
plt.bar(names, averages, color=['mediumblue', 'slateblue', 'blueviolet', 'mediumorchid', 'violet', 'hotpink', 'lightpink', 'coral'], edgecolor='black')
plt.xlabel('Nutrition Fact', fontweight='bold')
plt.ylabel('Averages', fontweight='bold')
plt.title('Average Nutrition Facts of LesserEvil Popcorn')
for i, v in enumerate(averages):
    plt.text(i, v+1, str(v), 
            color = 'dodgerblue', fontweight = 'bold', ha='center')
plt.show()






