from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base


class Cart_page(Base):
    url_checkout_page = 'https://www.citilink.ru/order/checkout/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wb = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    # Locators

    first_product_in_cart_cost = '(//span[@class="e1j9birj0 e106ikdt0 css-175fskm e1gjr6xo0"])[1]'
    second_product_in_cart_cost = '(//span[@class="e1j9birj0 e106ikdt0 css-175fskm e1gjr6xo0"])[2]'
    sum_of_products_in_cart = '//span[@class="e1j9birj0 e106ikdt0 css-zmmgir e1gjr6xo0"]'
    go_to_checkout_page_button = '//button[@class="e4uhfkv0 css-ch34l1 e4mggex0"]'
    modal_window_about_changes_close_button = '//button[@class="e1nu7pom0 css-cmjyur e4mggex0"]'
    sum_of_products_value_on_checkout_page = '(//span[@class="e1j9birj0 e106ikdt0 css-175fskm e1gjr6xo0"])[2]'
    delete_first_product_from_cart = '(//div[@data-meta-name="DeleteAction"])[1]'
    delete_second_product_from_cart = '(//div[@data-meta-name="DeleteAction"])[2]'




    # Getters

    def get_first_product_in_cart_cost(self):
        return self.wb.until((EC.element_to_be_clickable((By.XPATH, self.first_product_in_cart_cost))))

    def get_second_product_in_cart_cost(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.second_product_in_cart_cost)))

    def get_sum_of_products_in_cart(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.sum_of_products_in_cart)))

    def get_go_to_checkout_page_button(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.go_to_checkout_page_button)))

    def get_modal_window_about_changes_close_button(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.modal_window_about_changes_close_button)))

    def get_sum_of_products_value_on_checkout_page(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.sum_of_products_value_on_checkout_page)))

    def get_delete_first_product_from_cart(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.delete_first_product_from_cart)))

    def get_delete_second_product_from_cart(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.delete_second_product_from_cart)))

    # Actions

    def first_product_in_cart_text(self):
        first_product_in_cart_value = int(self.get_first_product_in_cart_cost().text.replace(' ', ''))
        return first_product_in_cart_value

    def second_product_in_cart_text(self):
        second_product_in_cart_value = int(self.get_second_product_in_cart_cost().text.replace(' ', ''))
        return second_product_in_cart_value

    def sum_of_products_in_cart_text(self):
        get_sum_of_products_in_cart_value = int(self.get_sum_of_products_in_cart().text.replace(' ', ''))
        return get_sum_of_products_in_cart_value

    def sum_of_products_on_checkout_page(self):
        get_sum_of_products_on_checkout_page_value = int(self.get_sum_of_products_value_on_checkout_page().text.replace(' ', ''))
        return get_sum_of_products_on_checkout_page_value

    def click_modal_window_about_changes_close_button(self):
        try:
            self.get_modal_window_about_changes_close_button().click()
        except:
            pass

    def click_go_to_checkout_page_button(self):
        product_1 = self.first_product_in_cart_text()
        product_2 = self.second_product_in_cart_text()
        sum_of_products = product_1 + product_2
        print(f'Sum of products in cart: {sum_of_products}')

        self.get_go_to_checkout_page_button().click()
        print('Go to checkout page button clicked')
        self.click_modal_window_about_changes_close_button()
        self.assert_url(self.url_checkout_page)
        assert self.sum_of_products_on_checkout_page() == sum_of_products
        print('Complete cost assertion on checkout page')

    def click_delete_first_product_from_cart(self):
        self.get_delete_first_product_from_cart().click()
        print('First product deleted from cart')

    def click_delete_second_product_from_cart(self):
        self.get_delete_second_product_from_cart().click()
        print('Second product deleted from cart')


    # Methods

    def test_sum_of_products_in_cart(self):
        fact_sum_of_products_in_cart = self.first_product_in_cart_text() + self.second_product_in_cart_text()
        assert self.sum_of_products_in_cart_text() == fact_sum_of_products_in_cart
        print('Sum of products in cart is correct')
        self.click_go_to_checkout_page_button()

