import os
import time
import unittest

from python.common.selenium import Selenium, true

USERS = {
    'successfully': {'email': os.getenv('FB_EMAIL'), 'password': os.getenv('FB_PASSWORD')},
    'failed': {'email': os.getenv('FB_EMAIL'), 'password': 'XXXXXXXXXXX'},
    'not_exist': {'email': 'ed42cfb64291e4@gmail.com', 'password': 'XXXXXXXXXXX'},
    'not_cred': {'email': '', 'password': ''},
}


class ContiagoTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Selenium.launch({'headless': true(os.getenv('HEADLESS', True))})

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def loginServer(self, email, password):
        self.driver.get('http://136.243.36.97:2000')
        self.driver.find_element_by_name("email").send_keys(email)
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_xpath("//button[@type='submit'][contains(.,'Login')]").click()

    def test_loginServer__failed_wrong_credentials(self):
        self.loginServer(**USERS['failed'])
        time.sleep(5)
        assert 'Falsche Anmeldeinformationen' in self.driver.page_source

    def test_loginServer__failed_user_not_exist(self):
        self.loginServer(**USERS['not_exist'])
        time.sleep(5)
        assert 'Falsche Anmeldeinformationen' in self.driver.page_source

    def test_loginServer__successfully(self):
        self.loginServer(**USERS['successfully'])
        time.sleep(5)
        assert 'Überblick über alle Kanäle.' in self.driver.page_source

        # def test_loginServer__not_cred(self):
    #     self.loginServer(**USERS['not_cred'])
    #     time.sleep(5)
    #     assert 'Wrong request format.' in self.driver.page_source

    def test_loginServer__logout_(self):
        self.test_loginServer__successfully()
        self.driver.find_element_by_xpath("//button[contains(.,'Abmelden')]").click()
        time.sleep(5)
        assert 'Login' in self.driver.page_source


if __name__ == '__main__':
    unittest.main()