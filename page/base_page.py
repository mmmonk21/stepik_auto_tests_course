from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import math
import time
from .locators import BasePageLocators
from selenium.webdriver.common.by import By


class BasePage:
   def __init__(self, browser, url, timeout=10):
    self.browser = browser
    self.url = url
    #self.browser.implicitly_wait(timeout)
    
   def are_elements_present(self, how, what):
        return self.browser.find_elements(how, what)
   
   def is_element_present(self, how, what):
    try:
        self.browser.find_element(how, what)
    except (NoSuchElementException):
        return False
    return True 
    
   def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click() 
    
   def open(self):
     self.browser.get(self.url)
     
   def is_not_element_present(self, how, what, timeout=4):
    try:
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
    except TimeoutException:
        return True
    return False
    
    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()
    
    def input(self, locator_type, locator, value):
        element = self.browser.find_element(locator_type, locator)
        element.send_keys(value)
    
    def is_disappeared(self, how, what, timeout=4):
     try:
        WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
     except TimeoutException:
        return False

     return True
     
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click() 
     
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
        " probably unauthorised user" 

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"     
     
    def solve_quiz_and_get_code(self):
     
     WebDriverWait(self.browser, 10).until(EC.alert_is_present())
     alert = self.browser.switch_to.alert
     x = alert.text.split(" ")[2]
     answer = str(math.log(abs((12 * math.sin(float(x))))))
     alert.send_keys(answer)
     alert.accept()
     try:
        WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
     except NoAlertPresentException:
        print("No second alert presented")     
     # assert self.is_goods_in_basket(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Goods not in basket"
