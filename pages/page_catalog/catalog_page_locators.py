from dataclasses import dataclass


@dataclass
class CatalogPageLocators:
    BREADCRUMBS: str = '//ul[@class="breadcrumb"]'
    ITEM: str = '//div[contains(@class, "product-layout")]'
    SELECT_INPUT: str = "//select"
    LEFT_MENU: str = '//div[@class="list-group"]'
    PAGE_TITLE: str = '//h2[text()="Monitors"]'

    CERTAIN_ITEM: str = f'{ITEM}//h4/a[text()="text-&"]'
