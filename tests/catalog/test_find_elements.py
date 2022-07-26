import allure
import pytest
from selenium import webdriver

from pages.navigation.navigation import Navigation
from pages.navigation.navigation_locators import Pages
from pages.page_catalog.catalog_page import CatalogPage
from pages.page_catalog.catalog_page_locators import CatalogPageLocators


@allure.parent_suite("Каталог")
@allure.suite("Проверки страницы каталога товаров")
@allure.title("Проверка наличия элементов на странице")
@pytest.mark.usefixtures("open_opencart")
def test_find_elements(driver: webdriver):
    catalog = CatalogPage(driver)
    navigation = Navigation(driver)

    navigation.goto_page(Pages.MONITORS)
    with allure.step("Проверить наличие элементов на странице"):
        assert catalog.is_element_present(CatalogPageLocators.BREADCRUMBS)
        assert catalog.is_element_present(CatalogPageLocators.ITEM)
        assert catalog.is_element_present(CatalogPageLocators.SELECT_INPUT)
        assert catalog.is_element_present(CatalogPageLocators.LEFT_MENU)
        assert catalog.is_element_present(CatalogPageLocators.PAGE_TITLE)
