# 1.Ознакомиться с некоторые интересными API. https://docs.ozon.ru/api/seller/ https://developers.google.com/youtube/v3/getting-started https://spoonacular.com/food-api
# 2.Потренируйтесь делать запросы к API. Выберите публичный API, который вас интересует, и потренируйтесь делать API-запросы с помощью Postman. Поэкспериментируйте с различными типами запросов и попробуйте получить различные типы данных.
# 3.Сценарий Foursquare
# 4.Напишите сценарий на языке Python, который предложит пользователю ввести интересующую его категорию (например, кофейни, музеи, парки и т.д.).
# 5.Используйте API Foursquare для поиска заведений в указанной категории.
# 6.Получите название заведения, его адрес и рейтинг для каждого из них.
# 7.Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль

import requests

# Запрос информации о заведениях в определенной категории
def search_places(category):
    url = 'https://api.foursquare.com/v2/venues/search'
    params = {
        'client_id': 'YOUR_CLIENT_ID',
        'client_secret': 'YOUR_CLIENT_SECRET',
        'v': '20220101',
        'near': 'Moscow',
        'query': category,
        'limit': 10
    }

    response = requests.get(url, params=params).json()

    for venue in response['response']['venues']:
        venue_id = venue['id']
        venue_url = f'https://api.foursquare.com/v2/venues/{venue_id}'
        venue_params = {
            'client_id': 'YOUR_CLIENT_ID',
            'client_secret': 'YOUR_CLIENT_SECRET',
            'v': '20220101'
        }
        
        venue_info = requests.get(venue_url, params=venue_params).json()
        
        name = venue_info['response']['venue']['name']
        address = venue_info['response']['venue']['location']['address']
        rating = venue_info['response']['venue']['rating']
        
        print(f'Name: {name}')
        print(f'Address: {address}')
        print(f'Rating: {rating}')
        print('---')

# Ввод категории от пользователя
category = input('Введите категорию заведения: ')

# Запуск скрипта
search_places(category)
