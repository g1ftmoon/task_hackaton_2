from cgitb import html
from operator import delitem
import re
import requests
from bs4 import BeautifulSoup as BS

import csv

URL = ''
def get_html(url):
    response = requests.get(url)
    return response.text
    

def get_data(html):
    soup = BS(html, 'lxml')
    catalog = soup.find('div',class_='search-results-table')
    # phones = catalog.find_all('div', class_='product_text pull-left')
    # image = catalog.find('div', class_='listbox_img pull-left').find('img')
    for phone in catalog:
        try:
            title = soup.find('div', class_='listbox_title oh').find('a').text.strip()
        except:
            title = ''
        try:
            price = phone.find('div', class_='listbox_price text-center').text.strip()
        except:
            price = ''
        try:
            img = phone.find('div', class_ ='listbox_img pull-left').find('img').get('src')
        except:
            img = ''
 
        data = {
            'title': title,
            'price': price,
            'img': img
        }
        write_csv(data)

def write_csv(data):
    with open('phone.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='/')

        writer.writerow(
            (
                data['title'],
                data['price'],
                data['img']
            )
        )

def main():
    page = 0
    while page<32:
        print(f'Парсинг {page + 1}  страницы...')
        if page ==0:
            url = 'https://www.kivano.kg/mobilnye-telefony'
        else:
            url = f'https://www.kivano.kg/mobilnye-telefony?page={page}'
        html = get_html(url)
        get_data(html)
        page+= 1
        
main()

