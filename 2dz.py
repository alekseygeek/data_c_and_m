# Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/ и извлечь информацию о всех книгах на сайте во всех категориях:
# название, цену, количество товара в наличии (In stock (19 available)) в формате integer, описание.

# Затем сохранить эту информацию в JSON-файле.


import requests
from bs4 import BeautifulSoup
import json

url = 'http://books.toscrape.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

books_info = []

for num, book in enumerate(soup.find_all('article', class_='product_pod')):
    print('Обработка книги', num)
    href = book.h3.a['href']
    resp = requests.get(url + href)
    page = BeautifulSoup(resp.text, 'html.parser')
    article = page.find('article', {'class': 'product_page'})
    info = article.find('div', {'class': 'product_main'})
    title = info.h1.text
    price_text = page.find('p', class_='price_color').text.split('£')
    price = round(float(price_text[1]), 2) if len(price_text) == 2 else 0
    stock = int(page.find('p', class_='instock availability').text.split('(')[1].split()[0])
    description = page.find('div', {'id': 'product_description'}).find_next_sibling('p').text

    book_info = {
        'title': title,
        'price': price,
        'stock': stock,
        'description': description
    }

    books_info.append(book_info)

with open('books_info.json', 'w') as file:
    json.dump(books_info, file, indent=4)

print('Данные были обработаны и сохранены в файле books_info.json')
