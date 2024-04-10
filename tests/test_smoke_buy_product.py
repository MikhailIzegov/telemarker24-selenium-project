import allure
from allure_commons.types import Severity

from model.application import Application
from model.components.authorization import Authorization
from pages.apple_iphones import AppleIphonesSection
from pages.cart_menu import CartMenu
from pages.cart_page import CartPage
from pages.main_page import MainPage


@allure.label('owner', '@ms_izegov')
@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.feature('Смоук-тест: добавление в корзину')
@allure.story('Обычный юзер может выбрать товар согласно фильтрам и добавить в корзину')
@allure.link('https://example.com', name='see the task here')
def test_buy_product(browser):

    with allure.step('Открытие главной страницы'):
        app = Application(browser)
        app.open('https://telemarket24.ru/')

    with allure.step('Авторизация'):
        logging_in = Authorization(browser)
        logging_in.authorize()

    with allure.step('Переход в раздел смартфонов Apple'):
        mp = MainPage(browser)
        mp.move_to_apple_smartphones_section()

    with allure.step('Применение фильтров: выбор товара'):
        ai = AppleIphonesSection(browser)
        ai.select_product_according_to_filters()

    with allure.step('Проверка соответствия названия товара и цены'):
        cm = CartMenu(browser)
        cm.click_cart_icon_header()
        cm.save_product_name_in_cart_menu()
        cm.save_product_price_in_cart_menu()

        ai.compare_name_on_page_and_in_cart_menu()
        ai.compare_price_on_page_and_in_cart_menu()

    with allure.step('Проверка итоговой цены, переход на страницу корзины'):
        cm.check_total_and_create_order()

    with allure.step('Итоговый чекаут'):
        cp = CartPage(browser)
        cp.check_name_and_total_and_create_order()

    with allure.step('Чистка куков, удаление из корзины'):
        cp.remove_from_cart()
        browser.delete_all_cookies()
        browser.refresh()
