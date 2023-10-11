import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.cart_page import Cart_page


class Game_product_page(Cart_page):
    lenovo_title = 'lenovo'
    url_cart = 'https://www.citilink.ru/order/'
    search_request_second_product_name = 'Iphone Pro Max 15 256'
    url_iphone_page = 'https://www.citilink.ru/product/smartfon-apple-iphone-15-pro-max-a3108-256gb-goluboi-titan-3g-4g-2sim-1979447/?text=Iphone+Pro+Max+15+256'


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wb = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)


    # Locators

    sort_by_rating_button = "//button[@data-meta-value='rating']"
    search_filter = "//input[@data-meta-name='FilterSearch__input']"
    ok_button = "//button[@class='exponea-tooltip-btn']"
    lenovo_check_box = "//div[@class='eyyy4a70 app-catalog-1c39u95 e158ikld0']"
    first_product_add_to_cart_button = '(//button[@class="e1kkg8nh0 app-catalog-13w08en e4mggex0"])[1]'
    cart_button = '(//div[@data-meta-name="BasketButton"])[1]'
    first_product_cost = '(//span[@class="e1j9birj0 e106ikdt0 app-catalog-j8h82j e1gjr6xo0"])[1]'
    button_to_close_modal_window = '//button[@data-meta-name="UpsaleBasket__close-popup"]'
    search_request = '//input[@name="text"]'
    to_iphone_page_button = '(//div[@data-meta-name="InstantSearchMainResult__title"])[1]'


    # Getters

    def get_search_filter(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.search_filter)))

    def get_sort_by_rating_button(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.sort_by_rating_button)))

    def get_ok_button(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.ok_button)))

    def get_lenovo_check_box(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.lenovo_check_box)))

    def get_first_product_add_to_cart_button(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.first_product_add_to_cart_button)))

    def get_cart_button(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_first_product_cost(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.first_product_cost)))

    def get_button_to_close_modal_window(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.button_to_close_modal_window)))

    def get_search_request_input(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.search_request)))

    def get_to_iphone_page_button(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.to_iphone_page_button)))



    # Actions

    def click_sort_by_rating_button(self):
        self.get_sort_by_rating_button().click()
        print('Sort by rating button clicked')
        self.driver.execute_script('window.scrollTo(0, 500)')

    def input_search_filter(self):
        self.get_search_filter().send_keys(self.lenovo_title)
        print('Input search filter')

    def click_lenovo_check_box(self):
        self.get_lenovo_check_box().click()
        print('Lenovo check box clicked')
        self.driver.execute_script('window.scrollTo(0, -500)')

    def click_ok_button(self):
        try:
            self.get_ok_button().click()
        except TimeoutException:
            pass

    def click_first_product_add_to_cart(self):
        self.get_first_product_add_to_cart_button().click()
        print('First product add to cart button clicked')

    def click_cart_button(self):
        self.get_cart_button().click()
        print('Cart button clicked')

    def read_first_product_cost_value(self):
        self.get_first_product_cost()

    def click_button_to_close_modal_window(self):
        try:
            self.get_button_to_close_modal_window().click()
            print('Close modal window button clicked')
        except:
            pass

    def first_product_cost_text(self):
        first_product_value = self.get_first_product_cost().text.replace(' ', '')
        int_first_product_value = int(first_product_value)
        return int_first_product_value

    def assertion_prices_first_product(self):
        first_product_price_on_products_page = int(self.get_first_product_cost().text.replace(' ', ''))
        print(first_product_price_on_products_page)

        self.click_cart_button()
        self.assert_url(self.url_cart)

        first_product_price_on_cart_page = int(self.get_first_product_in_cart_cost().text.replace(' ', ''))
        print(first_product_price_on_cart_page)

        assert first_product_price_on_products_page == first_product_price_on_cart_page
        print('Complete cost assertion')
        self.driver.back()

    def input_search_request(self):
        self.get_search_request_input().send_keys(self.search_request_second_product_name)
        print('Second name of product has filled')
        time.sleep(2)

    def click_to_iphone_page_button(self):
        self.get_to_iphone_page_button().click()
        print('Go to iphone page button clicked')


    # Methods

    def choice_product_with_filters(self):
        self.click_ok_button()
        self.click_sort_by_rating_button()
        self.input_search_filter()
        self.click_ok_button()
        self.click_lenovo_check_box()
        self.click_first_product_add_to_cart()
        self.click_button_to_close_modal_window()
        self.assertion_prices_first_product()
        self.input_search_request()
        self.click_to_iphone_page_button()
        self.assert_url(self.url_iphone_page)


