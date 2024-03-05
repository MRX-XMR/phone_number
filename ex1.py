import requests

url = 'https://hands.ru/company/about/'  # URL страницы, которую нужно сохранить

# Отправляем GET-запрос к странице и получаем ее содержимое
response = requests.get(url)
html = response.text

# Создаем новый HTML файл и записываем в него содержимое страницы
with open('full_page1.html', 'w', encoding='utf-8') as file:
    file.write(html)

print('Страница успешно сохранена в файле "full_page1.html"')