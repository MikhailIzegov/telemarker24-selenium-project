from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from model.application import Application


# Не page, а menu - оно открывается по клику из футера, page - тоже есть, но это отдельный модуль
class CartMenu(Application):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

        # Locators

        self.cart_icon_header = (By.XPATH, "//span[@class='icon_cart']")
        self.product_price = (By.XPATH, "//tr[@data-product-id='88155']//span[@class='value']")
        self.product_name = (By.XPATH, "//tr[@data-product-id='88155']//a/span[@class='text']")
        self.total_sum = (By.XPATH, "//span[@class='total']//span[@class='value']")
        self.create_order_btn = (By.XPATH, "//a[contains(@class, 'btn-main')]//span[@class='text']")
        self.all_products_in_cart_menu = (By.XPATH, "(//tr//span[@class='value'])")
        self.cart_page_title = (By.XPATH, "//h1[contains( text(), 'Корзина')]")

        self.price_of_each_product_in_cart_menu = (By.CSS_SELECTOR, ".price-new > .value")
        self.quantity_of_items = (By.CSS_SELECTOR, "[name='quantity']")

    # Getters

    def get_cart_icon_header(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.cart_icon_header))

    def get_product_price_in_cart_menu(self):
        return WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located(self.product_price))

    def get_product_name_in_cart_menu(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.product_name))

    def get_total_sum(self):
        return WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located(self.total_sum))

    def get_create_order_btn(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.create_order_btn))

    def get_cart_page_title(self):
        return WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located(self.cart_page_title))

    def get_price_of_each_product_in_cart_menu(self):
        return WebDriverWait(self.browser, 30).until(EC.presence_of_all_elements_located
                                                     (self.price_of_each_product_in_cart_menu))

    def get_quantity_of_items(self):
        return WebDriverWait(self.browser, 30).until(EC.presence_of_all_elements_located(self.quantity_of_items))

    # Actions

    def save_product_name_in_cart_menu(self):
        product_name_in_cart_menu = self.get_product_name_in_cart_menu()
        self.set_data('product_name_in_cart_menu', self.text_from_element(product_name_in_cart_menu))

    def save_product_price_in_cart_menu(self):
        product_price_in_cart_menu = self.get_product_price_in_cart_menu()
        self.set_data('product_price_in_cart_menu', self.text_from_element(product_price_in_cart_menu))

    def click_cart_icon_header(self):
        self.get_cart_icon_header().click()

    # Эта функция не учитывает разное кол-во одного и того же товара! - исправить
    def compare_total_with_selected_products(self):
        summed_price = 0

        price_of_each_product_in_cart_menu = self.get_price_of_each_product_in_cart_menu()
        quantity_of = self.get_quantity_of_items()
        for index in range(len(price_of_each_product_in_cart_menu)):
            numeric_price = int(self.text_from_element(price_of_each_product_in_cart_menu[index]).replace(" ", ""))
            multiplier = int(quantity_of[index].get_attribute('value'))
            total_of_item = numeric_price * multiplier
            summed_price += total_of_item

        ts = self.get_total_sum()
        total_price_text = self.text_from_element(ts).replace(" ", "")
        total_price_numeric = int(total_price_text)
        assert summed_price == total_price_numeric, "Итоговая сумма не равна сумме товаров в корзине"

    def click_create_order_btn(self):
        self.get_create_order_btn().click()

    def is_cart_page(self):
        assert self.get_cart_page_title().is_displayed(), "Нет заголовка 'Корзина'. Возможно вы находитесь не в корзине"

    # Methods

    def check_total_and_create_order(self):
        self.compare_total_with_selected_products()
        self.click_create_order_btn()
        self.is_cart_page()



