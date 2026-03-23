UMT Python Web — Домашнє завдання №3
Опис

Цей проєкт є простим веб-додатком, створеним у межах курсу FullStack Web Development on Python.

Додаток демонструє:

маршрутизацію між сторінками
обробку HTML-форми (POST-запити)
збереження даних у JSON-файл
використання шаблонів Jinja2
роботу зі статичними ресурсами (CSS, зображення)
обробку помилки 404
Функціональність

Основні сторінки:
/ — головна сторінка
/message — сторінка з формою

Обробка повідомлень:
користувач вводить username та message
дані зберігаються у storage/data.json
кожне повідомлення має унікальний timestamp

Сторінка /read:
реалізована за допомогою Jinja2
відображає всі збережені повідомлення

Статичні файли:
style.css
logo.png

Сторінка помилки:
error.html (для 404 Not Found)

Використані технології:
Python 3
Flask
Jinja2
HTML / CSS / Bootstrap
JSON (для збереження даних)
uv (менеджер залежностей)

Структура проєкту
UMT-pythonweb-hw-03/
├── app.py
├── pyproject.toml
├── uv.lock
├── templates/
│   ├── index.html
│   ├── message.html
│   ├── read.html
│   └── error.html
├── static/
│   ├── style.css
│   └── logo.png
└── storage/
    └── data.json

Встановлення та запуск
1. Клонування репозиторію
git clone https://github.com/your-username/UMT-pythonweb-hw-03.git
2. Встановлення залежностей (через uv)
uv sync
3. Запуск застосунку
uv run python app.py
4. Відкрити у браузері
http://127.0.0.1:3000

Робота застосунку:
Flask обробляє HTTP-запити та маршрути
Дані з форми передаються через POST-запит
Дані перетворюються у словник Python
Повідомлення зберігаються у JSON-файл з часовою міткою
Jinja2 використовується для відображення даних на сторінці /read

Docker (додатково)
Збірка образу:
docker build -t umt-hw3 .
Запуск контейнера:
docker run -p 3000:3000 -v ./storage:/app/storage umt-hw3

Дані зберігаються поза контейнером завдяки volume


Автор:
Салтиков Андрій
