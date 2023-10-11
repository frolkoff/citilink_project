from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base.base_class import Base




class Main_page(Base):

    url = 'https://www.citilink.ru/'
    url_after_auth = 'https://www.citilink.ru/?_action=login&_success_login=1'
    url_game_product_page = 'https://www.citilink.ru/catalog/igrovye-noutbuki/?ref=mainmenu'
    user_login = 'markfrolkoff@gmail.com'
    user_password = 10022008


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wb = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)


    # Locators

    open_auth_window_button = "//*[@id='__next']/div/div[3]/div/div[2]/div/div/div[2]/div[2]/div[1]/div/span"
    login = "//input[@name='login']"
    password = "//input[@name='pass']"
    login_button = "/html/body/div[5]/div/div/div/div/div[2]/div/div/div/form/div/button/span"
    catalog_button = '//div[@class="css-gbhtnj eyoh4ac0"]'
    product_for_gamers_title = '(//a[@data-meta-name="DesktopMenu__category--menu-item"])[20]'
    game_notebooks_link = '(//a[@data-meta-name="DesktopMenu__sub-sub-category"])[2]'


    # Getters

    def get_open_auth_window_button(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.open_auth_window_button)))

    def get_login(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.login)))

    def get_password(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.login_button)))


    def get_catalog_button(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.catalog_button)))

    def get_product_for_gamers_title(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.product_for_gamers_title)))

    def get_game_notebooks_link(self):
        return self.wb.until(EC.element_to_be_clickable((By.XPATH, self.game_notebooks_link)))


    # Actions

    def click_get_open_auth_window_button(self):
        self.get_open_auth_window_button().click()
        print('Window to auth opened')

    def input_login(self, login):
        self.get_login().send_keys(login)
        print('Login was filled')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Password was filled')

    def click_login_button(self):
        self.get_login_button().click()
        print('Login button clicked')

    def click_catalog_button(self):
        self.get_catalog_button().click()
        print('Catalog button clicked')

    def hover_to_product_for_gamers_title(self):
        self.actions.move_to_element(self.get_product_for_gamers_title()).perform()
        print('Hover has done')

    def click_game_notebooks_link(self):
        self.get_game_notebooks_link().click()
        print('Game notebooks link clicked')


    # Methods

    def authorisation(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

        self.get_current_url()

        self.click_get_open_auth_window_button()
        self.input_login(self.user_login)
        self.input_password(self.user_password)
        self.click_login_button()
        self.assert_url(self.url_after_auth)



    def go_to_game_product_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_catalog_button()
        self.hover_to_product_for_gamers_title()
        self.click_game_notebooks_link()
        self.assert_url(self.url_game_product_page)
