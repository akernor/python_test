import unittest
import os
import time


from python.loginShop.test.shop import contiago_test as log
from python.common.selenium import Selenium, true


class ShopNoAuthorize(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Selenium.launch({'headless': true(os.getenv('HEADLESS', True))})

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def shopNoAuthorize(self):
        log.ContiagoTest.loginShop(self, email='', password='')
        bo = self.driver.find_element_by_xpath('//*[@id="app"]'
                                               '/div/div[3]/div/div[2]/form/div[3]/button[2]')
        bo.click()
        self.driver.find_element_by_xpath("(.//*[normalize-space(text())"
                                          " and normalize-space(.)='Merkzettel'])"
                                          "[1]/preceding::span[1]").click()
        self.closeModalWindow()
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[1]/div[2]').click()
        self.closeModalWindow()

    def closeModalWindow(self):
        button = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[2]'
                                                   '/div/button[2]')
        button.click()

    def feedDetais(self):
        

    def test_shopNoAuthorize__check(self):
        self.shopNoAuthorize()
        assert 'Anmelde' in self.driver.page_source






if __name__ == '__main__':
    unittest.main()