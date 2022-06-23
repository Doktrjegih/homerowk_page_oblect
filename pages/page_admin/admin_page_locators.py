from dataclasses import dataclass


@dataclass
class AdminPageLocators:
    USERNAME_FIELD: str = '//input[@name="username"]'
    PASSWORD_FIELD: str = '//input[@name="password"]'
    SUBMIT_BUTTON: str = '//button[@type="submit"]'
    FORGET_PASSWORD: str = '//a[text()="Forgotten Password"]'
    OPENCART_SITE: str = '//a[@href="http://www.opencart.com"]'

    WORLD_MAP_TITLE: str = '//h3[normalize-space(text())="World Map"]'

    CATALOG_MENU: str = '//a[normalize-space(text())="Catalog"]'
    PRODUCTS_MENU: str = '//a[text()="Products"]'
    PRODUCTS_TITLE: str = '//h1[text()="Products"]'

    CREATE_ITEM_BUTTON: str = '//i[@class="fa fa-plus"]'
    FILTER_APPLY_BUTTON: str = '//button[@id="button-filter"]'
    DELETE_ITEM_BUTTON: str = '//i[@class="fa fa-trash-o"]'

    DATA_TAB: str = '//a[text()="Data"]'
    SAVE_BUTTON: str = '//i[@class="fa fa-save"]'
    PRODUCTS_NAME_FIELD: str = '//input[@placeholder="Product Name"]'
    META_TAG_FIELD: str = '//input[@placeholder="Meta Tag Title"]'
    MODEL_FIELD: str = '//input[@placeholder="Model"]'

    ROW_IN_TABLE: str = "//tbody//tr"
    NO_RESULTS: str = '//td[text()="No results!"]'
    SELECT_ROW: str = '(//tbody//td//input[@type="checkbox"])[row-&]'
