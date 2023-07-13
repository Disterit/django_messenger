# Получить базовый образ
FROM python:3.11
# Установите переменные среды
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Установите рабочую директорию
WORKDIR /code
# Установите зависимости
COPY Pipfile Pipfile.lock requirements.txt /code/
RUN pip install pipenv && pipenv install --system
RUN pip install -r requirements.txt
# Копирование проекта
COPY . /code/
