import pytest

from pages.base_page import BasePage
from pages.page_register.register_page_locators import RegisterPageLocators


class RegisterPage(BasePage):
    def create_user(
        self, name: str, last_name: str, email: str, tel: str, password: str
    ):
        self.input_text(RegisterPageLocators.FIRSTNAME_FIELD, text=name)
        self.input_text(RegisterPageLocators.LASTNAME_FIELD, text=last_name)
        self.input_text(RegisterPageLocators.EMAIL_FIELD, text=email)
        self.input_text(RegisterPageLocators.TELEPHONE_FIELD, text=tel)
        self.input_text(RegisterPageLocators.PASSWORD_FIELD, text=password)
        self.input_text(RegisterPageLocators.CONFIRM_PASSWORD, text=password)
        self.click(RegisterPageLocators.POLICY_AGREE_CHECKBOX)
        self.click(RegisterPageLocators.SUBMIT_BUTTON)
        if self.is_element_present(RegisterPageLocators.SUCCESS_REGISTER):
            return
        pytest.fail('Пользователь не зарегистрирован')
