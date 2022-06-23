from dataclasses import dataclass


@dataclass
class ItemPageLocators:
    ITEM_IMAGE: str = '//a[@class="thumbnail"]//img'
    NAME: str = '//h1[text()="Samsung SyncMaster 941BW"]'
    INPUT_AMOUNT: str = '//input[@name="quantity"]'
    ADD_TO_CART_BUTTON: str = '//button[text()="Add to Cart"]'
    FAVORITES_BUTTON: str = '//div[@class="btn-group"]//i[@class="fa fa-heart"]'
