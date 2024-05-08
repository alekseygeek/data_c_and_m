# Урок 4. Парсинг HTML. XPath
# Выберите веб-сайт с табличными данными, который вас интересует.
# Напишите код Python, использующий библиотеку requests для отправки HTTP GET-запроса на сайт и получения HTML-содержимого страницы.
# Выполните парсинг содержимого HTML с помощью библиотеки lxml, чтобы извлечь данные из таблицы.
# Сохраните извлеченные данные в CSV-файл с помощью модуля csv.
# 
# Ваш код должен включать следующее:
# 
# Строку агента пользователя в заголовке HTTP-запроса, чтобы имитировать веб-браузер и избежать блокировки сервером.
# Выражения XPath для выбора элементов данных таблицы и извлечения их содержимого.
# Обработка ошибок для случаев, когда данные не имеют ожидаемого формата.
# Комментарии для объяснения цели и логики кода.
# 
# Примечание: Пожалуйста, не забывайте соблюдать этические и юридические нормы при веб-скреппинге.


import requests
from lxml import html
import csv

# Установка URL-адреса веб-сайта и строки агента пользователя
url = 'https://www.w3schools.com/html/html_tables.asp'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Отправка HTTP GET-запроса
response = requests.get(url, headers=headers)
if response.status_code == 200:
    # Получение содержимого HTML
    tree = html.fromstring(response.content)

    # Использование XPath для извлечения данных из таблицы
    rows = tree.xpath('//table[@id="customers"]/tr')
    
    # Создание CSV-файла и запись данных из таблицы
    with open('table_data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in rows:
            data = [td.text_content().strip() for td in row.xpath('td')]
            writer.writerow(data)
    print('Данные успешно извлечены и сохранены в CSV-файл!')
else:
    print('Не удалось получить доступ к веб-сайту')
