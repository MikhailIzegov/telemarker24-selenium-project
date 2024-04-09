from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from model.application import Application


class CartPage(Application):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    # Locators

        self.product_price = (By.CSS_SELECTOR, ".basket-items-list-item-price-for-one .basket-item-price-current-text")
        self.product_name = (By.CSS_SELECTOR, ".basket-item-info-name-link span")
        self.total_price_of_1_product = (By.CSS_SELECTOR, "td[class=basket-items-list-item-price] ["
                                                          "class='basket-item-price-current-text']")
        self.total_price = (By.XPATH, "//div[@data-entity='basket-total-price']")
        self.create_order_btn = (By.XPATH, "//button[@data-entity='basket-checkout-button']")
        self.all_products_total_price_of_1_item = (By.XPATH, "(//td[@class='basket-items-list-item-price']//"
                                                             "span[@class='basket-item-price-current-text'])")

    # Getters

    def get_product_price(self):
        return WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located(self.product_price))

    def get_product_name(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.product_name))

    def get_total_price_of_1_product(self):
        return WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located
                                                    (self.total_price_of_1_product))

    def get_total_price(self):
        return WebDriverWait(self.browser, 30).until(EC.visibility_of_element_located(self.total_price))

    def get_create_order_btn(self):
        return WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.create_order_btn))

    # Actions

    def process_total_price_of_1_product(self):
        raw_text = self.text_from_element(self.get_total_price_of_1_product())
        price_text = raw_text.replace("₽", "")
        price_text = price_text.replace(" ", "")
        return price_text

    def compare_price_in_cart_page_and_on_page(self):
        print(self.process_total_price_of_1_product())
        print(self.get_data('product_price_on_page'))
        assert self.process_total_price_of_1_product() == self.get_data('product_price_on_page')

    def compare_name_in_cart_page_and_on_page(self):
        self.assert_text(self.product_name, (self.get_data('product_name_on_page')))

    # Учитывает кол-во товара, но сюда надо добавить еще функцию, которая проверяла бы
    # 1шт * на кол-во = сумма как в локаторе
    # Так же нужно не писать эту Ф. еще раз, а вызвать из cart_menu -
    # 1) это на одну переменную self.all_products_total_price_of_1_item;
    # 2) это на другую self.get_total_price()
    def summ_everything_in_cart_compare_with_total(self):
        locator_index = 1
        summed_price = 0
        while True:
            try:
                # Формируем локатор элемента в корзине
                locator = f"{self.all_products_total_price_of_1_item}[{locator_index}]"
                print(locator)
                # Записываем локатор в такую переменную, чтобы это был объект класса WebElement, иначе выдавал ошибку!
                loc = WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.XPATH, locator)))
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

            ts = self.get_total_price()
            total_price_text = self.text_from_element(ts).replace(" ", "")
            total_price_numeric = int(total_price_text)
            assert summed_price == total_price_numeric, "Итоговая сумма не равна сумме товаров в корзине"
            print("Итоговая сумма равна сумме товаров в корзине")

    # Methods

    def check_name_and_total_and_create_order(self):
        self.compare_price_in_cart_page_and_on_page()
        self.compare_name_in_cart_page_and_on_page()



