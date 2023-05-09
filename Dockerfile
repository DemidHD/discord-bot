# syntax=docker/dockerfile:1
FROM python:3.10-slim as python-base

# python settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# directory project
WORKDIR /srv

# installing dependencies
COPY requirements.txt /srv/
RUN pip install --upgrade pip
RUN pip install --upgrade --no-cache-dir -r requirements.txt

# Copy the entire project to the container.
COPY . /srv/