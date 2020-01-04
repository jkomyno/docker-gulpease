FROM python:3.7-alpine as base

FROM base
COPY src /app
WORKDIR /app
CMD ["python", "gulpease.py", "/pdf", "/report"]
