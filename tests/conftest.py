from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest


@pytest.fixture(scope='module', autouse=False)
def conf_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # options.add_argument("--headless")
    g = Service('C:\\chromedriver\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)

    yield driver
    driver.quit()

