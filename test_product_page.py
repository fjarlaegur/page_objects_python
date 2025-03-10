import pytest
from .pages.product_page import ProductPage


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
parameter_list = [f"?promo=offer{i}" for i in range(10)]
link_list = [link + parameter for parameter in parameter_list]

#  marking bugged promo as xfail
link_list[7] = pytest.param(link_list[7], marks=pytest.mark.xfail)


@pytest.mark.parametrize("link", link_list)
def test_guest_can_add_products_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.product_is_in_basket()
