import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


BASE_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

#  list comprehension for promos ranged 0-9
parameter_list = [f"?promo=offer{i}" for i in range(10)]
promo_link_list = [BASE_LINK + parameter for parameter in parameter_list]

#  marking bugged promo as xfail
promo_link_list[7] = pytest.param(promo_link_list[7], marks=pytest.mark.xfail)


@pytest.mark.adding_to_basket
class TestAddingProductToBasket():
    @pytest.mark.skip
    @pytest.mark.parametrize("link", promo_link_list)
    def test_guest_can_add_products_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.product_is_in_basket()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, BASE_LINK)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        page = ProductPage(browser, BASE_LINK)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, BASE_LINK)
        page.open()
        page.add_product_to_basket()
        page.disappeared_success_message()


@pytest.mark.login_guest_product
class TestLoginFromProductPage():
    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, BASE_LINK)
        page.open()
        page.login_link_exists()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, BASE_LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, BASE_LINK)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_is_empty()
