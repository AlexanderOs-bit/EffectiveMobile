# Effective Mobile UI Tests

## О проекте

Этот проект содержит UI-тесты для проверки навигации по разделам главной страницы https://effective-mobile.ru.
Тесты проверяют корректность переходов по всем основным блокам сайта.

## Локальный запуск

### 1. Клонировать репозиторий
```bash
git clone https://github.com/AlexanderOs-bit/EffectiveMobile
cd EffectiveMobile
```
### 2. Установить зависимости
```bash
pip install -r requirements.txt
```
### 3. Установить браузеры Playwright
```bash
playwright install
```
### 4. Запустить тесты
```bash   
pytest
```
### 4.1 Запустить тесты с генерацией Allure отчётов
```bash
pytest --alluredir=allure-results
```
### 5. Просмотр отчётов Allure
```bash
allure serve allure-results
```
## Запуск в Docker

### 1. Собрать Docker образ
```bash
docker build -t effective-mobile-tests .
```
### 2. Запустить тесты в контейнере
```bash
docker run effective-mobile-tests
```
### 2.1 Запустить тесты с сохранением отчётов
```bash
docker run -v $(pwd)/allure-results:/app/allure-results effective-mobile-tests
```
### 3. Просмотреть отчёт после запуска в Docker
```bash
allure serve allure-results
```
## Очистка отчётов
```bash
rm -rf allure-results
```
