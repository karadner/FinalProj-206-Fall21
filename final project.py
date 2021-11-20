from typing import List, Tuple
from bs4 import BeautifulSoup
import requests



def get_data_from_website(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    nutrition_tags = soup.find_all('div', class_='d-flex')
    nutrition_lst = []
    for tag in nutrition_tags:
        nutrition_lst.append(tag.text.strip())
    return nutrition_lst


obj=get_data_from_website('https://lesserevil.com/collections/organic-popcorn/products/avocado-licious-organic-popcorn?variant=28241948573789')
print(obj)

