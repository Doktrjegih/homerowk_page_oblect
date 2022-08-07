import datetime
import logging
from dataclasses import dataclass

import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.opera.options import Options

from pages.base_page import BasePage


@dataclass
class AuthData:
    ip: str


@pytest.fixture
def auth_data(request):
    ip = request.config.getoption("url")
    return AuthData(ip=f"http://{ip}")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--bv", action="store")
    parser.addoption("--executor", action="store", default="192.168.0.110:4444")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--url", action="store", default="192.168.0.110:8081")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--videos", action="store_true")
    parser.addoption("--mobile", action="store_true")  # only for chrome
    parser.addoption("--headless", action="store_true", default=False)


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    browser_version = request.config.getoption("--bv")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    videos = request.config.getoption("--videos")
    mobile = request.config.getoption("--mobile")
    headless = request.config.getoption("--headless")
    executor_ip = request.config.getoption("--executor")

    logger = logging.getLogger(request.node.name)

    logger.addHandler(logging.FileHandler(f"logs/{request.node.name}.log"))
    logger.setLevel(level=log_level)

    logger.info(
        f"=== Test {request.node.name} started at {datetime.datetime.now()} ==="
    )

    if executor != "local":
        caps = {
            "browserName": browser_name,
            "browserVersion": browser_version,
            "selenoid:options": {"enableVNC": vnc, "enableVideo": videos},
            "goog:chromeOptions": {},
        }

        if mobile:
            caps["goog:chromeOptions"]["mobileEmulation"] = {
                "deviceName": "iPhone 5/SE"
            }

        options = Options()
        if browser_name == "opera":
            options.add_experimental_option("w3c", True)

        browser = webdriver.Remote(
            command_executor=f"http://{executor_ip}/wd/hub",
            desired_capabilities=caps,
            options=options,
        )
    else:
        if browser_name == "chrome":
            options = ChromeOptions()
            if headless:
                options.headless = headless
            browser = webdriver.Chrome()
        elif browser_name == "firefox":
            browser = webdriver.Firefox()
        elif browser_name == "opera":
            browser = webdriver.Opera()
        else:
            raise ValueError("Браузер передан неверно")

    browser.log_level = log_level
    browser.logger = logger

    logger.info(f"Browser: {browser}")

    browser.maximize_window()

    def final():
        browser.quit()
        logger.info(
            f"=== Test {request.node.name} finished at {datetime.datetime.now()} ==="
        )

    request.addfinalizer(final)
    return browser


@pytest.fixture
def open_opencart(driver: webdriver, auth_data: AuthData):
    base = BasePage(driver)
    base.open(auth_data.ip)
