import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


@pytest.fixture(scope='session', autouse=False)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def setup_browser(load_env):
    options = Options()
    options.add_argument('--start-maximized')
    selenoid_capabilities = {
        'browserName': 'chrome',
        'browserVersion': '100.0',
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    selenoid_login = os.getenv('SELENOID_LOGIN')
    selenoid_password = os.getenv('SELENOID_PASSWORD')

    browser = webdriver.Remote(
        command_executor=f'https://{selenoid_login}:{selenoid_password}@selenoid.autotests.cloud/wd/hub',
        options=options
    )

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
