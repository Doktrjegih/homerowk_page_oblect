import allure

from pages.base_page import BasePage
from pages.navigation.navigation_locators import NavigationLocators


class Navigation(BasePage):
    @allure.step("Перейти на страницу: {page_name}")
    def goto_page(self, page_name):
        if page_name == "Components":
            self.click(NavigationLocators.COMPONENTS_MENU)
            self.click(NavigationLocators.ALL_COMPONENTS)
        if page_name == "Monitors":
            self.click(NavigationLocators.COMPONENTS_MENU)
            self.click(NavigationLocators.MONITORS)
        if page_name == "Register":
            self.click(NavigationLocators.MY_ACCOUNT)
            self.click(NavigationLocators.REGISTER)
