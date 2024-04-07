from datetime import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Application:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    """Method get current URL"""
    def get_current_url(self):
        get_url = self.browser.current_url
        print("Current url ", get_url)

    """Method assert text"""
    def assert_text(self, text, result):
        value_text = text.text
        assert value_text == result
        print("Good value text")

    """Method screenshot"""
    def get_screenshot(self):
        current_date = datetime.now().strftime("%Y.%m.%d %H.%M.%S")
        name_screenshot = 'screenshot' + current_date + '.png'
        self.browser.save_screenshot(
            'C:\\Users\\Михаил Сергеевич\\PycharmProjects\\AutoProject\\screen\\' + name_screenshot)

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.browser.current_url
        assert get_url == result
        print("Good value URL")

    """Method scroll to element"""
    def scroll_to_element(self, element):
        action = ActionChains(self.browser)
        action.move_to_element(element).perform()

    """Method is element located on a page"""
    def is_located(self, element):
        WebDriverWait(self.browser, 10).until(EC.visibility_of(element))

    """Method get text from element"""
    def text_from_element(self, element):
        return (WebDriverWait(self.browser, 10).until(EC.visibility_of(element))).text


