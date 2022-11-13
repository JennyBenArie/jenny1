from selenium import webdriver
from selenium.webdriver.common.by import By


class Category_Page:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def choose_product(self, num:int):
        # click one of the products from the list by number of index
        product_list = self.driver.find_elements(By.CSS_SELECTOR, "[class='productName ng-binding']")
        product_list[num].click()


    def return_line_category(self, num):
        # list of the return line, find every item with index
        return self.driver.find_elements(By.CSS_SELECTOR, 'nav[class ="pages categoryDataFixedNav"]>a')[num]

    def click_return_line_category(self, num):
        # click the return line and insert the index to the function
        self.return_line_category(num).click()

    def category_title(self):
        # returns the title of the category
        return self.driver.find_element(By.CSS_SELECTOR, "[class='categoryTitle roboto-regular sticky ng-binding']").text




