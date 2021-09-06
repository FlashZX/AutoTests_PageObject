from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), 'Basket button is not presented!'

    def add_product_to_basket(self):
        add_product = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_product.click()

    def check_product_add_notice(self):
        name_in_notice = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_NOTICE).text
        name_in_discription = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_DISCRIPTION).text
        assert name_in_notice == name_in_discription, 'Cost in notice is not equal to cost of product!'

    def check_product_price_notice(self):
        cost_in_notice = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_DISCRIPTION).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert cost_in_notice == basket_price, 'Cost in notice is not equal to cost of basket!'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_IN_NOTICE), \
            "Success message is presented, but should not be"

    def should_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_IN_NOTICE), \
            "Success message is presented, but should not be"