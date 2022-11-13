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

    def click_pay_now(self):
        self.driver.find_element(By.ID, "pay_now_btn_SAFEPAY").click()

    def succses_payment(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'div[id="orderPaymentSuccess"]>h2>span').text
