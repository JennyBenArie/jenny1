from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Category_page:

    def __init__(self, driver: webdriver.chrome):
        self.driver = driver

    def choose_product(self, num:int):
        product_list = self.driver.find_elements(By.CSS_SELECTOR, "[class='productName ng-binding']")
        product_list[num].click()

    def shopping_cart(self):
        return self.driver.find_element(By.ID, "[id='menuCart']")

    def mice_on_cart(self):
        ActionChains(self.driver).move_to_element(self.shopping_cart()).perform()