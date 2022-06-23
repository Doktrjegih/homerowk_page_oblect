import time
from typing import List

import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self._driver = driver

    def open(self, ip: str) -> None:
        self._driver.get(ip)

    def is_element_present(self, locator: str, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self._driver, timeout=timeout).until(
                EC.visibility_of_element_located((By.XPATH, locator))
            )
        except TimeoutException:
            return False
        return True

    def find_elements(self, locator: str, timeout: int = 5) -> List:
        try:
            return WebDriverWait(self._driver, timeout=timeout).until(
                EC.visibility_of_any_elements_located((By.XPATH, locator))
            )
        except TimeoutException:
            return []

    def find_element(self, locator: str, timeout: int = 5) -> WebElement:
        try:
            element = WebDriverWait(self._driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, locator))
            )
        except TimeoutException:
            pytest.fail(f"Элемент {locator} не появился за {timeout} секунд")
        return element

    def click(self, locator: str, timeout: int = 5, delay: float = 0.1) -> None:
        element = self.find_element(locator=locator, timeout=timeout)
        time.sleep(delay)
        try:
            element.click()
        except ElementClickInterceptedException:
            pytest.fail(f"Элемент {locator} перекрыт другим элементом")

    def input_text(
        self, locator: str, text: str, timeout: int = 5, delay: float = 0.1
    ) -> None:
        element = self.find_element(locator=locator, timeout=timeout)
        time.sleep(delay)
        element.send_keys(text)

    def accept_alert(self):
        self._driver.switch_to.alert.accept()
