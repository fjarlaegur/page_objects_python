from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def login_link_exists(self):
        """Check if there's a login link on a page.
        """
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK
            ), "Login link doesn't exist"

    def go_to_basket(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    def is_element_present(self, how, what):
        """Check if a certain element is present on a page.

        Args:
            how (By): How we want to locate an element (e.g. By.CSS_SELECTOR, By.XPATH etc).
            what (str): The locator string.

        Returns:
            bool: True if the element is found, otherwise False.
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """Check if a certain element is not present on a page.

        Args:
            how (By): How we want to locate an element (e.g. By.CSS_SELECTOR, By.XPATH etc).
            what (str): The locator string.
            timeout (int, optional): The number of seconds to check for element presence.

        Returns:
            bool: True if element is not located, otherwise False.
        """
        try:
            WebDriverWait(self.browser, timeout).\
                until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """Check if a certain element that is present on a page disappeared.

        Args:
            how (By): How we want to locate an element (e.g. By.CSS_SELECTOR, By.XPATH etc).
            what (str): The locator string.
            timeout (int, optional): The number of seconds to check for element presence.

        Returns:
            bool: True if element has disappeared, otherwise False.
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        """Method to solve a math expression, which appears only if there's a
        'promo' parameter in the product's URL and you're trying to add
        the product to basket.
        """
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
