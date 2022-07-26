import allure
import pytest
from selenium import webdriver

from pages.page_admin.admin_page_locators import AdminPageLocators
from pages.page_main.main_page import MainPage


@allure.parent_suite("Главная страница")
@allure.suite("Проверки главной страницы")
@allure.title("Проверка ошибки при отсутствии элемента на странице")
@pytest.mark.usefixtures("open_opencart")
def test_error(driver: webdriver):
    main = MainPage(driver)

    with allure.step("Проверить, что элемент присутствует на странице"):
        main.click(AdminPageLocators.WORLD_MAP_TITLE)
