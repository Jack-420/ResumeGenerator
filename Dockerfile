FROM python:3.11-slim

LABEL key=org.opencontainers.image.source value="https://github.com/AmulyaParitosh/ResumeGenerator"
LABEL key=org.opencontainers.image.description value="ResumeGenerator is an API that generates a resume in pdf format using the data provided in a json file."
LABEL key=org.opencontainers.image.licenses value="MIT"

# RUN apt-get update && apt=get install texlive-full
RUN apt-get -y update
RUN apt-get -y install --fix-missing sudo texlive-full
RUN rm -rf /var/lib/apt/lists/*

RUN pip install poetry==1.3.2


ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./
COPY resumegenerator-6a627-firebase-adminsdk-62uz7-182c9cb744.json ./
COPY .env ./
RUN touch README.md

RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

COPY ResumeGenerator/src ./ResumeGenerator/src
COPY ResumeGenerator/__init__.py ./ResumeGenerator/__init__.py

RUN poetry install --without dev

CMD ["poetry", "run", "uvicorn", "ResumeGenerator:app", "--host", "0.0.0.0", "--port", "80"]
