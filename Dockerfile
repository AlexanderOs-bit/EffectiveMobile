FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

RUN pip install playwright && playwright install-deps

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN playwright install chromium

COPY . .

CMD ["pytest", "tests/", "--alluredir=allure-results"]