FROM python:3.8

ENV APP_PATH=/code \
    POETRY_VIRTUALENVS_IN_PROJECT=true

RUN pip install poetry

WORKDIR $APP_PATH

COPY ./app/ ./app
COPY ./pyproject.toml ./poetry.lock ./docker-entrypoint.sh .
RUN chmod +x ./docker-entrypoint.sh && poetry install

EXPOSE 80

ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["python", "./app/main.py"]

