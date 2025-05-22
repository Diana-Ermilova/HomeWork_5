import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os

from utils.attach import *

@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()



@pytest.fixture(autouse=True, scope='module')
def configure_base_browser():
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1500
    browser.config.timeout = 10.0

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    options=Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "127.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    executor = f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub"
    driver = webdriver.Remote(
        command_executor=executor,
        options=options)
    browser.config.driver = driver


    yield

    add_screenshot(browser)
    add_html(browser)
    add_video(browser)
    add_logs(browser)
    browser.quit()



