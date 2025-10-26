from playwright.sync_api import Page
from allure import step

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 30000
    @step("Открытие страницы: {url}")
    def open(self, url: str):
        self.page.goto(url)

    def get_current_url(self) -> str:
        return self.page.url

    @step("Ожидание URL содержащего: {expected_url}")
    def wait_for_url(self, expected_url, timeout: int = 1000):
        self.page.wait_for_url(expected_url, timeout=timeout)