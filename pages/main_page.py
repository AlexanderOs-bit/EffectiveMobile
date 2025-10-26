from pages.base_page import BasePage
from playwright.sync_api import Page
from allure import step

class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.main_link = "div[data-elem-id='1680606406475'] a[href='#main']"
        self.about_us_link = "a.tn-atom[href*='#about']"
        self.more_info_link = "//a[contains(@class, 'tn-atom') and contains(@href, '#moreinfo') and contains(text(), 'Услуги')]"
        self.projects_link = "a.tn-atom[href*='#cases']"
        self.reviews_link = "a.tn-atom[href*='#Reviews']"
        self.contacts_link = "//a[contains(@class, 'tn-atom') and contains(@href, '#contacts') and contains(text(), 'Контакты')]"
        self.specialists_link = "a.tn-atom[href*='#specialists']"

    @step("Переход на главную страницу")
    def click_main(self):
        self.page.click(self.main_link)

    @step("Переход в раздел 'О нас'")
    def click_about(self):
        self.page.click(self.about_us_link)

    @step("Переход в раздел 'Услуги'")
    def click_more(self):
        self.page.click(self.more_info_link)

    @step("Переход в раздел 'Проекты'")
    def click_projects(self):
        self.page.click(self.projects_link)

    @step("Переход в раздел 'Отзывы'")
    def click_reviews(self):
        self.page.click(self.reviews_link)

    @step("Переход в раздел 'Контакты'")
    def click_contacts(self):
        self.page.click(self.contacts_link)

    @step("Переход в раздел 'Выбрать специалиста'")
    def click_specialists(self):
        self.page.click(self.specialists_link)



