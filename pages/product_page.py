from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC




class ProductPage(BasePage):
    def add_to_basket(self):
     add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
     add_button.click()
     #BasePage.solve_quiz_and_get_code(self)
     
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
    
    def should_be_product_page(self):
        self.should_be_basket_and_product_same_name()
        self.should_be_basket_and_product_same_price()
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"    
         
    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Element is presented, but should disappear"

    def should_be_basket_and_product_same_name(self):
        # Проверка того, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром,
        # который добавили
        product_name_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_PAGE).text
        product_name_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_BASKET).text
        assert product_name_basket == product_name_page, \
            f"Product names in page and basket are not the same! {product_name_page} != {product_name_basket}"

    def should_be_basket_and_product_same_price(self):
        # Проверка стоимости в корзине. Стоимость в корзине должна совпадать с ценой товара
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text[1:]
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text[1:]
        assert product_price == basket_price, \
            f"Product prices in page and basket are not the same! {product_price} != {basket_price}"
