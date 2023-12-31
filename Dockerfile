# Use a more specific base image
FROM python:3.11

ENV DEBIAN_FRONTEND noninteractive
ENV GECKODRIVER_VER v0.33.0 
ENV FIREFOX_VER 108.0 
ENV POETRY_VERSION=1.6.1 
ENV POETRY_HOME=/opt/poetry 
ENV POETRY_VENV=/opt/poetry-venv 
ENV POETRY_CACHE_DIR=/opt/.cache
ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

ENV PATH="${PATH}:${POETRY_VENV}/bin"

RUN set -x \
   && apt update \
   && apt upgrade -y

WORKDIR /app

COPY poetry.lock pyproject.toml ./

# Install Python dependencies using Poetry
RUN poetry install

# Install playwright dependencies
RUN poetry run playwright install firefox \
    && poetry run playwright install-deps firefox

COPY . /app

EXPOSE ${PORT}

CMD ["poetry", "run", "python", "main.py"]
