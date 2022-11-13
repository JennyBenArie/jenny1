from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Cart_page:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def product_price_in_cart(self, num:int):
        pr = self.driver.find_elements(By.CSS_SELECTOR, "div[id='shoppingCart']>table>tbody>tr>td>p")[num].text
        tmp = ''
        for i in pr:
            if i.isalnum() or i == '.':
                tmp += i
        tmp = float(tmp)
        return tmp

    def product_quantity(self, num: int):
        return self.driver.find_elements(By.CSS_SELECTOR, 'div[id="shoppingCart"]>table>tbody>tr>td[class="smollCell quantityMobile"]>label[class="ng-binding"]')[num]

    def product_quantity_in_cart_text(self,num:int):
        q = self.driver.find_elements(By.CSS_SELECTOR, 'div[id="shoppingCart"]>table>tbody>tr>td[class="smollCell quantityMobile"]>label[class="ng-binding"]')[num].text
        q = int(q)
        return q

    def product_name_cart(self, num:int):
        return self.driver.find_elements(By.CSS_SELECTOR, "[class='roboto-regular productName ng-binding']")[num].text

    def cart_total_price(self):
        TP = self.driver.find_element(By.CSS_SELECTOR, 'div[id="shoppingCart"]>table>tfoot>tr>td>span[class="roboto-medium ng-binding"]').text
        tmp2 = ''
        for i in TP:
            if i.isalnum() or i == '.':
                tmp2 += i
        tmp2 = float(tmp2)
        return tmp2

    def edit_button(self, num:int):
        return self.driver.find_elements(By.LINK_TEXT, "EDIT")[num]

    def click_edit_button(self, num:int):
        self.edit_button(num).click()

    def minus_product(self):
        return self.driver.find_element(By.CLASS_NAME, "minus")

    def click_minus_product(self):
        self.minus_product().click()

    def plus_button(self):
        return self.driver.find_element(By.CLASS_NAME, "plus")

    def click_plus_button(self):
        self.plus_button().click()
