from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Product_Page:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def add_to_cart(self):
        # returns add to cart button
        return self.driver.find_element(By.CSS_SELECTOR, '[name="save_to_cart"]')

    def click_add_to_cart(self):
        # click add to cart button
        self.add_to_cart().click()

    def plus_product(self):
        # returns plus product
        return self.driver.find_element(By.CSS_SELECTOR, '[class="plus"]')

    def click_plus_product(self):
        # click plus product
        self.plus_product().click()


    def icon(self):
        # returns the username icon
        return self.driver.find_element(By.ID, "menuUserSVGPath")

    def home_page_back(self):
        # returns the homepage going back button
        return self.driver.find_element(By.CSS_SELECTOR, '[translate="HOME"]')

    def click_home_page(self):
        # click the return home page
        self.home_page_back().click()

    def number_of_products_in_cart(self):
        # returns the number of products that is written above the cart icon
        return self.driver.find_element(By.CSS_SELECTOR, '[id="shoppingCartLink"]>[class="cart ng-binding"]')

    def x_button(self):
        # returns the X button from the shopping window
        return self.driver.find_element(By.CSS_SELECTOR,'[class="removeProduct iconCss iconX"]')

    def total_products(self):
        # quantity of the total products in the cart window
        return self.driver.find_element(By.CSS_SELECTOR, '[class="roboto-regular ng-binding"]')

    def shopping_cart_window(self):
        # returns the cart window
        return self.driver.find_element(By.ID, "menuCart")

    def click_shopping_cart_window(self):
        # click the cart window - gives you the shopping cart page
        self.shopping_cart_window().click()

    def mice_on_cart_window(self):
        # put the mice on the cart icon
        ActionChains(self.driver).move_to_element(self.shopping_cart_window()).perform()

    def product_price_cart_window(self, num:int):
        # list of each product prices in the cart window
        return self.driver.find_elements(By.CSS_SELECTOR, "[class='price roboto-regular ng-binding']")[num].text

    def product_quantity_cart_window(self, num:int):
        # list of each product quantity in the cart window
        # only num % 2 = 0
        return self.driver.find_elements(By.CSS_SELECTOR, 'label[class="ng-binding"]')[num].text

    def product_color_cart_window(self, num:int):
        # list of each product color in the cart window
        # only num % 2 != 0
        return self.driver.find_elements(By.CSS_SELECTOR, 'label[class="ng-binding"]')[num].text

    def product_name_in_cart(self, num):
        # list of the names of the products in the cart window
        return self.driver.find_elements(By.CSS_SELECTOR, 'table>tbody>tr>td>a>h3')[num].text

    def shopping_cart_page(self):
        # returns the shopping cart page
        return self.driver.find_element(By.CSS_SELECTOR, 'a[class="select  ng-binding"]')

    def return_line(self, num):
        # gives the return line from the product page
        return self.driver.find_elements(By.CSS_SELECTOR, 'nav[class="pages fixedImportant productImage ng-scope"]>a')[num]

    def click_return_line(self, num):
        # click the return line
        self.return_line(num).click()

    def click_checkout_from_window(self):
        # click checkout order from the cart window
        return self.driver.find_element(By.NAME, "check_out_btn").click()



