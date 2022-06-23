import random
import string

import pytest
from selenium import webdriver

from pages.page_admin.admin_page import AdminPage
from tests.conftest import AuthData


@pytest.mark.usefixtures("open_opencart")
def test_add_delete_item(driver: webdriver, auth_data: AuthData):
    admin = AdminPage(driver)
    admin.open_page(auth_data.ip)

    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for _ in range(10))

    admin.login()
    admin.goto_products()
    admin.create_item(name=rand_string, tag="tag", model="model_name")
