# Foodgram - Продуктовый помощник

![example workflow](https://github.com/NIK-TIGER-BILL/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)  

## Стек технологий

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)

## Описание проекта
Foodgram - это социальная сеть для тех, кто не только любит вкусно покушать, но и научиться готовить самостоятельно.
Тут вы найдете множество оригинальных рецептов от разных пользователей, сможете подписываться на их творчество, добавлять лучшие рецепты в избранное, а также создавать список покупок и загружать его.

## Установка проекта 

* Склонировать репозиторий на локальную машину:
```bash
git clone https://github.com/Hlompy/foodgram-project-react.git
cd foodgram-project-react
```

* Cоздать и активировать виртуальное окружение:

```bash
python3 -m venv env
```

```bash
. venv/bin/activate
```

* Cоздайте файл `.env` в директории `/infra/` с содержанием:

```
SECRET_KEY=секретный ключ django
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

* Перейти в директирию и установить зависимости из файла requirements.txt:

```bash
cd backend/
pythom -m pip install -r requirements.txt
```

## Запуск проекта в Docker контейнере

* Запустите docker compose:
```bash
docker-compose up -d --build
```  

* Примените миграции:
```bash
docker-compose exec backend python manage.py migrate
```

* Загрузите ингредиенты:
```bash
docker-compose exec backend python manage.py importcsv
```

* Создайте администратора:
```bash
docker-compose exec backend python manage.py createsuperuser
```

* Соберите статику:
```bash
docker-compose exec backend python manage.py collectstatic --noinput
```

## Сайт
51.250.110.145
