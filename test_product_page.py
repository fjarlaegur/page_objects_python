from .pages.product_page import ProductPage


def test_guest_can_add_products_to_basket(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.product_is_in_basket()
