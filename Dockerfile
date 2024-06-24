FROM python:3.11-slim

LABEL org.opencontainers.image.source https://github.com/AmulyaParitosh/ResumeGenerator
LABEL org.opencontainers.image.description "ResumeGenerator is an API that generates a resume in pdf format using the data provided in a json file."
LABEL org.opencontainers.image.licenses=MIT

RUN pip install poetry==1.3.2

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY resumegenerator-6a627-firebase-adminsdk-62uz7-77d8182b2e.json ./
COPY .env ./
RUN touch README.md

RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

COPY ResumeGenerator/src ./ResumeGenerator/src
COPY ResumeGenerator/__init__.py ./ResumeGenerator/__init__.py

RUN poetry install --without dev

CMD ["poetry", "run", "uvicorn", "ResumeGenerator:app", "--host", "0.0.0.0", "--port", "80"]
