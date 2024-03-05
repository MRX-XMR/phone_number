import re



# Открываем файл с HTML страницей
with open('full_page1.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Регулярное выражение для поиска номеров телефонов
phone_pattern = re.compile(r'(\+\d{1,2}\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})')


# Ищем все номера телефонов на странице
phone_numbers = phone_pattern.findall(html_content)

print('Найденные номера телефонов:')
for phone_number in phone_numbers:
    print(phone_number)
