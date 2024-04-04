import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException


ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)


class Base():
    def __init__(self, driver):
        self.driver = driver

    # Locators

    icon_to_login = "//span[@class='pseudolink']"
    btn_to_login_form = ".pseudolink_box > [data-target='#modal_login']"
    email_field = "//input[@name='USER_LOGIN']"
    password_field = "//input[@name='USER_PASSWORD']"
    checkbox_remember_me = "//div[@id='USER_REMEMBER_frm-styler']"
    login_btn = "//button[contains(@class, 'btn-submit')]/span[text()='Вход в личный кабинет']"
    my_account_btn = "//a[@href='/personal/']/span[text()='Мой кабинет']"

    # Getters

    def get_icon_to_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.icon_to_login)))

    def get_btn_to_login_form(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.btn_to_login_form)))

    def get_email_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_field)))

    def get_checkbox_remember_me(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_remember_me)))

    def get_login_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_btn)))

    def get_my_account_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.my_account_btn)))

    # Actions

    def click_icon_to_login(self):
        self.get_icon_to_login().click()

    def click_btn_login_form(self):
        self.get_btn_to_login_form().click()
        print("Login form is opened")

    def input_email_field(self, email):
        self.get_email_field().send_keys(email)  # Убрать костыль, заменить переменной

    def input_password_field(self, password):
        self.get_password_field().send_keys(password)

    def remember_me_not(self):
        self.get_checkbox_remember_me().click()
        print("Do not remember me")

    def click_login_btn(self):
        self.get_login_btn().click()
        print("Clicked login button")

    def check_logged_in(self):
        self.click_icon_to_login()
        assert self.get_my_account_btn().is_displayed()
        self.driver.refresh()  # Чтобы убрать открывшийся список

    # Methods

    # Авторизация в Base, т.к. для нее нет отдельной страницы и авторизоваться можно с любой вкладки сайта в хэдэре
    """Method authorization"""
    def authorization(self):
        self.get_current_url()
        self.click_icon_to_login()
        self.click_btn_login_form()
        self.input_email_field("autotest.selenium.test@yandex.ru")
        self.input_password_field("qweasd123")
        self.remember_me_not()
        self.click_login_btn()
        self.check_logged_in()

    """Method get current URL"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url ", get_url)

    """Method assert text"""

    def assert_text(self, text, result):
        value_text = text.text
        assert value_text == result
        print("Good value text")

    """Method screenshot"""

    def get_screenshot(self):
        current_date = datetime.datetime.now().strftime("%Y.%m.%d %H.%M.%S")
        name_screenshot = 'screenshot' + current_date + '.png'
        self.driver.save_screenshot(
            'C:\\Users\\Михаил Сергеевич\\PycharmProjects\\AutoProject\\screen\\' + name_screenshot)

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value URL")

    """Method scroll to element"""
    def scroll_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    """Method is element located on a page"""
    def is_located(self, element):
        WebDriverWait(self.driver, 10).until(EC.visibility_of(element))

    """Method get text from element"""
    def text_from_element(self, element):
        return (WebDriverWait(self.driver, 10).until(EC.visibility_of(element))).text


