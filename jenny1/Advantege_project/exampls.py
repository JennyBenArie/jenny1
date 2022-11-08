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

driver.get("https://www.advantageonlineshopping.com/#/")

driver.maximize_window()
driver.implicitly_wait(10)
#
driver.find_element(By.CSS_SELECTOR, "[class='twoRows categoryCell']").click()

product_list = driver.find_elements(By.CSS_SELECTOR, "[class='productName ng-binding']")
product_list[2].click()
colors = driver.find_elements(By.CSS_SELECTOR, '[class="productColor ng-scope]')
colors[2].click()

# shopping_cart = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="ShoppingCart"]')
# ActionChains(driver).move_to_element(shopping_cart).perform()

sleep(2)

