from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Home_page import Home_Page
from Category_Page import Category_Page
from Product_page import Product_Page
from selenium.webdriver.chrome.service import Service
from time import sleep
from Cart_page import Cart_page
from Checkout_page import Checkout_Page

class Test_AOS(TestCase):
    def setUp(self):
        service_chrome = Service(r"C:\game_cards-master\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service_chrome)
        self.driver.get("https://www.advantageonlineshopping.com/")
        self.home_page = Home_Page(self.driver)
        self.category_page = Category_Page(self.driver)
        self.product_page = Product_Page(self.driver)
        self.cart_page = Cart_page(self.driver)
        self.checkout_page = Checkout_Page(self.driver)
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    #targil1
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

    #targil2
    def test_products_info(self):
        self.home_page.click_headphones_category()
        self.category_page.choose_product(2)
        self.product_page.click_plus_product()
        self.product_page.click_add_to_cart()
        self.product_page.click_home_page()
        self.home_page.click_laptops_category()
        self.category_page.choose_product(1)
        self.product_page.click_add_to_cart()
        self.product_page.click_home_page()
        self.home_page.click_mice_category()
        self.category_page.choose_product(0)
        self.product_page.click_plus_product()
        self.product_page.click_plus_product()
        self.product_page.click_add_to_cart()
        self.product_page.mice_on_cart_window()
        #nametest
        self.assertEqual(self.product_page.product_name_in_cart(0), 'HP USB 3 BUTTON OPTICAL MOUSE')
        self.assertEqual(self.product_page.product_name_in_cart(1), 'HP CHROMEBOOK 14 G1(ES)')
        self.assertEqual(self.product_page.product_name_in_cart(2), 'HP H2310 IN-EAR HEADSET')
        #colortest
        self.assertEqual(self.product_page.product_color_cart_window(1), 'Color: BLACK')
        self.assertEqual(self.product_page.product_color_cart_window(3), 'Color: GRAY')
        self.assertEqual(self.product_page.product_color_cart_window(5), 'Color: BLACK')
        #QTYtest
        self.assertEqual(self.product_page.product_quantity_cart_window(0), 'QTY: 3')
        self.assertEqual(self.product_page.product_quantity_cart_window(2), 'QTY: 1')
        self.assertEqual(self.product_page.product_quantity_cart_window(4), 'QTY: 2')
        #pricetest
        self.assertEqual(self.product_page.product_price_cart_window(0), '$29.97')
        self.assertEqual(self.product_page.product_price_cart_window(1), '$1,261.99')
        self.assertEqual(self.product_page.product_price_cart_window(2), '$27.98')
        self.product_page.click_home_page()


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
        self.assertEqual(self.product_page.total_products().text,"(1 Item)")
        sleep(2)
        self.product_page.click_home_page()

    #targil4
    def test_shopping_cart_page(self):
        self.home_page.click_headphones_category()
        self.category_page.choose_product(2)
        self.product_page.click_add_to_cart()
        self.product_page.shopping_cart_window().click()
        self.assertEqual(self.product_page.shopping_cart_page().text, 'SHOPPING CART')
        self.product_page.click_home_page()

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
        print(f"product 1: {self.cart_page.product_name_cart(0)},quantity: {self.cart_page.product_quantity_in_cart_text(0)},price: {self.cart_page.product_price_in_cart(0)}")
        print(f"product 2: {self.cart_page.product_name_cart(1)},quantity: {self.cart_page.product_quantity_in_cart_text(1)},price: {self.cart_page.product_price_in_cart(1)}")
        print(f"product 3: {self.cart_page.product_name_cart(2)},quantity: {self.cart_page.product_quantity_in_cart_text(2)},price: {self.cart_page.product_price_in_cart(2)}")
        self.product_page.click_home_page()

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
        self.wait.until(EC.visibility_of_element_located(self.cart_page.edit_button()))
        self.cart_page.click_edit_button(0)
        self.cart_page.click_minus_product()
        self.product_page.click_add_to_cart()
        self.wait.until(EC.visibility_of_element_located(self.cart_page.edit_button()))
        self.cart_page.click_edit_button(1)
        self.cart_page.click_plus_button()
        self.product_page.click_add_to_cart()
        self.wait.until(EC.visibility_of_element_located(self.cart_page.edit_button()))
        self.assertEqual(self.cart_page.product_quantity_in_cart_text(0), 2)
        self.assertEqual(self.cart_page.product_quantity_in_cart_text(1), 3)
        self.product_page.click_home_page()

    #targil7
    def test_tablet_return(self):
        self.home_page.click_tablets_category()
        self.category_page.choose_product(1)
        self.product_page.click_return_line(1)
        self.assertEqual(self.category_page.category_title(), 'TABLETS')
        self.category_page.click_return_line_category(0)
        self.assertEqual(self.home_page.special_offer(), 'SPECIAL OFFER')

    #targil8
    def test_new_user(self):
        self.home_page.click_mice_category()
        self.category_page.choose_product(0)
        self.product_page.click_add_to_cart()
        self.product_page.click_checkout_from_window()
        self.checkout_page.click_registration_button()
        self.checkout_page.send_account_details('jbathebesr', 'jenybena01@gmail.com', '123Ab')
        self.checkout_page.click_i_agree_button()
        self.checkout_page.click_end_registration()
        self.wait.until(EC.visibility_of_element_located((By.ID, "userCart")))
        self.checkout_page.click_next_button()
        self.checkout_page.send_safepay_details('Abcd123')
        self.checkout_page.click_pay_now()
        self.assertEqual(self.checkout_page.succses_payment(), 'Thank you for buying with Advantage')








