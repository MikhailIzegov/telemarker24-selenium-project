from model.application import Application
from model.components.authorization import Authorization


def test_buy_product(browser):
    print("Start test 1")

    app = Application(browser)
    app.open('https://telemarket24.ru/')

    logging_in = Authorization(browser)
    logging_in.authorization()

    #
    # mp = MainPage(init_driver)

    #
    # logging_in = Base(driver)
    # logging_in.authorization()
    # mp = MainPage(driver)
    # mp.move_to_apple_smartphones_section()
    #
    # ai = AppleIphonesSection(driver)
    # ai.select_product_according_to_filters()
    #
    # cm = CartMenu(driver)
    # cm.click_cart_icon_header()
    # ai.compare_name_on_page_and_in_cart_menu()
    # ai.compare_price_on_page_and_in_cart_menu()
    # cm.check_total_and_create_order()
    #
    # cp = CartPage(driver)
    # cp.check_name_and_total_and_create_order()
    print("Конец")
