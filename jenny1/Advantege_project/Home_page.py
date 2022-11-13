from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Home_Page:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def speakers_category(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='SpeakersImg categoryCell']")

    def click_speakers_category(self):
        self.speakers_category().click()

    def tablets_category(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[class="categoryCell"]')

    def click_tablets_category(self):
        self.tablets_category().click()

    def laptops_category(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='laptopImg categoryCell']")

    def click_laptops_category(self):
        self.laptops_category().click()

    def mice_category(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='miceImg categoryCell']")

    def click_mice_category(self):
        self.mice_category().click()

    def headphones_category(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='twoRows categoryCell']")

    def click_headphones_category(self):
        self.headphones_category().click()

    def shopping_cart(self):
        return self.driver.find_element(By.ID, "shoppingCartLink")

    def click_shopping_cart(self):
        self.shopping_cart().click()

    def mice_on_cart(self):
        ActionChains(self.driver).move_to_element(self.shopping_cart()).perform()

    def special_offer(self):
        return self.driver.find_element(By.CSS_SELECTOR, "article[id='special_offer_items'] h3").text






