'''this test will check whether all products have a price
and whether the counter works correctly'''
import unittest
import selenium.common.exceptions as EX
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Laredoute(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        wait = WebDriverWait(self.driver, 10)

    def test_price(self):
        driver = self.driver
        driver.get("https://www.laredoute.ru/")             #go to the website
        try:                                                #check the website name in title
            self.assertIn("La Redoute", driver.title)
            print("Pagename is correct!")
        except AssertionError:
            print("Pagename is incorrect!")
        driver.find_element(By.XPATH,
        '//*[@id="mmFRv4divMain"]/div[3]/ul/li[3]/a').click()     #go to "men's clothes" category
        men_cl_link = "https://www.laredoute.ru/men_style.aspx"   #check the corectness of button and link (try-except with assert method)
        try:
            self.assertIn(men_cl_link, driver.current_url)
        except AssertionError:
            print("Wrong url is provided to men's clothes category!")
            driver.get(men_cl_link)
        driver.find_element(By.XPATH,
        '//*[@id="ctl00_cphMain_ctl00_divInner982"]/div[2]/div/div[2]/div[1]/a[2]/img').click()   #go to "men's shirts" category
        shirts_link = 'https://www.laredoute.ru/pplp/100/157938/244/cat-271.aspx'                 #check the corectness of button and link (try-except with assert method)
        try:
            self.assertIn(shirts_link, driver.current_url)
        except AssertionError:
            print("Wrong url is provided to men's shirts category!")
            driver.get(shirts_link)
        prices = []                                          #create an empty list to store values
        pages = driver.find_elements(By.CLASS_NAME, "page")  #find the whole list of page buttons
        for x in pages:                                      #iterate through each page and collect the items related to prices
            if x.is_displayed():  #if there is more than one page here
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                try:
                    driver.execute_script("window.oldjQuery=window.jQuery;delete"
                     +"window.jQuery;delete window.$;window.oSend=XMLHttpRequest.prototype.send;"
                     +"XMLHttpRequest.prototype.send = function()"+
                     "{console.log('stopped ajax request', arguments)};") #stop repeating AJAX requests
                    wait.until(EC.element_to_be_clickable)   #handle AJAX elements
                    x.click()
                    prices += driver.find_elements(By.CLASS_NAME, "final-price")
                except EX.StaleElementReferenceException:      #handle AJAX elements
                    elem = WebDriverWait(driver, 10).until(EC.visibility_of(x))
                    elem.click()
            else:                #if there only one page here
                prices += driver.find_elements(By.CLASS_NAME, "final-price")
        count_title = driver.find_element(By.XPATH,
        '//*[@id="plpFRdivMain"]/div[1]/div[4]/div[2]/span[1]') #find the product counter on the page
        if str(len(prices)) == count_title.text:  #if numbers is the same, the counter works correctly
            print("All is ok, the number of products on the page corresponds"
             +"to the counter!")
        else:
            print("There are differences in the quantity of goods and" +
             "the counter number!")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
