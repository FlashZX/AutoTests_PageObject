import pytest
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    @pytest.mark.skip
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), 'Basket button is not presented!'

    def add_product_to_basket(self):
        add_product = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_product.click()

    def check_product_add_notification(self):
        add_notice = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_DISCRIPTION).text
        assert add_notice == product_name, 'Cost in notice is not equal to cost of product!'

    def check_product_price_notification(self):
        cost_in_notice = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_DISCRIPTION).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert cost_in_notice == basket_price, 'Cost in notice is not equal to cost of basket!'