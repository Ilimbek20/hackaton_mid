import requests
from bs4 import BeautifulSoup as BS
import csv

def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    soup = BS(html, 'lxml')
    return soup

def get_mot(soup):
    moto = soup.find('div', class_= 'table-view-list')
    moto2 = moto.find_all('div', class_='list-item')
    for mot in moto2:
        title = mot.find('h2', class_='name').text.strip()
        image = mot.find('img', class_='lazy-image').get('data-src')
        price = mot.find('p', class_='price').find('strong').get_text(strip=True)
        info = mot.find('p', class_='body-type').get_text(strip=True)
    
        write_csv({

            'title' : title,
            'image' : image,
            'price' : price,
            'info' : info
            
        })



def write_csv(data):
    with open('moto.csv', 'a') as file:
        names = ['title', 'image', 'price', 'info']
        write = csv.DictWriter(file, delimiter=',', fieldnames=names)
        write.writerow(data)

def main():
    url = 'https://www.mashina.kg/motosearch/all/'
    html = get_html(url)
    soup = get_soup(html)
    get_mot(soup)
main()   