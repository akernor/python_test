import os
import unittest

from selenium.webdriver.common.keys import Keys

from python3.common.selenium import Selenium, true

USERS = {
    'successfully': {'email': os.getenv('FB_EMAIL'), 'password': os.getenv('FB_PASSWORD')},
    'failed': {'email': os.getenv('FB_EMAIL'), 'password': 'XXXXXXXXXXX'},
    'not_exist': {'email': 'ed42cfb64291e4@gmail.com', 'password': 'XXXXXXXXXXX'},
}


class ContiagoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Selenium.launch({'headless': true(os.getenv('HEADLESS', True))})

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def loginShop(self, email, password):
        self.driver.get('http://136.243.36.97:3000')
        elements = self.driver.find_elements_by_css_selector('a[href="/Home"]')
        for element in elements:
            if element.text == 'Anmelden':
                element.click()
                break
        self.driver.find_element_by_name('email').send_keys(email)
        self.driver.find_element_by_name('password').send_keys(password)
        buttons = self.driver.find_elements_by_css_selector('button[type="submit"]')
        for button in buttons:
            if button.text == 'Anmelden':
                button.click()
                break
        errors = self.driver.find_elements_by_css_selector('p[class*="ErrorMessage"]')
        found = False
        for error in errors:
            if 'Bad credentials' in error.text:
                found = True
                break
        if not found:
            raise Exception("Test failed")

    def test_loginShop__failed_wrong_credentials(self):
        self.loginShop(**USERS['failed'])
        assert 'Bad credentials' in self.driver.page_source

    def test_loginShop__failed_user_not_exist(self):
        self.loginShop(**USERS['not_exist'])
        assert 'Bad credentials(user with this email is not registered)' in self.driver.page_source

if __name__ == '__main__':
        unittest.main()