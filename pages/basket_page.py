from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_alerts(self):
        assert self.are_elements_present(*BasketPageLocators.ALERTS), "Alerts are not presented"

    def check_product_info(self, prod_name, prod_price):
        alerts = self.browser.find_elements(*BasketPageLocators.ALERTS)
        assert prod_name == alerts[0].text, f"Expected {prod_name}, get {alerts[0].text}"
        assert prod_price == alerts[2].text, f"Expected {prod_price}, get {alerts[2].text}"

    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.IN_BASKET), "Корзина не пуста"

    def should_be_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.CONTENT)
