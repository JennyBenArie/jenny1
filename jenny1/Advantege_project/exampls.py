from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

service_chrome = Service(r"C:\game_cards-master\chromedriver.exe")

driver = webdriver.Chrome(service=service_chrome)

driver.get("https://www.advantageonlineshopping.com/")

driver.maximize_window()
driver.implicitly_wait(10)

shopping_cart = driver.find_element(By.ID, "shoppingCartLink")
sleep(2)
ActionChains(driver).move_to_element(shopping_cart).perform()

sleep(6)

