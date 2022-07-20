import allure
import pytest
from selenium import webdriver

from pages.navigation.navigation import Navigation
from pages.navigation.navigation_locators import Pages
from pages.page_catalog.catalog_page_locators import CatalogPageLocators
from pages.page_item.item_page import ItemPage
from pages.page_item.item_page_locators import ItemPageLocators


@allure.parent_suite("Товары")
@allure.suite("Проверки страницы товара")
@allure.title("Проверка наличия элементов на странице")
@pytest.mark.usefixtures("open_opencart")
def test_find_elements(driver: webdriver):
    item = ItemPage(driver)
    navigation = Navigation(driver)

    navigation.goto_page(Pages.MONITORS)
    item.click(
        CatalogPageLocators.CERTAIN_ITEM.replace("text-&", "Samsung SyncMaster 941BW")
    )
    with allure.step("Проверить наличие элементов на странице"):
        assert item.is_element_present(ItemPageLocators.ITEM_IMAGE)
        assert item.is_element_present(ItemPageLocators.NAME)
        assert item.is_element_present(ItemPageLocators.INPUT_AMOUNT)
        assert item.is_element_present(ItemPageLocators.ADD_TO_CART_BUTTON)
        assert item.is_element_present(ItemPageLocators.FAVORITES_BUTTON)
