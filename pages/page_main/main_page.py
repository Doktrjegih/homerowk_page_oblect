import allure

from pages.base_page import BasePage
from pages.page_main.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step("Переключить валюту на {currency}")
    def switch_currency(self, currency: str):
        if currency.upper() not in ["EUR", "USD", "GBP"]:
            self.fail('Валюта может быть только "EUR", "USD" или "GBP"')
        self.click(MainPageLocators.CURRENCY)
        if currency.upper() == "EUR":
            self.click(MainPageLocators.EURO)
            if "€" in self.find_element(MainPageLocators.FIRST_ITEM_PRICE).text:
                return
        if currency.upper() == "USD":
            self.click(MainPageLocators.DOLLARS)
            if "$" in self.find_element(MainPageLocators.FIRST_ITEM_PRICE).text:
                return
        if currency.upper() == "GBP":
            self.click(MainPageLocators.GBP)
            if "£" in self.find_element(MainPageLocators.FIRST_ITEM_PRICE).text:
                return
        self.fail("Валюта не применилась")
