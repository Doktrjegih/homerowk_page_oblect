import pytest
from selenium import webdriver

from pages.navigation.navigation import Navigation
from pages.navigation.navigation_locators import Pages
from pages.page_register.register_page import RegisterPage
from pages.page_register.register_page_locators import RegisterPageLocators


@pytest.mark.usefixtures("open_opencart")
def test_find_elements(driver: webdriver):
    register = RegisterPage(driver)
    navigation = Navigation(driver)

    navigation.goto_page(Pages.REGISTER)
    assert register.is_element_present(RegisterPageLocators.RIGHT_MENU)
    assert register.is_element_present(RegisterPageLocators.FIRSTNAME_FIELD)
    assert register.is_element_present(RegisterPageLocators.PASSWORD_FIELD)
    assert register.is_element_present(RegisterPageLocators.SUBMIT_BUTTON)
    assert register.is_element_present(RegisterPageLocators.POLICY_AGREE_CHECKBOX)
