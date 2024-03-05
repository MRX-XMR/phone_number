import re

# Открываем файл с HTML страницей
with open('full_page.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Регулярное выражение для поиска номеров телефонов
# phone_pattern = re.compile(r'(\+\d{1,2}\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})')
phone_pattern = re.compile(r'8\s\(\d{3}\)\s\d{3}-\d{2}-\d{2}')

# Ищем все номера телефонов на странице
phone_numbers = phone_pattern.findall(html_content)

# Выводим найденные номера телефонов
print('Найденные номера телефонов:')
for phone_number in phone_numbers:
    print(phone_number)

