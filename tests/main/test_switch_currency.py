import pytest
from selenium import webdriver

from pages.page_main.main_page import MainPage


@pytest.mark.usefixtures("open_opencart")
def test_switch_currency(driver: webdriver):
    main = MainPage(driver)

    main.switch_currency()
