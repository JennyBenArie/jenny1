from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Home_Page:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def speakers_category(self):
        # returns speakers category
        return self.driver.find_element(By.CSS_SELECTOR, "[class='SpeakersImg categoryCell']")

    def click_speakers_category(self):
        # click speakers category
        self.speakers_category().click()

    def tablets_category(self):
        # returns tablets category
        return self.driver.find_element(By.CSS_SELECTOR, '[class="categoryCell"]')

    def click_tablets_category(self):
        # click tablets category
        self.tablets_category().click()

    def laptops_category(self):
        # returns leptops category
        return self.driver.find_element(By.CSS_SELECTOR, "[class='laptopImg categoryCell']")

    def click_laptops_category(self):
        # click leptops category
        self.laptops_category().click()

    def mice_category(self):
        # returns mice category
        return self.driver.find_element(By.CSS_SELECTOR, "[class='miceImg categoryCell']")

    def click_mice_category(self):
        # click mice category
        self.mice_category().click()

    def headphones_category(self):
        # returns headphones category
        return self.driver.find_element(By.CSS_SELECTOR, "[class='twoRows categoryCell']")

    def click_headphones_category(self):
        # click headphones category
        self.headphones_category().click()

    def special_offer(self):
        # returns the text of the special offer in the home page
        return self.driver.find_element(By.CSS_SELECTOR, "article[id='special_offer_items'] h3").text

    def login(self, username:str, password:str):
        # insert the details to the login window the website
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)

    def click_sign_in(self):
        # click on the sing in button
        self.driver.find_element(By.ID, "sign_in_btnundefined").click()

    def icon_name(self):
        # returns the name above the username icon
        return self.driver.find_element(By.CSS_SELECTOR, "[class='hi-user containMiniTitle ng-binding']").text

    def icon_no_name(self):
        # returns the text from the unlogged user icon
        return self.driver.find_element(By.CSS_SELECTOR, "[class ='hi-user containMiniTitle ng-binding ng-hide']").text

    def click_sign_out(self):
        # click the sign out button
        self.driver.find_element(By.CSS_SELECTOR, 'label[class="option roboto-medium ng-scope"][translate="Sign_out"]').click()









