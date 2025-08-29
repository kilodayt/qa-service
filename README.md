# QA Service (FastAPI + Postgres)

Сервис вопросов и ответов.

## Стек

    - FastAPI, Pydantic v2
    - SQLAlchemy 2.0, Alembic
    - PostgreSQL
    - Docker & docker-compose
    - pytest

## Запуск

    1. Скопируйте `.env.example` в `.env` и при необходимости измените `DATABASE_URL`.
    2. Поднимите сервис
      docker-compose up -d --build
    3. Приложение: http://localhost:8000
    4. Документация Swagger: http://localhost:8000/docs
    Alembic миграции применяются автоматически при старте контейнера.

## Методы API

    1. Вопросы

    GET /questions/ — список всех вопросов
    POST /questions/ — создать вопрос { "text": "..." }
    GET /questions/{id} — вопрос + ответы
    DELETE /questions/{id} — удалить вопрос (каскадно удаляет ответы)

    2. Ответы

    POST /questions/{id}/answers/ — добавить ответ { "user_id": "uuid", "text": "..." }
    GET /answers/{id} — получить ответ
    DELETE /answers/{id} — удалить ответ

## Тесты

    pip install -e .[dev]
    pytest

## Валидация и логика

    Пустые text и user_id запрещены (валидация Pydantic).
    Ответ к несуществующему вопросу запрещён (HTTP 400).
    Один пользователь может оставлять несколько ответов на один вопрос.
    При удалении вопроса его ответы удаляются каскадно (FK ondelete=CASCADE + relationship(cascade="all, delete-orphan")).