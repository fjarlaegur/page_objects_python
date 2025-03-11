import pytest
from .pages.product_page import ProductPage


BASE_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

#  creating a list comprehension for promos ranged 0-9
parameter_list = [f"?promo=offer{i}" for i in range(10)]
promo_link_list = [BASE_LINK + parameter for parameter in parameter_list]

#  marking bugged promo as xfail
promo_link_list[7] = pytest.param(promo_link_list[7], marks=pytest.mark.xfail)


@pytest.mark.parametrize("link", promo_link_list)
def test_guest_can_add_products_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.product_is_in_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, BASE_LINK)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, BASE_LINK)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, BASE_LINK)
    page.open()
    page.add_product_to_basket()
    page.disappeared_success_message()
