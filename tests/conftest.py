import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def browser_options():

    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.driver_options.page_load_strategy = 'eager'
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()