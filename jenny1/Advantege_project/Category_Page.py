from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Category_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def choose_product(self, num:int):
        product_list = self.driver.find_elements(By.CSS_SELECTOR, "[class='productName ng-binding']")
        product_list[num].click()

    def shopping_cart(self):
        return self.driver.find_element(By.ID, "shoppingCartLink")


    def mice_on_cart(self):
        ActionChains(self.driver).move_to_element(self.shopping_cart()).perform()

    def shopping_cart_page(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'a[class="select  ng-binding"]')

    def product_title(self):
        return self.driver.find_element(By.CLASS_NAME, "categoryTitle roboto-regular sticky ng-binding")

    def return_line_category(self, num):
        return self.driver.find_elements(By.CSS_SELECTOR, 'nav[class ="pages categoryDataFixedNav"]>a')[num]

    def click_return_line_category(self, num):
        self.return_line_category(num).click()

    def category_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='categoryTitle roboto-regular sticky ng-binding']").text




