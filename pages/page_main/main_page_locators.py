from dataclasses import dataclass


@dataclass
class MainPageLocators:
    LOGO: str = '//img[@title="Your Store"]'
    SLIDESHOW_PICTURES: str = '//div[@class="swiper-wrapper"]'
    SEARCH_INPUT: str = '//div[@id="search"]/input'
    SHOP_CART: str = '//button[@data-loading-text="Loading..."]'
    NAVIGATION_BAR: str = '//nav[@id="menu"]'

    CURRENCY: str = "//strong/following-sibling::span"
    EURO: str = '//button[@name="EUR"]'
    DOLLARS: str = '//button[@name="USD"]'
    GBP: str = '//button[@name="GBP"]'

    FIRST_ITEM_PRICE: str = '//p[@class="price"]'
