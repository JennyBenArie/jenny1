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

class Test_AOS(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\game_cards-master\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service_chrome)
        self.driver.get("https://www.advantageonlineshopping.com/")
        self.home_page = Home_Page(self.driver)
        self.category_page = Category_page(self.driver)
        self.product_page = Product_Page(self.driver)
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
        self.product_page.shopping_cart().click()
        sleep(2)
        self.assertEqual(self.product_page.shopping_cart_page().text, 'SHOPPING CART')
        sleep(2)

    def test_



