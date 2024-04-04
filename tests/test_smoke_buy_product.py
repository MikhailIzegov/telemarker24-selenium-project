from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from base.base_class import Base
from model.pages import AppleIphonesSection
from model.pages.cart_menu import CartMenu
from model.pages.cart_page import CartPage
from model.pages.main_page import MainPage


def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # options.add_argument("--headless")
    g = Service('C:\\Users\\Михаил Сергеевич\\PycharmProjects\\resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=g)
    url = "https://telemarket24.ru/"
    # Это должно быть именно в тесте перед авторизацией, ибо залогиниться можно с любой вкладки / урлы
    driver.get(url)
    driver.maximize_window()
    print("Start test 1")

    logging_in = Base(driver)
    logging_in.authorization()
    mp = MainPage(driver)
    mp.move_to_apple_smartphones_section()

    ai = AppleIphonesSection(driver)
    ai.select_product_according_to_filters()

    cm = CartMenu(driver)
    cm.click_cart_icon_header()
    ai.compare_name_on_page_and_in_cart_menu()
    ai.compare_price_on_page_and_in_cart_menu()
    cm.check_total_and_create_order()

    cp = CartPage(driver)
    cp.check_name_and_total_and_create_order()
    print("Конец")