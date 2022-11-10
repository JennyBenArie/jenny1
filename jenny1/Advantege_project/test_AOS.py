from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Home_page import Home_Page
from Category_Page import Category_page
from Product_page import Product_Page
from selenium.webdriver.chrome.service import Service
from time import sleep
from Cart_page import Cart_page

class Test_AOS(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\game_cards-master\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service_chrome)
        self.driver.get("https://www.advantageonlineshopping.com/")
        self.home_page = Home_Page(self.driver)
        self.category_page = Category_page(self.driver)
        self.product_page = Product_Page(self.driver)
        self.cart_page = Cart_page(self.driver)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

# targil 1
    def test_add_product_to_cart_num(self):
         self.home_page.click_headphones_category()
         self.category_page.choose_product(2)
         self.product_page.click_plus_product()
         self.product_page.click_add_to_cart()
         self.product_page.click_home_page()
         self.home_page.click_laptops_category()
         self.category_page.choose_product(1)
         self.product_page.click_add_to_cart()
         self.assertEqual(self.product_page.number_of_products_in_cart().text, '3')
         self.product_page.click_home_page()

    def test_products_info(self):
        self.home_page.click_headphones_category()
        self.category_page.choose_product(2)
        self.product_page.click_plus_product()
        self.product_page.click_add_to_cart()
        self.product_page.click_home_page()
        self.home_page.click_laptops_category()
        self.category_page.choose_product(1)
        self.product_page.click_add_to_cart()
        self.home_page.click_mice_category()
        self.category_page.choose_product(0)
        self.product_page.click_plus_product()
        self.product_page.click_plus_product()

#targil3
    def test_product_remove(self):
        self.home_page.click_headphones_category()
        self.category_page.choose_product(2)
        self.product_page.click_add_to_cart()
        self.product_page.click_home_page()
        self.home_page.click_laptops_category()
        self.category_page.choose_product(1)
        self.product_page.click_add_to_cart()
        sleep(1)
        self.product_page.x_button().click()
        sleep(1)
        self.assertEqual(self.product_page.total_prodocts().text,"(1 Item)")
        sleep(2)
        self.product_page.click_home_page()

#targil4
    def test_shopping_cart_page(self):
        self.home_page.click_headphones_category()
        self.category_page.choose_product(2)
        self.product_page.click_add_to_cart()
        self.product_page.shopping_cart_window().click()
        sleep(2)
        self.assertEqual(self.product_page.shopping_cart_page().text, 'SHOPPING CART')
        sleep(2)

    #targil5
    def test_total_price(self):
        self.home_page.click_headphones_category()
        self.category_page.choose_product(2)
        self.product_page.click_add_to_cart()
        self.product_page.click_home_page()
        self.home_page.click_laptops_category()
        self.category_page.choose_product(1)
        self.product_page.click_plus_product()
        self.product_page.click_add_to_cart()
        self.product_page.click_home_page()
        self.home_page.click_mice_category()
        self.category_page.choose_product(0)
        self.product_page.click_plus_product()
        self.product_page.click_plus_product()
        self.product_page.click_add_to_cart()
        sleep(3)
        self.product_page.click_shopping_cart_window()
        ActionChains(self.driver).move_to_element(self.product_page.icon()).perform()
        sleep(5)
        pro1 = self.cart_page.product_price_in_cart(0)
        pro2 = self.cart_page.product_price_in_cart(1)
        pro3 = self.cart_page.product_price_in_cart(2)
        sum_pro = pro3+pro2+pro1
        sum_pro = round(sum_pro, 2)
        self.assertEqual(self.cart_page.cart_total_price(), sum_pro)
        print(f"product 1: {self.cart_page.product_name_cart(0)},quantity: {self.cart_page.product_quantity_in_cart(0)},price: {self.cart_page.product_price_in_cart(0)}")
        print(f"product 2: {self.cart_page.product_name_cart(1)},quantity: {self.cart_page.product_quantity_in_cart(1)},price: {self.cart_page.product_price_in_cart(1)}")
        print(f"product 3: {self.cart_page.product_name_cart(2)},quantity: {self.cart_page.product_quantity_in_cart(2)},price: {self.cart_page.product_price_in_cart(2)}")

    #targil6
    def test_change_cart(self):
        self.home_page.click_mice_category()
        self.category_page.choose_product(0)
        self.product_page.click_plus_product()
        self.product_page.click_plus_product()
        self.product_page.click_add_to_cart()
        self.product_page.click_home_page()
        self.home_page.click_laptops_category()
        self.category_page.choose_product(1)
        self.product_page.click_plus_product()
        self.product_page.click_add_to_cart()
        self.product_page.click_shopping_cart_window()
        ActionChains(self.driver).move_to_element(self.product_page.icon()).perform()
        sleep(5)
        self.cart_page.click_edit_button(0)
        self.cart_page.click_minus_product()
        self.product_page.click_add_to_cart()
        sleep(5)
        self.cart_page.click_edit_button(1)
        self.cart_page.click_plus_button()
        self.product_page.click_add_to_cart()
        sleep(5)
        self.assertEqual(self.cart_page.product_quantity_in_cart(0), 2)
        self.assertEqual(self.cart_page.product_quantity_in_cart(1), 3)

