import pytest

from pages.base_page import BasePage
from pages.page_main.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def switch_currency(self):
        self.click(MainPageLocators.CURRENCY)
        self.click(MainPageLocators.EURO)
        if '€' in self.find_element(MainPageLocators.FIRST_ITEM_PRICE).text:
            pass
        else:
            pytest.fail('Валюта не применилась')
        self.click(MainPageLocators.CURRENCY)
        self.click(MainPageLocators.DOLLARS)
        if '$' in self.find_element(MainPageLocators.FIRST_ITEM_PRICE).text:
            pass
        else:
            pytest.fail('Валюта не применилась')
