from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    PRODUCT_NAME_IN_DISCRIPTION = (By.CSS_SELECTOR , ".col-sm-6 h1")
    PRODUCT_NAME_IN_NOTICE = (By.CSS_SELECTOR, '.alert:nth-child(1) .alertinner strong')
    PRODUCT_PRICE_IN_DISCRIPTION = (By.CSS_SELECTOR, 'p.price_color')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group a.btn-default')
    DISCOUNT_CODE = (By.CSS_SELECTOR, '.btn-full')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
