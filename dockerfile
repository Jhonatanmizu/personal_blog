FROM python:3.11-alpine3.20

# Set maintainer label (metadata)
LABEL maintainer="natanjesuss20@gmail.com"

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Ensure Python output is sent straight to terminal
ENV PYTHONUNBUFFERED=1
# Set PATH to include virtual environment
ENV PATH="/venv/bin:$PATH"

# Install system dependencies required for Python packages
RUN apk update && \
    apk add --no-cache \
        bash \
        postgresql-dev \
        gcc \
        python3-dev \
        musl-dev \
        libffi-dev && \
    rm -rf /var/cache/apk/*

# Create directories and set permissions
RUN mkdir -p /app && \
    mkdir -p /data/web/static && \
    mkdir -p /data/web/media && \
    mkdir -p /scripts

# Copy application code
COPY ./src /app
COPY ./scripts /scripts

# Set working directory
WORKDIR /app

# Create and activate virtual environment, install dependencies
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt && \
    chmod -R +x /scripts

# Create non-root user and set ownership
RUN adduser --disabled-password --no-create-home duser && \
    chown -R duser:duser /venv && \
    chown -R duser:duser /data/web && \
    chown -R duser:duser /app && \
    chmod -R 755 /data/web && \
    chmod -R +x /scripts

# Add venv and scripts

ENV PATH="/scripts:/venv/bind:${PATH}"

# # Switch to non-root user
# USER duser

# Expose port 8000 for Django
EXPOSE 8000

ENTRYPOINT ["/scripts/commands.sh"]