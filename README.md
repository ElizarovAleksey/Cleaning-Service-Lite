# 🧼 Портал клининговых услуг «Мой Не Сам»

Веб-приложение на Django для оформления заявок на клининговые услуги.

---

## 🚀 Быстрый запуск

```bash
    git clone https://github.com/ElizarovAleksey/Cleaning-Service-Lite.git
    cd Clining-Service-Lite

    python -m venv venv
    source venv/bin/activate  # Linux
    # venv\Scripts\activate   # Windows

    pip install -r requirements.txt

    python manage.py migrate
    python manage.py loaddata initial_data

    python manage.py runserver
```
Открыть в браузере:

```bash
    http://127.0.0.1:8000/
```
👤 Тестовый администратор

    Логин: adminka
    Пароль: cleanservic

Админка доступна по адресу:
```bash
    http://127.0.0.1:8000/admin/
```
📦 Функционал

    Регистрация пользователей
    Авторизация
    Создание заявок
    Просмотр истории заявок
    Панель администратора
    Фильтрация и изменение статусов
    Отмена заявки с указанием причины
    Кастомизированная админка
    Адаптивный интерфейс
    Слайдер на главной странице