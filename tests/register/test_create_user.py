import random
import string

import pytest
from selenium import webdriver

from pages.navigation.navigation import Navigation
from pages.navigation.navigation_locators import Pages
from pages.page_register.register_page import RegisterPage


@pytest.mark.usefixtures("open_opencart")
def test_create_user(driver: webdriver):
    register = RegisterPage(driver)
    navigation = Navigation(driver)

    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for _ in range(10))

    navigation.goto_page(Pages.REGISTER)
    register.create_user(
        name="some_first_name",
        last_name="some_last_name",
        email=f"{rand_string}@some.com",
        tel="some_tel",
        password="password",
    )
