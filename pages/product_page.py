from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
#       self.solve_quiz_and_get_code()

    def product_is_in_basket(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
            ).text
        added_product_name = self.browser.find_element(
            *ProductPageLocators.ADDED_PRODUCT_NAME
            ).text
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
            ).text
        basket_total = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL
            ).text
        assert added_product_name == product_name and basket_total == product_price, \
            f"Expected {product_name} and {product_price}, got {added_product_name} and {basket_total}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
            ), \
            "Success message is on the page, and it shouldn't be"

    def disappeared_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), \
            "Success message didn't disappear"
