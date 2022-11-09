from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Product_Page:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def add_to_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[name="save_to_cart"]')

    def click_add_to_cart(self):
        self.add_to_cart().click()

    def plus_product(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[class="plus"]')

    def click_plus_product(self):
        self.plus_product().click()

    def minus_product(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[class="minus disableBtn"]')

    def click_minus_product(self):
        self.minus_product().click()

    def quantity(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'input[name="quantity"]')

    def insert_quantity(self, num:int):
        self.quantity().click()
        self.quantity().send_keys(num)

    def home_page_back(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[translate="HOME"]')

    def click_home_page(self):
        self.home_page_back().click()

    def number_of_products_in_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[id="shoppingCartLink"]>[class="cart ng-binding"]')


    def x_button(self):
        return self.driver.find_element(By.CSS_SELECTOR,'[class="removeProduct iconCss iconX"]')

    def total_prodocts(self):
        return self.driver.find_element(By.CSS_SELECTOR,'[class="roboto-regular ng-binding"]')

    def shopping_cart(self):
        return self.driver.find_element(By.ID, "shoppingCartLink")

    def click_shopping_cart(self):
        self.shopping_cart().click()

    def mice_on_cart(self):
        ActionChains(self.driver).move_to_element(self.shopping_cart()).perform()

    def product_price(self):
        self.driver.find_element(By.CSS_SELECTOR, 'h2[class="roboto-thin screen768 ng-binding"]')

    def sum_price_products(self):
        self.product_price()*self.quantity()

    def shopping_cart_page(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'a[class="select  ng-binding"]')
