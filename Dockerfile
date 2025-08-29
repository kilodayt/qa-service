FROM python:3.12-slim
WORKDIR /app

ENV PYTHONPATH=/app

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml /app/
RUN pip install --upgrade pip && pip install -e .

COPY alembic.ini /app/
COPY app /app/app

ENV ALEMBIC_CONFIG=/app/alembic.ini

# сначала применяем миграции, потом запускаем приложение
CMD alembic -c /app/alembic.ini upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000
