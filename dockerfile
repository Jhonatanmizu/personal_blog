# -------- STAGE 1: Build Stage --------
FROM python:3.11-alpine3.20 AS builder

LABEL maintainer="natanjesuss20@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV VENV_PATH=/venv
ENV PATH="${VENV_PATH}/bin:$PATH"

# Install build dependencies
RUN apk add --no-cache \
    gcc \
    musl-dev \
    python3-dev \
    postgresql-dev \
    libffi-dev \
    bash

# Create virtual environment
RUN python -m venv ${VENV_PATH}

WORKDIR /app

# Copy requirements and install
COPY ./src/requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy full app code (used in collectstatic, etc.)
COPY ./src /app

# -------- STAGE 2: Final Stage --------
FROM python:3.11-alpine3.20

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV VENV_PATH=/venv
ENV PATH="${VENV_PATH}/bin:/scripts:$PATH"

# Install only runtime dependencies
RUN apk add --no-cache \
    bash \
    postgresql-libs

# Create necessary directories
RUN mkdir -p /app /data/web/static /data/web/media /scripts /venv

# Set working directory
WORKDIR /app

# Copy virtual environment from build stage
COPY --from=builder /venv /venv

# Copy app and scripts
COPY ./src /app/
COPY ./scripts  /scripts

# Ensure scripts are executable
RUN chmod -R +x /scripts

EXPOSE 8000

ENTRYPOINT ["commands.sh"]
