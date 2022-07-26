import allure
import pytest
from selenium import webdriver

from pages.page_main.main_page import MainPage
from pages.page_main.main_page_locators import MainPageLocators


@allure.parent_suite("Главная страница")
@allure.suite("Проверки главной страницы")
@allure.title("Проверка наличия элементов на странице")
@pytest.mark.usefixtures("open_opencart")
def test_find_elements(driver: webdriver):
    main = MainPage(driver)

    with allure.step("Проверить наличие элементов на странице"):
        assert main.is_element_present(MainPageLocators.LOGO)
        assert len(main.find_elements(MainPageLocators.SLIDESHOW_PICTURES)) == 2
        assert main.is_element_present(MainPageLocators.SEARCH_INPUT)
        assert main.is_element_present(MainPageLocators.SHOP_CART)
        assert main.is_element_present(MainPageLocators.NAVIGATION_BAR)
