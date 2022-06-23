import time

from selenium import webdriver

from pages.base_page import BasePage
from pages.navigation.navigation_locators import NavigationLocators


class Navigation(BasePage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self._driver = driver

    def goto_page(self, page_name):
        if page_name == "Components":
            self.click(NavigationLocators.COMPONENTS_MENU)
            self.click(NavigationLocators.ALL_COMPONENTS)
            time.sleep(3)
        if page_name == "Monitors":
            self.click(NavigationLocators.COMPONENTS_MENU)
            self.click(NavigationLocators.MONITORS)
            time.sleep(3)
        if page_name == "Register":
            self.click(NavigationLocators.MY_ACCOUNT)
            self.click(NavigationLocators.REGISTER)
            time.sleep(3)
