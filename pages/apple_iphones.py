import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.test_data import test_user
from model.application import Application
from sections.filters_apple_iphones import FiltersAppleIphones as fai
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException

ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)


class AppleIphonesSection(Application):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Locators

    set_filters_btn = (By.XPATH, "//button[@id='set_filter']")
    flying_results_wrap = (By.XPATH, "//button[@class='btn-show-results']")
    all_given_products_cart_btn = (By.XPATH, "//button[contains(@class, 'btn-action buy')]")
    # Если появился такой элемент (с классом forced), то это одна из успешных проверок на добавление в корзину
    msg_after_adding_to_cart = (By.XPATH, "//button[contains(@class, 'forced')]/span[@class='text in-cart']")
    text_in_cart_already_in_cart = (By.XPATH, "//button[@data-product-id='88155']/span[@class='text in-cart']")
    product_price_on_page = (By.XPATH, "//span[@id='bx_3966226736_blocks-88155_price']/span[@class='value']")
    product_name_on_page = (By.XPATH, "//*[@id='bx_3966226736_blocks-88155']//a/span")
    icon_to_login = (By.XPATH, "//span[@class='pseudolink']")

    target_value_price_filter = test_user.budget_from_filter

    # Getters

    def get_price_filter_pull(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable((By.XPATH, fai.price_filter_pull)))

    def get_current_value_price_filter_pull(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable
                                                    ((By.XPATH, fai.current_value_price_filter_pull)))

    def get_set_filters_btn(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.set_filters_btn))

    def get_flying_results_wrap(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.flying_results_wrap))

    def get_all_given_products_cart_btn(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.all_given_products_cart_btn))

    def get_msg_after_adding_to_cart(self):
        return (WebDriverWait(self.browser, 30, ignored_exceptions=ignored_exceptions)
                .until(EC.visibility_of_element_located(self.msg_after_adding_to_cart)))

    def get_product_name_on_page(self):
        return WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located(self.product_name_on_page))

    def get_product_price_on_page(self):
        return WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located
                                                     (self.product_price_on_page))

    def get_icon_to_login(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.icon_to_login))

    # Actions

    '''
        def move_slider_to_target_value(self):
        (self.driver.execute_script
         ("arguments[0].textContent = arguments[1];",
          self.get_current_value_price_filter_pull(), self.target_value_price_filter))
    '''

    def save_product_name_on_page(self):
        product_name_on_page = self.get_product_name_on_page()
        self.set_data('product_name_on_page', self.text_from_element(product_name_on_page))
        print(self.get_data('product_name_on_page'))

    def save_product_price_on_page(self):
        product_price_on_page = self.get_product_price_on_page()
        product_price_on_page_text = self.text_from_element(product_price_on_page)
        product_price_on_page_text = product_price_on_page_text.replace(" ", "")
        self.set_data('product_price_on_page', product_price_on_page_text)
        print(self.get_data('product_price_on_page'))

    def delete_space_for_conversion(self):
        price_value_with_space = self.get_current_value_price_filter_pull().text
        price_value_no_space = price_value_with_space.replace(" ", "")
        return price_value_no_space

    def move_price_filter_pull_to_target_value(self):
        current_value_price_filter_pull = int(self.delete_space_for_conversion())

        # Если текущее значение меньше целевого, то тянем ползунок вправо
        while current_value_price_filter_pull < self.target_value_price_filter:
            ActionChains(self.browser).drag_and_drop_by_offset(self.get_price_filter_pull(), 10, 0).perform()
            # Ждем, чтобы значение обновилось - тест падал, потому что фильтр не успевал примениться

            self.browser.implicitly_wait(1)
            current_value_price_filter_pull = int(self.delete_space_for_conversion())

    def click_set_filters_btn(self):
        self.get_set_filters_btn().click()

    def add_product_to_cart(self):
        self.first_element(self.all_given_products_cart_btn).click()

    def compare_price_on_page_and_in_cart_menu(self):
        self.assert_text(self.product_price_on_page, (self.get_data('product_price_in_cart_menu')))

    def compare_name_on_page_and_in_cart_menu(self):
        self.assert_text(self.product_name_on_page, (self.get_data('product_name_in_cart_menu')))

    # Methods

    def select_product_according_to_filters(self):
        f = fai(self.browser)
        self.get_current_url()
        self.scroll_to_element(f.get_number_of_cores())
        f.select_memory_capacity(256)
        f.select_color("beige")
        self.move_price_filter_pull_to_target_value()
        self.scroll_to_element(self.get_set_filters_btn())
        self.click_set_filters_btn()
        time.sleep(3)
        self.save_product_name_on_page()
        self.save_product_price_on_page()
        self.add_product_to_cart()
        self.is_located(self.get_msg_after_adding_to_cart())
        self.scroll_to_element(self.get_icon_to_login())
