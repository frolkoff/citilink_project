import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current url: {get_url}')

    """Method assertion url"""

    def assert_url(self, result_url):
        get_url = self.driver.current_url
        print(f'Current URL: {get_url}')
        assert get_url == result_url
        print('Url assertion was completed succesfully')



    """Method word assertion"""

    def assert_value(self, word, result_word):
        word_value = word.text
        assert word_value == result_word
        print('Complete word assertion')



    """Product cost assertion"""

    def product_cost_assertion(self, result_cost, cost_in_cart):

        print(f'result cost: {result_cost}\ncost in cart: {cost_in_cart}')
        assert result_cost == cost_in_cart

        print('Complete cost assertion')

