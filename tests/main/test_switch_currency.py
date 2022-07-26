import allure
import pytest
from selenium import webdriver

from pages.page_main.main_page import MainPage


@allure.parent_suite("Главная страница")
@allure.suite("Проверки главной страницы")
@allure.title("Проверка переключения между валютами")
@pytest.mark.usefixtures("open_opencart")
def test_switch_currency(driver: webdriver):
    main = MainPage(driver)

    main.switch_currency("EUR")
    main.switch_currency("USD")
    main.switch_currency("GBP")
