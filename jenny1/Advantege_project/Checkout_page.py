from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Checkout_Page:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_registration_button(self):
        return self.driver.find_element(By.ID, "registration_btnundefined").click()

    def send_account_details(self,username:str, userEmail:str, userPassword:str):
        self.driver.find_element(By.NAME, "usernameRegisterPage").send_keys(username)
        self.driver.find_element(By.NAME, "emailRegisterPage").send_keys(userEmail)
        self.driver.find_element(By.NAME, "passwordRegisterPage").send_keys(userPassword)
        self.driver.find_element(By.NAME, "confirm_passwordRegisterPage").send_keys(userPassword)

    def click_i_agree_button(self):
        self.driver.find_element(By.NAME, "i_agree").click()

    def click_end_registration(self):
        self.driver.find_element(By.ID, "register_btnundefined").click()

    def click_next_button(self):
        self.driver.find_element(By.ID, "next_btn").click()

    def send_safepay_details(self, details:str):
        self.driver.find_element(By.NAME, "safepay_username").send_keys(details)
        self.driver.find_element(By.NAME, "safepay_password").send_keys(details)

    def click_pay_now_safepay(self):
        self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY").click()

    def succses_payment(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[class="roboto-regular ng-binding"]').text

    def my_orders(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div[id="loginMiniTitle"] label[class="option ng-scope"]')

    def orderd_product_number(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[class="left ng-binding"]').text

    def username_and_password_input(self,username:str,password:str):
        self.driver.find_element(By.NAME, "usernameInOrderPayment").send_keys(username)
        self.driver.find_element(By.NAME,"passwordInOrderPayment").send_keys(password)

    def click_mastercredit(self):
        self.driver.find_element(By.NAME, "masterCredit").click()

    def click_edit(self):
        self.driver.find_element(By.CLASS_NAME, "edit  ng-scope").click()

    def input_credit_number(self,credit:int):
        self.driver.find_element(By.ID, "creditCard").send_keys(credit)

    def input_cvv_number(self,cvv:int):
        self.driver.find_element(By.NAME, "cvv_number").send_keys(cvv)

    def input_cardholder_name(self,name:str):
        self.driver.find_element(By.NAME, "cardholder_name").send_keys(name)

    def click_pay_now_credit(self):
        self.driver.find_element(By.ID, "pay_now_btn_MasterCredit").click()

    def click_login(self):
        self.driver.find_element(By.ID, "login_btnundefined").click()

