import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="en",
                     help="Choose language. Example: en")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None

    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option(
        "prefs", {"intl.accept_languages": user_language}
    )

    options_firefox = OptionsFirefox()
    options_firefox.set_preference(
        "intl.accept_languages", user_language
    )

    if browser_name == "chrome":
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        browser = webdriver.Firefox(options=options_firefox)

    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser

    browser.quit()
