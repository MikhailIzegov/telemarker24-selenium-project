import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from model.pages.cart_menu import CartMenu
from sections.filters_apple_iphones import FiltersAppleIphones as fai
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException

ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)


# fai наследуется от Base, поэтому если AppleIphonesSection - потомок fai,
# то он автоматически наследует Base, в том числе. И если указать class AppleIphonesSection(Base, fai),
# то возникнет ошибка в наследовании классов
class AppleIphonesSection(fai, CartMenu):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

        self.set_filters_btn = (By.XPATH, "//button[@id='set_filter']")
        self.flying_results_wrap = (By.XPATH, "//button[@class='btn-show-results']")
        self.product_to_cart = (By.XPATH, "//button[@id='bx_3966226736_blocks-88154_buy_link']")
        # Если появился такой элемент (с классом forced), то это одна из успешных проверок на добавление в корзину
        self.msg_after_adding_to_cart = (By.XPATH, "//button[contains(@class, 'forced')]/span[@class='text in-cart']")
        self.text_in_cart_already_in_cart = (By.XPATH, "//button[@data-product-id='88154']/span[@class='text in-cart']")
        self.product_price_on_page = (By.XPATH, "//span[@id='bx_3966226736_blocks-88154_price']/span[@class='value']")
        self.product_name_on_page = (By.XPATH, "//*[@id='bx_3966226736_blocks-88154']//a/span")

    target_value_price_filter = 100000

    # Getters

    def get_price_filter_pull(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, fai.price_filter_pull)))

    def get_current_value_price_filter_pull(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, fai.current_value_price_filter_pull)))

    def get_set_filters_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.set_filters_btn)))

    def get_flying_results_wrap(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.flying_results_wrap)))

    def get_product_to_cart_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_to_cart)))

    def get_msg_after_adding_to_cart(self):
        return (WebDriverWait(self.driver, 30, ignored_exceptions=ignored_exceptions)
                .until(EC.element_to_be_clickable((By.XPATH, self.msg_after_adding_to_cart))))

    def get_product_name_on_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_name_on_page)))

    def get_product_price_on_page(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located
                                                    ((By.XPATH, self.product_price_on_page)))

    # Actions

    # Тут я практиковался в скриптах, потому что функция с движением ползунка по пикселям не даст выставить его ТОЧНО
    # на значение, например, 100 000. В итоге значение подставляется, но логика не меняется.
    # Не вижу другого выхода, кроме как двигать ползунок на значение близкое к 100 000р

    # def move_slider_to_target_value(self):
    #     (self.driver.execute_script
    #      ("arguments[0].textContent = arguments[1];",
    #       self.get_current_value_price_filter_pull(), self.target_value_price_filter))

    def delete_space_for_conversion(self):
        price_value_with_space = self.get_current_value_price_filter_pull().text
        price_value_no_space = price_value_with_space.replace(" ", "")
        return price_value_no_space

    def move_price_filter_pull_to_target_value(self):
        current_value_price_filter_pull = int(self.delete_space_for_conversion())
        # Если текущее значение меньше целевого, то тянем ползунок вправо
        while current_value_price_filter_pull < self.target_value_price_filter:
            ActionChains(self.driver).drag_and_drop_by_offset(self.get_price_filter_pull(), 10, 0).perform()
            # Ждем, чтобы значение обновилось - тест падал, потому что фильтр не успевал примениться
            self.driver.implicitly_wait(1)
            current_value_price_filter_pull = int(self.delete_space_for_conversion())

    def click_set_filters_btn(self):
        self.get_set_filters_btn().click()

    def add_product_to_cart(self):
        self.get_product_to_cart_btn().click()

    def is_product_in_cart(self):
        self.get_product_to_cart_btn().click()

    def compare_price_on_page_and_in_cart_menu(self):
        self.assert_text(self.get_product_price_on_page(), (self.get_product_price_in_cart_menu()).text)

    def compare_name_on_page_and_in_cart_menu(self):
        self.assert_text(self.get_product_name_on_page(), (self.get_product_name_in_cart_menu()).text)

    # Methods

    def select_product_according_to_filters(self):
        f = fai(self.driver)
        self.get_current_url()
        self.scroll_to_element(self.get_number_of_cores())
        f.select_memory_capacity(512)
        f.select_color("beige")
        self.move_price_filter_pull_to_target_value()
        self.scroll_to_element(self.get_set_filters_btn())
        self.click_set_filters_btn()
        time.sleep(3)
        self.add_product_to_cart()
        # Одна из проверок, что мы добавили в корзину
        self.is_located(self.get_msg_after_adding_to_cart())
