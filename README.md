# Tooba DRF Backend

Backend для проекта **Tooba**, написан на Django REST Framework.

## 🚀 Локальный запуск

### Клонирование репозитория
```bash
git clone https://github.com/abdulshamilov/tooba-drf.git
cd tooba-drf
python -m venv venv
# Активация окружения
# Windows:
venv\Scripts\activate
# Linux / MacOS:
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Основные зависимости

Django

Django REST Framework

djangorestframework-simplejwt (JWT авторизация)

drf-yasg (Swagger / Redoc документация)

Полный список зависимостей находится в requirements.txt

Документация API

После запуска локально документация доступна:

Swagger UI → http://127.0.0.1:8000/api/schema/swagger-ui/

Redoc → http://127.0.0.1:8000/api/schema/redoc/
