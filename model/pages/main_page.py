from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    burger_menu = "//div[@class='kat_btn']"
    smartphones_section = "//span[@class='category-name' and text()='Телефоны и смартфоны']"
    apple_iphone_section = "//span[@class='text' and text()='Apple iPhone']"
    title_apple_iphone_section = "//h1[contains(text(), 'Смартфоны Apple iPhone')]"

    # Getters

    def get_burger_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.burger_menu)))

    def get_smartphones_section(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.smartphones_section)))

    def get_apple_iphone_section(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apple_iphone_section)))

    def get_title_apple_iphone_section(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, self.title_apple_iphone_section)))

    # Actions

    def hover_burger_menu(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_burger_menu()).perform()

    def hover_smartphones_section(self):
        action = ActionChains(self.driver)
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
