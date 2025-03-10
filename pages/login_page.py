from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Слово login отсутствует в текущей ссылке"    
        
    def register_new_user(self, email, password):
        self.input(*LoginPageLocators.REG_EMAIL, value=mail)
        self.input(*LoginPageLocators.REG_PASS1, value=password)
        self.input(*LoginPageLocators.REG_PASS2, value=password)
        self.browser.find_element(*LoginPageLocators.REG_BTN).click()    
    
    
    def should_be_login_form(self):
        assert self.browser.find_element(By.CSS_SELECTOR, "#login_form"), "Login form is not presented"

    def should_be_register_form(self):
        assert self.browser.find_element(By.CSS_SELECTOR, "#register_form"), "Register form is not presented"
