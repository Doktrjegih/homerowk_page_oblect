from dataclasses import dataclass


@dataclass
class RegisterPageLocators:
    RIGHT_MENU: str = "//aside"

    FIRSTNAME_FIELD: str = '//input[@name="firstname"]'
    LASTNAME_FIELD: str = '//input[@name="lastname"]'
    EMAIL_FIELD: str = '//input[@name="email"]'
    TELEPHONE_FIELD: str = '//input[@name="telephone"]'
    PASSWORD_FIELD: str = '//input[@name="password"]'
    CONFIRM_PASSWORD: str = '//input[@name="confirm"]'

    POLICY_AGREE_CHECKBOX: str = '//div[@class="pull-right"]//input[@type="checkbox"]'

    SUBMIT_BUTTON: str = '//input[@type="submit"]'

    SUCCESS_REGISTER: str = '//h1[text()="Your Account Has Been Created!"]'
