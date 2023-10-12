import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.cart_page import Cart_page


class Checkout_page(Cart_page):
    first_name = 'Mark'
    last_name = 'Frolkov'
    phone_number = '+79085017462'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wb = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    # Locators

    user_first_name = '//input[@name="contact-form_firstName"]'
    user_last_name = '//input[@name="contact-form_lastName"]'
    user_phone_number = '//input[@name="contact-form_phone"]'


    # Getters

    def get_user_first_name(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.user_first_name)))

    def get_user_last_name(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.user_last_name)))

    def get_user_phone_number(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.user_phone_number)))


    # Actions

    def input_user_first_name(self):
        self.get_user_first_name().clear()
        self.get_user_first_name().send_keys(self.first_name)
        print('First name inputted')

    def input_user_last_name(self):
        self.get_user_last_name().clear()
        self.get_user_last_name().send_keys(self.last_name)
        print('Last name inputted')

    def input_user_phone_number(self):
        self.get_user_phone_number().clear()
        self.get_user_phone_number().send_keys(self.phone_number)
        print('Phone number inputted')
        self.driver.back()



    # Methods

    def checkout_order(self):
        self.input_user_first_name()
        self.input_user_last_name()
        self.input_user_phone_number()
        self.click_delete_first_product_from_cart()
        self.click_delete_second_product_from_cart()

        time.sleep(2)


