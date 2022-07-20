import logging
import random
import string

import allure
import pytest
from selenium import webdriver

from pages.page_admin.admin_page import AdminPage
from tests.conftest import AuthData

logging.basicConfig(level=logging.DEBUG)


@allure.parent_suite("Панель администратора")
@allure.suite("Проверки страницы администратора")
@allure.title("Проверка создания и удаления товара в базе")
@pytest.mark.usefixtures("open_opencart")
def test_add_delete_item(driver: webdriver, auth_data: AuthData):
    admin = AdminPage(driver)
    admin.open_page(auth_data.ip)

    letters = string.ascii_lowercase
    rand_string = "".join(random.choice(letters) for _ in range(10))

    admin.login()
    admin.goto_products()
    admin.create_item(name=rand_string, tag="tag", model="model_name")
