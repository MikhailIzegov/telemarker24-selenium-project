from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.test_data import test_user
from model.application import Application


class Authorization(Application):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

        self.icon_to_login = (By.XPATH, "//span[@class='pseudolink']")
        self.btn_to_login_form = (By.CSS_SELECTOR, ".pseudolink_box > [data-target='#modal_login']")
        self.email_field = (By.XPATH, "//input[@name='USER_LOGIN']")
        self.password_field = (By.XPATH, "//input[@name='USER_PASSWORD']")
        self.checkbox_remember_me = (By.XPATH, "//div[@id='USER_REMEMBER_frm-styler']")
        self.login_btn = (By.XPATH, "//button[contains(@class, 'btn-submit')]/span[text()='Вход в личный кабинет']")
        self.my_account_btn = (By.XPATH, "//a[@href='/personal/']/span[text()='Мой кабинет']")

    # Getters

    def get_icon_to_login(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.icon_to_login))

    def get_btn_to_login_form(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.btn_to_login_form))

    def get_email_field(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.email_field))

    def get_password_field(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.password_field))

    def get_checkbox_remember_me(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.checkbox_remember_me))

    def get_login_btn(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.login_btn))

    def get_my_account_btn(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.my_account_btn))

    # Actions

    def click_icon_to_login(self):
        self.get_icon_to_login().click()

    def click_btn_login_form(self):
        self.get_btn_to_login_form().click()
        print("Login form is opened")

    def input_email_field(self, email):
        self.get_email_field().send_keys(email)

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
        self.browser.refresh()  # Чтобы убрать открывшийся список

    # Methods

    """
    Method authorization
    Авторизация в components, т.к. для нее нет отдельной страницы и 
    авторизоваться можно с любой вкладки сайта в хэдэре
    """
    def authorize(self):
        self.get_current_url()
        self.click_icon_to_login()
        self.click_btn_login_form()
        self.input_email_field(test_user.email)
        self.input_password_field(test_user.password)
        self.remember_me_not()
        self.click_login_btn()
        self.check_logged_in()

