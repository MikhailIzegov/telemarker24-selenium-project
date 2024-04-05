from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


# Не page, а menu - оно открывается по клику из футера, page - тоже есть, но это отдельный модуль
class CartMenu(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators

        self.cart_icon_header = (By.XPATH, "//span[@class='icon_cart']")
        self.product_price = (By.XPATH, "//tr[@data-product-id='88154']//span[@class='value']")
        self.product_name = (By.XPATH, "//tr[@data-product-id='88154']//a/span[@class='text']")
        self.total_sum = (By.XPATH, "//span[@class='total']//span[@class='value']")
        self.create_order_btn = (By.XPATH, "//a[contains(@class, 'btn-main')]//span[@class='text']")
        self.all_products_in_cart_menu = (By.XPATH, "(//tr//span[@class='value'])")
        self.cart_page_title = (By.XPATH, "//h1[contains( text(), 'Корзина')]")

    # Getters

    def get_cart_icon_header(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.cart_icon_header))

    def get_product_price_in_cart_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.product_price))

    def get_product_name_in_cart_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.product_name))

    def get_total_sum(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.total_sum))

    def get_create_order_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.create_order_btn))

    def get_cart_page_title(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.cart_page_title))

    # Actions

    def click_cart_icon_header(self):
        self.get_cart_icon_header().click()

    # Эта функция не учитывает разное кол-во одного и того же товара! - исправить
    def compare_total_with_selected_products(self):
        locator_index = 1
        summed_price = 0
        while True:
            try:
                # Формируем локатор элемента в корзине
                locator = f"{self.all_products_in_cart_menu}[{locator_index}]"
                print(locator)
                # Записываем локатор в такую переменную, чтобы это был объект класса WebElement, иначе выдавал ошибку!
                loc = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, locator)))
                print(type(loc))
                # Убираем пробел, конвертим в int, чтобы сложить и проверить total
                price_in_cart_text = self.text_from_element(loc).replace(" ", "")
                print(price_in_cart_text)
                price_in_cart_numeric = int(price_in_cart_text)
                summed_price += price_in_cart_numeric
                locator_index += 1
                print(locator_index)
            # Если NoSuchElementException или TimeoutException возникает, значит мы достигли конца корзины
            except (NoSuchElementException, TimeoutException):
                print("End of cart items.")
                break

        ts = self.get_total_sum()
        total_price_text = self.text_from_element(ts).replace(" ", "")
        total_price_numeric = int(total_price_text)
        assert summed_price == total_price_numeric, "Итоговая сумма не равна сумме товаров в корзине"
        print("Итоговая сумма равна сумме товаров в корзине")

    def click_create_order_btn(self):
        self.get_create_order_btn().click()

    def is_cart_page(self):
        assert self.get_cart_page_title().is_displayed(), "Нет заголовка 'Корзина'. Возможно вы находитесь не в корзине"

    # Methods

    def check_total_and_create_order(self):
        self.compare_total_with_selected_products()
        self.click_create_order_btn()
        self.is_cart_page()



