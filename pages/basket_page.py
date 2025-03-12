from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        self.no_items_in_basket()
        self.should_be_empty_basket_message()

    def no_items_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEM
        ), "There are items in basket when it should be empty"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE
        ), "No empty basket message present"
