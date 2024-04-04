from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class FiltersAppleIphones(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    price_filter_pull = "//div[contains(@class, 'noUi-handle-lower')]"
    current_value_price_filter_pull = "//div[contains(@class, 'noUi-handle-lower')]/div"
    number_of_cores = "//span[contains(text(), 'Количество ядер')]"
    memory_toggle = "//span[contains(text(), 'Объем встроенной памяти')]"
    memory = {128: "//div[@id='arrFilter_265_919546716-styler']/following-sibling::span[@class='checkbox-content']",
              256: "//div[@id='arrFilter_265_832761669-styler']/following-sibling::span[@class='checkbox-content']",
              512: "//div[@id='arrFilter_265_2829827839-styler']/following-sibling::span[@class='checkbox-content']",
              1024: "//div[@id='arrFilter_265_3297604967-styler']/following-sibling::span[@class='checkbox-content']"}
    # cb_128_gb = "//input[@id='arrFilter_265_919546716']"
    # cb_256_gb = "//input[@id='arrFilter_265_832761669']"
    # cb_512_gb = "//input[@id='arrFilter_265_2829827839']"
    # cb_1_tb = "//input[@id='arrFilter_265_3297604967']"
    color_toggle = "//span[contains(text(), 'Цвет')]"
    color = {"white": "//div[@id='arrFilter_245_1871979024-styler']/following-sibling::span[@class='checkbox-content']",
             "black": "//div[@id='arrFilter_245_257141749-styler']/following-sibling::span[@class='checkbox-content']",
             "beige": "//div[@id='arrFilter_245_1401779972-styler']/following-sibling::span[@class='checkbox-content']",
             "blue": "//div[@id='arrFilter_245_2623426736-styler']/following-sibling::span[@class='checkbox-content']"
             }
    # cb_white_color = "//input[@id='arrFilter_245_1871979024']"
    # cb_black_color = "//input[@id='arrFilter_245_257141749']"
    # cb_beige_color = "//input[@id='arrFilter_245_1401779972']"
    # cb_blue_color = "//input[@id='arrFilter_245_2623426736']"

    # Getters

    def get_memory_toggle(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.memory_toggle)))

    def get_number_of_cores(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.number_of_cores)))

    def get_internal_memory(self, chosen_memory):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.memory[chosen_memory])))

    def get_color_toggle(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.color_toggle)))

    def get_color(self, chosen_color):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.color[chosen_color])))

    # Actions

    def select_memory_capacity(self, memory):
        self.get_memory_toggle().click()
        print("Развернул тоггл")
        self.get_internal_memory(chosen_memory=memory).click()
        print("Выбрал память")

    def select_color(self, color):
        self.get_color_toggle().click()
        self.get_color(chosen_color=color).click()
        print("Выбрал цвет")

    # Methods
