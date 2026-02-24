# 🧼 Портал клининговых услуг «Мой Не Сам»

Веб-приложение на Django для оформления заявок на клининговые услуги.

## 🚀 Быстрый запуск

```bash
git clone https://github.com/ElizarovAleksey/Clining-Service-Lite.git
cd Project

python -m venv venv
source venv/bin/activate  # Linux
# venv\Scripts\activate   # Windows

pip install -r requirements.txt

python manage.py makemigrations   # если нужно
python manage.py migrate
python manage.py loaddata initial_data

python manage.py createsuperuser # если нужно

python manage.py runserver

👤 Тестовый администратор

    Логин: adminka
    Пароль: cleanservic

📦 Функционал

    Регистрация пользователей
    Авторизация
    Создание заявок
    История заявок
    Панель администратора
    Фильтрация и изменение статусов
    Кастомизированная админка
    Адаптивный интерфейс