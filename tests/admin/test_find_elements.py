import allure
import pytest
from selenium import webdriver

from pages.page_admin.admin_page import AdminPage
from pages.page_admin.admin_page_locators import AdminPageLocators
from tests.conftest import AuthData


@allure.parent_suite("Панель администратора")
@allure.suite("Проверки страницы администратора")
@allure.title("Проверка наличия элементов на странице")
@pytest.mark.usefixtures("open_opencart")
def test_find_elements(driver: webdriver, auth_data: AuthData):
    admin = AdminPage(driver)
    admin.open_page(auth_data.ip)

    with allure.step("Проверить наличие элементов на странице"):
        assert admin.is_element_present(AdminPageLocators.USERNAME_FIELD)
        assert admin.is_element_present(AdminPageLocators.PASSWORD_FIELD)
        assert admin.is_element_present(AdminPageLocators.SUBMIT_BUTTON)
        assert admin.is_element_present(AdminPageLocators.FORGET_PASSWORD)
        assert admin.is_element_present(AdminPageLocators.OPENCART_SITE)
