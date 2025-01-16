from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "h1 + .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alertinner > p > strong ")
    PRODUCT_NAME_PAGE = (By.CSS_SELECTOR, "div.row h1")
    SUCCESS_MESSAGE = By.XPATH, "//div[@class='alertinner ']//strong[contains(text(), 'Coders at Work')]"
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK = By.XPATH, "//a[@class='btn btn-default']"
    
class LoginPageLocators:
    LOGIN_FORM = By.CSS_SELECTOR, "#login_form"
    REGISTER_FORM = By.CSS_SELECTOR, "#register_form"

    REG_EMAIL = By.CSS_SELECTOR, "#id_registration-email"
    REG_PASS1 = By.CSS_SELECTOR, "#id_registration-password1"
    REG_PASS2 = By.CSS_SELECTOR, "#id_registration-password2"
    REG_BTN = By.XPATH, "//form[@id='register_form']//button"
    
class BasketPageLocators:
    ALERTS = By.CSS_SELECTOR, ".alertinner strong"
    CONTENT = By.CSS_SELECTOR, "#content_inner"
    IN_BASKET = By.CSS_SELECTOR, ".basket-mini strong"
