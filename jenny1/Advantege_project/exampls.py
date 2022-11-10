from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from Category_Page import Category_page
from Product_page import Product_Page

service_chrome = Service(r"C:\game_cards-master\chromedriver.exe")

driver = webdriver.Chrome(service=service_chrome)

driver.get("https://www.advantageonlineshopping.com/")

driver.maximize_window()
driver.implicitly_wait(10)

# shopping_cart = driver.find_element(By.ID, "shoppingCartLink")
# shopping_cart.click()
# sleep(2)
# ActionChains(driver).move_to_element(shopping_cart).perform()
driver.find_element(By.CSS_SELECTOR, "[class='miceImg categoryCell']").click()
product = Category_page(driver)
product.choose_product(0)
driver.find_element(By.CSS_SELECTOR, '[name="save_to_cart"]').click()
driver.find_element(By.CSS_SELECTOR, '[translate="HOME"]').click()
driver.find_element(By.CSS_SELECTOR, "[class='miceImg categoryCell']").click()
product.choose_product(3)
driver.find_element(By.CSS_SELECTOR, '[name="save_to_cart"]').click()
sleep(5)
# pr = driver.find_element(By.CSS_SELECTOR, 'h2[class="roboto-thin screen768 ng-binding"]').text
#
# q = driver.find_element(By.CSS_SELECTOR, 'class="ng-valid ng-dirty ng-valid-parse ng-touched"')
# print(pr)
# print(q)
# sleep(6)
c = driver.find_elements(By.CSS_SELECTOR, "tbody>tr>td>a>label")
print(c[0].text)
pr = driver.find_elements(By.XPATH, '//table/tbody/tr/td/p')
print(pr[0].text)


