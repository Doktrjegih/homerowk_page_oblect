from dataclasses import dataclass

import pytest
from selenium import webdriver

from pages.base_page import BasePage


@dataclass
class AuthData:
    ip: str


@pytest.fixture
def auth_data(request):
    ip = request.config.getoption("url")
    return AuthData(ip=ip)


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--url", default="http://10.20.53.41:8081")


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        browser = webdriver.Firefox()
    elif browser_name == "opera":
        browser = webdriver.Opera()
    else:
        raise ValueError("Браузер передан неверно")

    browser.maximize_window()
    request.addfinalizer(browser.close)

    return browser


@pytest.fixture
def open_opencart(driver: webdriver, auth_data: AuthData):
    base = BasePage(driver)
    base.open(auth_data.ip)
