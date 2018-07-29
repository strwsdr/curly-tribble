import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time


class First(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_asos_price(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://www.asos.com/ru/men/")
        elem = WebDriverWait(driver, 10).until(lambda driver: driver.find_element(By.XPATH, "/html/body/section[1]/article/div[2]/ul/li[2]/a/img"))
        elem.click()
        time.sleep(5)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

