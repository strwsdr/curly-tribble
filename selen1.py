import unittest
import selenium.common.exceptions as EX
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class First(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_price(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)
        driver.get("https://www.laredoute.ru/")
        try:
            self.assertIn("La Redoute", driver.title)
            print("Pagename is correct!")
        except AssertionError:
            print("Pagename is incorrect!")
        driver.find_element(By.XPATH, '//*[@id="mmFRv4divMain"]/div[3]/ul/li[3]/a').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="ctl00_cphMain_ctl00_divInner982"]/div[2]/div/div[2]/div[1]/a[2]/img').click() #click on shirts image
        main_link = 'https://www.laredoute.ru/pplp/100/157938/244/cat-271.aspx'
        try:
            self.assertEqual(driver.current_url, main_link)
        except AssertionError:
            print("Wrong url is provided!")
            driver.get(main_link)
            time.sleep(1)
        prices = []
        pages = driver.find_elements(By.CLASS_NAME, "page")
        for x in pages:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            try:
                driver.execute_script(
                    "window.oldjQuery=window.jQuery;delete window.jQuery;delete window.$;window.oSend=XMLHttpRequest.prototype.send;XMLHttpRequest.prototype.send = function(){console.log('stopped ajax request', arguments)};")
                x.click()
                prices += driver.find_elements(By.CLASS_NAME, "final-price")
            except EX.StaleElementReferenceException:
                elem = WebDriverWait(driver, 10).until(EC.visibility_of(x))
                elem.click()
            time.sleep(3)
        print(len(prices))








    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

