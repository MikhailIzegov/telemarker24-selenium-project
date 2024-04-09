from model.application import Application
from model.components.authorization import Authorization
from pages.apple_iphones import AppleIphonesSection
from pages.cart_menu import CartMenu
from pages.cart_page import CartPage
from pages.main_page import MainPage


def test_buy_product(browser):
    print("Start test 1")

    app = Application(browser)
    app.open('https://telemarket24.ru/')

    logging_in = Authorization(browser)
    logging_in.authorize()

    mp = MainPage(browser)
    mp.move_to_apple_smartphones_section()

    ai = AppleIphonesSection(browser)
    ai.select_product_according_to_filters()

    cm = CartMenu(browser)
    cm.click_cart_icon_header()

    ai.compare_name_on_page_and_in_cart_menu()
    ai.compare_price_on_page_and_in_cart_menu()
    #
    # cm.check_total_and_create_order()
    #
    # cp = CartPage(browser)
    # cp.check_name_and_total_and_create_order()
    print("Конец")
