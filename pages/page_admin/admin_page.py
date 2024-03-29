import allure

from pages.base_page import BasePage
from pages.page_admin.admin_page_locators import AdminPageLocators


class AdminPage(BasePage):
    @allure.step("Открыть страницу авторизации админки")
    def open_page(self, ip: str):
        self.open(f"{ip}/admin")

    @allure.step("Залогиниться на странице авторизации админки")
    def login(self):
        self.input_text(AdminPageLocators.USERNAME_FIELD, text="user")
        self.input_text(AdminPageLocators.PASSWORD_FIELD, text="bitnami")
        self.click(AdminPageLocators.SUBMIT_BUTTON)
        if self.is_element_present(AdminPageLocators.WORLD_MAP_TITLE, timeout=10):
            return
        self.fail("Панель администратора не открылась за 10 секунд")

    @allure.step('Перейти в раздел "Products"')
    def goto_products(self):
        self.click(AdminPageLocators.CATALOG_MENU)
        self.click(AdminPageLocators.PRODUCTS_MENU)
        if self.is_element_present(AdminPageLocators.PRODUCTS_TITLE, timeout=5):
            return
        self.fail("Страница 'Products' не открылась за 5 секунд")

    @allure.step("Создать товар {name}")
    def create_item(self, name: str, tag: str, model: str):
        self.click(AdminPageLocators.CREATE_ITEM_BUTTON)
        self.input_text(AdminPageLocators.PRODUCTS_NAME_FIELD, text=name)
        self.input_text(AdminPageLocators.META_TAG_FIELD, text=tag)
        self.click(AdminPageLocators.DATA_TAB)
        self.input_text(AdminPageLocators.MODEL_FIELD, text=model)
        self.click(AdminPageLocators.SAVE_BUTTON)
        self.input_text(AdminPageLocators.PRODUCTS_NAME_FIELD, text=name)
        self.click(AdminPageLocators.FILTER_APPLY_BUTTON)
        if len(self.find_elements(AdminPageLocators.ROW_IN_TABLE)) == 1:
            pass
        else:
            self.fail("Кол-во отфильтрованных результатов не равно 1")
        self.click(AdminPageLocators.SELECT_ROW.replace("row-&", "1"))
        self.click(AdminPageLocators.DELETE_ITEM_BUTTON)
        self.accept_alert()
        if self.is_element_present(AdminPageLocators.NO_RESULTS):
            return
        self.fail("Товар не удален")
