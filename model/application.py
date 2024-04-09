from datetime import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Application:

    shared_data = {}  # Словарь для хранения общих данных между страницами (должен быть статическим атрибутом!)

    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def set_data(self, key, value):
        self.shared_data[key] = value

    def get_data(self, key):
        return self.shared_data.get(key)

    """Method get current URL"""
    def get_current_url(self):
        get_url = self.browser.current_url
        print("Current url ", get_url)

    """Method assert text"""
    def assert_text(self, element_1_locator, text_result):
        try:
            # Дожидаемся появления элемента на странице
            element = WebDriverWait(self.browser, 30).until(
                EC.presence_of_element_located(element_1_locator)
            )
            value_text_1 = element.text
            assert value_text_1 == text_result
            print("Good value text")

        except AssertionError as e:
            print(f"Assertion Error: {e}")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

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
        result = (WebDriverWait(self.browser, 10).until(EC.visibility_of(element))).text
        return result

    def first_element(self, elements_locator):
        try:
            # Ожидаем появления хотя бы одного элемента, соответствующего локатору
            elements = WebDriverWait(self.browser, 30).until(
                EC.presence_of_all_elements_located(elements_locator)
            )
            # Возвращаем первый элемент, если список не пустой
            if elements:
                return elements[0]
        except Exception as e:
            print(f"Произошла ошибка при поиске элемента: {e}")
        return None


