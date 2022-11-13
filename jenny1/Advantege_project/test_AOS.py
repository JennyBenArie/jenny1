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
        # driver as aos site
        self.driver.get("https://www.advantageonlineshopping.com/")
        # objects from classes (Home_Page, Category_Page, Product_Page, Cart_Page, Checkout_Page)
        self.home_page = Home_Page(self.driver)
        self.category_page = Category_Page(self.driver)
        self.product_page = Product_Page(self.driver)
        self.cart_page = Cart_page(self.driver)
        self.checkout_page = Checkout_Page(self.driver)
        # wait 15 seconds until...
        self.wait = WebDriverWait(self.driver, 15)
        # open big window
        self.driver.maximize_window()
        # if something not working wait 15 seconds
        self.driver.implicitly_wait(15)

    # Targil 1 : tests if the quantity of the total products is currect.
    def test_add_product_to_cart_num(self):
        # choose the third product from the headphones category, add 2 quantities to the cart
         self.home_page.click_headphones_category()
         self.category_page.choose_product(2)
         self.product_page.click_plus_product()
         self.product_page.click_add_to_cart()
         # back to homepage
         self.product_page.click_home_page()
         #  choose the second product from laptops category and add 1 quantity to the cart.
         self.home_page.click_laptops_category()
         self.category_page.choose_product(1)
         self.product_page.click_add_to_cart()
         # check if the total quantity is 3.
         self.assertEqual(self.product_page.number_of_products_in_cart().text, '3')
         self.product_page.click_home_page()

    # Targil 2: tests if the product's details in the cart window is correct.
    def test_products_info(self):
        # choose the third product from the headphones category, add 2 quantities to the cart
        self.home_page.click_headphones_category()
        self.category_page.choose_product(2)
        self.product_page.click_plus_product()
        self.product_page.click_add_to_cart()
        # back to homepage
        self.product_page.click_home_page()
        #  choose the second product from laptops category and add 1 quantity to the cart.
        self.home_page.click_laptops_category()
        self.category_page.choose_product(1)
        self.product_page.click_add_to_cart()
        # back to homepage
        self.product_page.click_home_page()
        # choose the first product from the mice category and add 3 quantities to the cart
        self.home_page.click_mice_category()
        self.category_page.choose_product(0)
        self.product_page.click_plus_product()
        self.product_page.click_plus_product()
        self.product_page.click_add_to_cart()
        # put the mice on the cart window
        self.product_page.mice_on_cart_window()
        # tests if the names of the products are correct
        self.assertEqual(self.product_page.product_name_in_cart(0), 'HP USB 3 BUTTON OPTICAL MOUSE')
        self.assertEqual(self.product_page.product_name_in_cart(1), 'HP CHROMEBOOK 14 G1(ES)')
        self.assertEqual(self.product_page.product_name_in_cart(2), 'HP H2310 IN-EAR HEADSET')
        # tests if the colors of the product are correct
        self.assertEqual(self.product_page.product_color_cart_window(1), 'Color: BLACK')
        self.assertEqual(self.product_page.product_color_cart_window(3), 'Color: GRAY')
        self.assertEqual(self.product_page.product_color_cart_window(5), 'Color: BLACK')
        # tests if the quantities of the products are correct
        self.assertEqual(self.product_page.product_quantity_cart_window(0), 'QTY: 3')
        self.assertEqual(self.product_page.product_quantity_cart_window(2), 'QTY: 1')
        self.assertEqual(self.product_page.product_quantity_cart_window(4), 'QTY: 2')
        # tests if the prices of the products are correct
        self.assertEqual(self.product_page.product_price_cart_window(0), '$29.97')
        self.assertEqual(self.product_page.product_price_cart_window(1), '$1,261.99')
        self.assertEqual(self.product_page.product_price_cart_window(2), '$27.98')
        # back to homepage
        self.product_page.click_home_page()


    # Targil 3: tests if the remove of a product did happend
    def test_product_remove(self):
        # choose the third product from the headphones category, add 2 quantities to the cart
        self.home_page.click_headphones_category()
        self.category_page.choose_product(2)
        self.product_page.click_add_to_cart()
        # back to homepage
        self.product_page.click_home_page()
        # choose the second product from laptops category and add 1 quantity to the cart.
        self.home_page.click_laptops_category()
        self.category_page.choose_product(1)
        self.product_page.click_add_to_cart()
        # wait until the X button will show
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'[class="removeProduct iconCss iconX"]')))
        # remove the first product from the cart
        self.product_page.x_button().click()
        # check if there is only 1 item in the cart
        self.assertEqual(self.product_page.total_products().text, "(1 Item)")
        # back to homepage
        self.product_page.click_home_page()

    # Targil 4: tests if the shopping cart page is showen after adding products to cart
    def test_shopping_cart_page(self):
        # choose the third product from the headphones category, add 2 quantities to the cart
        self.home_page.click_headphones_category()
        self.category_page.choose_product(2)
        self.product_page.click_add_to_cart()
        # move to the shopping cart page
        self.product_page.shopping_cart_window().click()
        # check if the shopping cart page did raise
        self.assertEqual(self.product_page.shopping_cart_page().text, 'SHOPPING CART')
        # back to homepage
        self.product_page.click_home_page()

    # Targil 5: tests if after adding 3 types of products to the cart, the summery in the cart page is correct.
    # printing the products details at the end of the test.
    def test_total_price(self):
        # choose the third product from the headphones category, add 1 quantity  to the cart
        self.home_page.click_headphones_category()
        self.category_page.choose_product(2)
        self.product_page.click_add_to_cart()
        # back to homepage
        self.product_page.click_home_page()
        # choose the second product from laptops category and add 2 quantities to the cart.
        self.home_page.click_laptops_category()
        self.category_page.choose_product(1)
        self.product_page.click_plus_product()
        self.product_page.click_add_to_cart()
        # back to homepage
        self.product_page.click_home_page()
        # choose the first product from the mice category and add 3 quantities to the cart
        self.home_page.click_mice_category()
        self.category_page.choose_product(0)
        self.product_page.click_plus_product()
        self.product_page.click_plus_product()
        self.product_page.click_add_to_cart()
        # move to the shopping cart page
        self.product_page.click_shopping_cart_window()
        # move the mice to the username icon
        ActionChains(self.driver).move_to_element(self.product_page.icon()).perform()
        # wait until the all page is shown
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="roboto-light ng-scope"][translate="QUANTITY"]')))
        # sets every product price in a variable
        pro1 = self.cart_page.product_price_in_cart(0)
        pro2 = self.cart_page.product_price_in_cart(1)
        pro3 = self.cart_page.product_price_in_cart(2)
        # sum up the prices together
        sum_pro = pro3+pro2+pro1
        # round the number 2 after the point so it can be equal
        sum_pro = round(sum_pro, 2)
        # check if the total price is correct
        self.assertEqual(self.cart_page.cart_total_price(), sum_pro)
        # printing the products details
        print(f"product 1: {self.cart_page.product_name_cart(0)},quantity: {self.cart_page.product_quantity_in_cart_text(0)},price: {self.cart_page.product_price_in_cart(0)}")
        print(f"product 2: {self.cart_page.product_name_cart(1)},quantity: {self.cart_page.product_quantity_in_cart_text(1)},price: {self.cart_page.product_price_in_cart(1)}")
        print(f"product 3: {self.cart_page.product_name_cart(2)},quantity: {self.cart_page.product_quantity_in_cart_text(2)},price: {self.cart_page.product_price_in_cart(2)}")
        # back to homepage
        self.product_page.click_home_page()

    # Targil 6: edit products in the cart page and check if it is correct at the shopping cart page.
    def test_change_cart(self):
        # choose the third product from the headphones category, add 3 quantities to the cart
        self.home_page.click_mice_category()
        self.category_page.choose_product(0)
        self.product_page.click_plus_product()
        self.product_page.click_plus_product()
        self.product_page.click_add_to_cart()
        # back to homepage
        self.product_page.click_home_page()
        # choose the second product from laptops category and add 2 quantities to the cart.
        self.home_page.click_laptops_category()
        self.category_page.choose_product(1)
        self.product_page.click_plus_product()
        self.product_page.click_add_to_cart()
        # get in the shopping cart page
        self.product_page.click_shopping_cart_window()
        # move the mice to the username icon
        ActionChains(self.driver).move_to_element(self.product_page.icon()).perform()
        self.wait.until(EC.visibility_of_all_elements_located((By.LINK_TEXT, "EDIT")))
        sleep(4)
        # minus 1 quantity from the last product that added
        self.cart_page.click_edit_button(0)
        self.cart_page.click_minus_product()
        self.product_page.click_add_to_cart()
        self.wait.until(EC.visibility_of_all_elements_located((By.LINK_TEXT, "EDIT")))
        sleep(4)
        # plus 1 quantity from the second product that added
        self.cart_page.click_edit_button(1)
        self.cart_page.click_plus_button()
        self.product_page.click_add_to_cart()
        self.wait.until(EC.visibility_of_all_elements_located((By.LINK_TEXT, "EDIT")))
        sleep(4)
        # check if there is 2 headphones and 3 laptops
        self.assertEqual(self.cart_page.product_quantity_in_cart_text(0), 2)
        self.assertEqual(self.cart_page.product_quantity_in_cart_text(1), 3)
        # go back to homepage
        self.product_page.click_home_page()

    # Targil 7: choose product from Tablet category and then go back to the tablet category, and to the home page.
    def test_tablet_return(self):
        # choose the second product from the tablet category
        self.home_page.click_tablets_category()
        self.category_page.choose_product(1)
        # click the second item(TABLETS) in the return line
        self.product_page.click_return_line(1)
        # check if the page is the tablet category
        self.assertEqual(self.category_page.category_title(), 'TABLETS')
        # press the first item (home page) in the return line
        self.category_page.click_return_line_category(0)
        # check if the page is home page
        self.assertEqual(self.home_page.special_offer(), 'SPECIAL OFFER')

    # Targil 8:
    def test_new_user(self):
        # choose the first product from the mice category and add 1 quantity to the cart
        self.home_page.click_mice_category()
        self.category_page.choose_product(0)
        self.product_page.click_add_to_cart()
        # checkout the order
        self.product_page.click_checkout_from_window()
        # creat new account
        self.checkout_page.click_registration_button()
        self.checkout_page.send_account_details('jennyariel', 'jenybena01@gmail.com', '123Ab')
        self.checkout_page.click_i_agree_button()
        self.checkout_page.click_end_registration()
        # wait until the page will load
        self.wait.until(EC.visibility_of_element_located((By.ID, "userCart")))
        # pay with Safepay
        self.checkout_page.click_next_button()
        self.checkout_page.send_safepay_details('Abcd123')
        self.checkout_page.click_pay_now_safepay()
        # self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="roboto-regular ng-binding"]')))
        # paynow button check
        self.assert_(self.checkout_page.click_pay_now_safepay(), "paynow button did not clicked.")
        # check if the order completed
        self.assertIn(self.checkout_page.succses_payment(), 'Your order number is')
        # check if the order is in the orders list
        order_number = self.driver.find_element(By.ID, "orderNumberLabel").text
        self.product_page.icon().click()
        self.checkout_page.my_orders().click()
        self.assertIn(self.checkout_page.orderd_product_number(), order_number)
        # go back to homepage
        self.product_page.click_home_page()

    # Targil 9: tests if you can pay with master credit
    def test_cradit_payment(self):
        # choose the first product from the laptops category and add it to the cart
        self.home_page.click_laptops_category()
        self.category_page.choose_product(0)
        self.product_page.click_add_to_cart()
        # checkout the order and login to exist account
        self.product_page.click_checkout_from_window()
        self.checkout_page.username_and_password_input('ariel123', 'Ariel1')
        self.checkout_page.click_login()
        # pay with mastercredit
        self.checkout_page.click_next_button()
        self.checkout_page.click_mastercredit()
        self.checkout_page.click_pay_now_credit()
        # remember order number
        order_number = self.driver.find_element(By.ID, "orderNumberLabel").text
        # move the mice to reach the cart window
        ActionChains(self.driver).move_to_element(self.product_page.shopping_cart_window()).perform()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="roboto-regular"]')))
        self.assertEqual(self.cart_page.items_number(), '(0)')
        # move the mice to click the username icon
        ActionChains(self.driver).move_to_element(self.product_page.icon()).perform()
        self.wait.until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="roboto-regular"]')))
        self.product_page.icon().click()
        self.checkout_page.my_orders().click()
        # check the if the order number exist in the orders list
        self.assertIn(self.checkout_page.orderd_product_number(), order_number)
        # go back to homepage
        self.product_page.click_home_page()

    # Targil 10: check loggin in and loggin out
    def test_login_logout(self):
        # login with exist user
        self.product_page.icon().click()
        self.home_page.login("ariel123", "Ariel1")
        self.home_page.click_sign_in()
        # check if the user icon contains the username
        self.assertEqual(self.home_page.icon_name(), "ariel123", "login sucsesful")
        # wait until there is an option to click the user icon
        # self.wait.until(EC.element_to_be_clickable((By.ID, "menuUserSVGPath")))
        sleep(4)
        # logout
        self.product_page.icon().click()
        self.home_page.click_sign_out()
        # check if the usericon is empty
        self.assertEqual(self.home_page.icon_no_name(), "", "logout sucssesful")











