from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture(scope='module', autouse=False)
def browser(request):
    options = webdriver.ChromeOptions()
    options.add_argument('start=maximized')
    options.add_experimental_option("detach", True)
    # options.add_argument("--headless")
    g = Service('C:\\chromedriver\\chromedriver-win64\\chromedriver.exe')
    browser = webdriver.Chrome(options=options, service=g)

    yield browser

    browser.quit()

