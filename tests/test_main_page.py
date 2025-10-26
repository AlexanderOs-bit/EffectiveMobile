import pytest
import allure
from pages.main_page import MainPage

@allure.epic("Effective Mobile Website")
@allure.feature("Навигация по главной странице")
class TestMainPage:
    @allure.story("Основная навигация")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("""
    Проверка перехода на главную страницу.
    Ожидаемый результат: переход на #main
    """)
    def test_main_page_navigation(self, page):
        main_page = MainPage(page)
        with allure.step("Открыть главную страницу"):
            main_page.open("https://effective-mobile.ru/")
        with allure.step("Кликнуть на локатор с названием сайта"):
            main_page.click_main()
        main_page.wait_for_url("https://effective-mobile.ru/#main")
        with allure.step("Проверить URL"):
            assert "main" in main_page.get_current_url().lower()

    @pytest.mark.parametrize("section,expected_hash", [
        ("about", "#about"),
        ("more", "#moreinfo"),
        ("projects", "#cases"),
        ("reviews", "#Reviews"),
        ("contacts", "#contacts"),
        ("specialists", "#specialists")
    ])
    @allure.story("Навигация по разделам")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка перехода по основным блокам.")
    def test_all_sections_navigation(self, page, section, expected_hash):
        main_page = MainPage(page)
        with allure.step(f"Тестирование раздела: {section}"):
            main_page.open("https://effective-mobile.ru/")
            getattr(main_page, f"click_{section}")()
            current_url = main_page.get_current_url()
            assert expected_hash in current_url, f"Expected {expected_hash} in {current_url}"


