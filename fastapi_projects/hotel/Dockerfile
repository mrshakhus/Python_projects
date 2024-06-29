FROM python:3.12

RUN mkdir /booking

WORKDIR /booking

COPY pyproject.toml poetry.lock ./

RUN pip install poetry

RUN poetry install --no-root

RUN pip install gunicorn uvicorn sentry_sdk

COPY . .

CMD ["gunicorn", "app.main:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]
