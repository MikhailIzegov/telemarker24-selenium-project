from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from base.base_class import Base
from model.application import app
from model.pages.cart_menu import CartMenu
from model.pages.cart_page import CartPage
from model.pages.main_page import MainPage


def test_buy_product(conf_driver):
    driver = conf_driver
    print("Start test 1")

    driver.get('https://telemarket24.ru/')
    driver.maximize_window()


    # app.auth.authorization()
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