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
    def add_product_to_cart_num(self):
         self.home_page.click_headphones_category()
         self.category_page.choose_product(2)
         self.product_page.insert_quantity(5)
         self.product_page.click_add_to_cart()


