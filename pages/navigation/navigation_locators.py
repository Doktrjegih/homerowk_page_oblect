from dataclasses import dataclass


@dataclass
class Pages:
    COMPONENTS: str = "Components"
    MONITORS: str = "Monitors"
    REGISTER: str = "Register"
    ADMIN_LOGIN: str = "Admin"


@dataclass
class NavigationLocators:
    COMPONENTS_MENU: str = '//a[text()="Components"]'
    MONITORS: str = (
        f'{COMPONENTS_MENU}/following-sibling::div//a[contains(text(), "Monitors")]'
    )
    ALL_COMPONENTS: str = (
        f'{COMPONENTS_MENU}/following-sibling::div//a[@class="see-all"]'
    )

    MY_ACCOUNT: str = '//span[text()="My Account"]'
    REGISTER: str = f'{MY_ACCOUNT}/ancestor::li//a[text()="Register"]'
