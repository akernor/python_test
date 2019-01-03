import os
import time
import unittest

from python.common.selenium import Selenium, true

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
        versions = self.driver.find_elements_by_css_selector('button[class*="Button"]')
        for version in versions:
            if version.text == 'WEITER':
                version.click()
                break
        elements = self.driver.find_elements_by_css_selector('a[href="/Home"]')
        for element in elements:
            if element.text == 'Anmelden':
                element.click()
                break
        self.driver.find_element_by_name('email').send_keys(email)
        self.driver.find_element_by_name('password').send_keys(password)
        buttons = self.driver.find_elements_by_css_selector('button[type="submit"]')
        for button in buttons:
            if button.text == 'ANMELDEN':
                button.click()
                break

    def test_loginShop__failed_wrong_credentials(self):
        self.loginShop(**USERS['failed'])
        time.sleep(5)
        # self.assertTrue('Das eingegebene Kennwort ist falsch' in self.driver.page_source)
        assert 'Das eingegebene Kennwort ist falsch' in self.driver.page_source

    def test_loginShop__failed_user_not_exist(self):
        self.loginShop(**USERS['not_exist'])
        time.sleep(5)
        assert 'Ein Benutzer mit dieser E-Mail ist nicht registriert' in self.driver.page_source

    def test_loginShop__successfully(self):
        self.loginShop(**USERS['successfully'])
        time.sleep(5)
        # self.assertTrue('Anna Kernozhytskaya' in self.driver.page_source)
        assert 'Anna Kernozhytskaya' in self.driver.page_source


if __name__ == '__main__':
    unittest.main()