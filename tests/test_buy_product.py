import time

from selenium import webdriver

from pages.cart_page import Cart_page
from pages.game_product_page import Game_product_page
from pages.iphone_page import Iphone_page
from pages.main_page import Main_page
from pages.checkout_page import Checkout_page


def test_buy_product_1():

    driver = webdriver.Chrome()

    mp = Main_page(driver)
    mp.authorisation()
    mp.go_to_game_product_page()

    gmp = Game_product_page(driver)
    gmp.choice_product_with_filters()

    ip = Iphone_page(driver)
    ip.add_to_cart_iphone()

    cp = Cart_page(driver)
    cp.test_sum_of_products_in_cart()


    chp = Checkout_page(driver)
    chp.checkout_order()

    time.sleep(2)







