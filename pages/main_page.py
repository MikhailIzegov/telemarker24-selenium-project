from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from model.application import Application


class MainPage(Application):

    # Locators

    burger_menu = (By.XPATH, "//div[@class='kat_btn']")
    smartphones_section = (By.XPATH, "//span[@class='category-name' and text()='Телефоны и смартфоны']")
    apple_iphone_section = (By.XPATH, "//span[@class='text' and text()='Apple iPhone']")
    title_apple_iphone_section = (By.XPATH, "//h1[contains(text(), 'Смартфоны Apple iPhone')]")

    # Getters

    def get_burger_menu(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.burger_menu))

    def get_smartphones_section(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.smartphones_section))

    def get_apple_iphone_section(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.apple_iphone_section))

    def get_title_apple_iphone_section(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.title_apple_iphone_section))

    # Actions

    def hover_burger_menu(self):
        action = ActionChains(self.browser)
        action.move_to_element(self.get_burger_menu()).perform()

    def hover_smartphones_section(self):
        action = ActionChains(self.browser)
        action.move_to_element(self.get_smartphones_section()).perform()

    def click_apple_iphone_section(self):
        self.get_apple_iphone_section().click()

    # Methods

    def move_to_apple_smartphones_section(self):
        self.get_current_url()
        self.hover_burger_menu()
        self.hover_smartphones_section()
        self.click_apple_iphone_section()
        assert self.get_title_apple_iphone_section().is_displayed(), "We are NOT in the the apple_iphone_section"
