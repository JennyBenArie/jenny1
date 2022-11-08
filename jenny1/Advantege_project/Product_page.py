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
        return self.driver.find_element(By.NAME, '[name="save_to_cart"]')

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
        return self.driver.find_element(By.NAME, 'input[name="quantity"]')

    def insert_quantity(self, num:int):
        self.quantity().send_keys(num)

    def colors(self):
        return self.driver.find_element(By.)
