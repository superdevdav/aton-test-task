# Используемые технологии
1. Backend: Python (FastAPI, SQLAlchemy, Jinja2)
2. Frontend: HTML, CSS, JS
3. Database: sqlite
## Про структуру проекта
1. src: находятся файлы .py и product.db
2. static: находятся папки css, img, js
3. templates: находятся шаблоны html
## Подробнее про src
1. main.py - запуск сервера
2. router.py - описаны маршруты
3. database.py - подключение к базе данных и создание сессии бд
4. models.py - модели, описывающие таблицы в бд
5. CustomerRepository и UserRepository - репозитории с одноименными классами и методами. Там же и методы для создания синтетических данных пользователей и клиентов.
6. utils.py - там должны находиться вспомогательные функции (там только hash_password() функция)
## Зависимости
Необходимые для установки зависимости находятся в requirements.txt
