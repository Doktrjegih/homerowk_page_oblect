import time
from typing import List

import allure
import pytest
from selenium.common.exceptions import (ElementClickInterceptedException,
                                        TimeoutException)
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver) -> None:
        self._driver = driver
        self.logger = driver.logger

    @allure.step("Открыть url {ip}")
    def open(self, ip: str) -> None:
        self.logger.info("Открыть url {ip}")
        self._driver.get(ip)

    @allure.step("Проверить, есть ли элемент: {locator}")
    def is_element_present(self, locator: str, timeout: int = 5) -> bool:
        self.logger.info(f"Проверить, есть ли элемент: {locator}")
        try:
            WebDriverWait(self._driver, timeout=timeout).until(
                EC.visibility_of_element_located((By.XPATH, locator))
            )
        except TimeoutException:
            return False
        return True

    @allure.step("Найти элементы: {locator}")
    def find_elements(self, locator: str, timeout: int = 5) -> List:
        self.logger.info(f"Найти элементы: {locator}")
        try:
            return WebDriverWait(self._driver, timeout=timeout).until(
                EC.visibility_of_any_elements_located((By.XPATH, locator))
            )
        except TimeoutException:
            return []

    @allure.step("Найти элемент: {locator}")
    def find_element(self, locator: str, timeout: int = 5) -> WebElement:
        self.logger.info(f"Найти элемент: {locator}")
        try:
            element = WebDriverWait(self._driver, timeout).until(
                EC.visibility_of_element_located((By.XPATH, locator))
            )
        except TimeoutException:
            self.fail(f"Элемент {locator} не появился за {timeout} секунд")
        return element

    @allure.step("Нажать на элемент: {locator}")
    def click(self, locator: str, timeout: int = 5, delay: float = 0.1) -> None:
        self.logger.info(f"Нажать на элемент: {locator}")
        element = self.find_element(locator=locator, timeout=timeout)
        time.sleep(delay)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.fail(f"Элемент {locator} перекрыт другим элементом")

    @allure.step("Ввести текст '{text}' в элемент: {locator}")
    def input_text(
        self, locator: str, text: str, timeout: int = 5, delay: float = 0.1
    ) -> None:
        self.logger.info(f'Ввести текст "{text}" в элемент: {locator}')
        element = self.find_element(locator=locator, timeout=timeout)
        time.sleep(delay)
        element.send_keys(text)

    @allure.step("Принять алерт браузера")
    def accept_alert(self):
        self.logger.info("Принять алерт браузера")
        self._driver.switch_to.alert.accept()

    def attach_screenshot_to_report(self) -> None:
        allure.attach(
            name=self._driver.session_id,
            body=self._driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG,
        )

    def fail(self, error_text: str) -> None:
        self.attach_screenshot_to_report()
        pytest.fail(error_text)
