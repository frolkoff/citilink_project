from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.cart_page import Cart_page


class Iphone_page(Cart_page):
    url_cart = 'https://www.citilink.ru/order/'


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wb = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)


    # Locators

    iphone_price = '//span[@class="e1j9birj0 e106ikdt0 app-catalog-1f8xctp e1gjr6xo0"]'
    add_to_cart_button_on_iphone_page = '//button[@class="e11w80q30 e4uhfkv0 app-catalog-1lk9ql2 e4mggex0"]'
    cart_button = '(//div[@data-meta-name="BasketButton"])[1]'
    close_modal_window_button = '(//span[@class="css-1xdhyk6 e1hf2t4f0"])[5]'


    # Getters

    def get_iphone_price(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.iphone_price)))

    def get_add_to_cart_button_on_iphone_page(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button_on_iphone_page)))

    def get_cart_button(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_close_modal_window_button(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.close_modal_window_button)))


    # Actions

    def click_add_to_cart_button_on_iphone_page(self):
        self.get_add_to_cart_button_on_iphone_page().click()
        print('Cart button on iphone page clicked')

    def click_go_cart_button(self):
        self.get_cart_button().click()
        print('Cart button clicked')


    def click_button_to_close_modal_window(self):
        try:
            self.get_close_modal_window_button().click()
            print('Close modal window button clicked')
        except:
            pass

    def assertion_iphone_prices(self):
        second_product_price_on_iphone_page = int(self.get_iphone_price().text.replace(' ', ''))
        print(second_product_price_on_iphone_page)

        self.click_go_cart_button()
        self.assert_url(self.url_cart)

        second_product_price_cart_page = int(self.get_second_product_in_cart_cost().text.replace(' ', ''))
        print(second_product_price_cart_page)

        assert second_product_price_on_iphone_page == second_product_price_cart_page
        print('Complete cost assertion')


    # Methods

    def add_to_cart_iphone(self):
        self.click_add_to_cart_button_on_iphone_page()
        self.click_button_to_close_modal_window()
        self.assertion_iphone_prices()

