from selenium import webdriver
from selenium.webdriver.common.by import By

class Checkout_Page:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_registration_button(self):
        # click the registartion button
        return self.driver.find_element(By.ID, "registration_btnundefined").click()

    def send_account_details(self,username:str, userEmail:str, userPassword:str):
        # insert to a new account details (username, email, password, confirm password)
        self.driver.find_element(By.NAME, "usernameRegisterPage").send_keys(username)
        self.driver.find_element(By.NAME, "emailRegisterPage").send_keys(userEmail)
        self.driver.find_element(By.NAME, "passwordRegisterPage").send_keys(userPassword)
        self.driver.find_element(By.NAME, "confirm_passwordRegisterPage").send_keys(userPassword)

    def click_i_agree_button(self):
        # click the "I agree" button
        self.driver.find_element(By.NAME, "i_agree").click()

    def click_end_registration(self):
        # click and registration button
        self.driver.find_element(By.ID, "register_btnundefined").click()

    def click_next_button(self):
        # click the next button
        self.driver.find_element(By.ID, "next_btn").click()

    def send_safepay_details(self, details:str):
        # insert the SafePay details (username, password)
        self.driver.find_element(By.NAME, "safepay_username").send_keys(details)
        self.driver.find_element(By.NAME, "safepay_password").send_keys(details)

    def click_pay_now_safepay(self):
        # click the paynow after SafePay
        self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY").click()

    def succses_payment(self):
        #  returns the text from the succses payment page
        return self.driver.find_element(By.CSS_SELECTOR, '[class="roboto-regular ng-binding"]').text

    def my_orders(self):
        # returns my orders option from the user icon
        return self.driver.find_element(By.CSS_SELECTOR, 'div[id="loginMiniTitle"] label[class="option ng-scope"]')

    def orderd_product_number(self):
        # returns all the order's numbers
        return self.driver.find_element(By.CSS_SELECTOR, '[class="left ng-binding"]').text

    def username_and_password_input(self,username:str,password:str):
        # insert details to the login in the payment page (username, password)
        self.driver.find_element(By.NAME, "usernameInOrderPayment").send_keys(username)
        self.driver.find_element(By.NAME,"passwordInOrderPayment").send_keys(password)

    def click_mastercredit(self):
        # click the master credit option
        self.driver.find_element(By.NAME, "masterCredit").click()

    def click_pay_now_credit(self):
        # click the paynow with mastercredit option
        self.driver.find_element(By.ID, "pay_now_btn_MasterCredit").click()

    def click_login(self):
        # click login after insert details from payment page
        self.driver.find_element(By.ID, "login_btnundefined").click()

