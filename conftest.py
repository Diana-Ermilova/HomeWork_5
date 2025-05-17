import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(autouse=True, scope='module')
def configure_base_browser():
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1366
    browser.config.window_height = 1280
    browser.config.driver_options.page_load_strategy = 'eager'
    browser.config.timeout = 20.0
    yield
    browser.quit()



