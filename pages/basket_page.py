from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_no_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.DISCOUNT_CODE), \
                                        "Discount code button is presented, but should not be!"

    def should_be_empty_basket_message(self):
        empty_basket_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert 'Your basket is empty' in empty_basket_message, \
                                        'Empty basket message is not present, but should be!'
