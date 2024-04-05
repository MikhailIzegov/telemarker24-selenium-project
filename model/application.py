from model.components.authorization import Authorization
from model.pages.apple_iphones import AppleIphonesSection
from model.pages.cart_menu import CartMenu
from model.pages.cart_page import CartPage
from model.pages.main_page import MainPage
from tests.conftest import conf_driver


class Application:
    def __init__(self, driver):
        self.driver = driver
        self.auth = Authorization(driver)
        self.main_page = MainPage(driver)
        self.cart_page = CartPage(driver)
        self.cart_menu = CartMenu(driver)
        self.ais = AppleIphonesSection(driver)

    @property
    def open(self, link):
        return self.driver.get(link)


app = Application(conf_driver)
