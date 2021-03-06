import os
import time
import unittest

from python.common.selenium import Selenium, true

USERS = {
    'emails': {'email': ['anna.kernozhytskaya@codex-soft.com',
               'AnnA.kerNoZytskAya@coDex-soFt.com', 'ed42cfb64291e4@gmail.com', '']},
    'passwords': {'password': ['codex123', 'XXXXXXXXXXX', '']},
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

    def suc_log(self):
        self.loginShop(USERS['emails']['email'][0], USERS['passwords']['password'][0])
        time.sleep(5)
        menu = self.driver.find_element_by_xpath("(.//*[normalize-space(text())"
                                                 " and normalize-space(.)='Rechtliches'])"
                                                 "[1]/following::p[1]")
        menu.click()

    def test_loginShop__failed_wrong_credentials(self):
        self.loginShop(USERS['emails']['email'][0], USERS['passwords']['password'][1])
        time.sleep(5)
        assert 'Das eingegebene Kennwort ist falsch' in self.driver.page_source

    def test_loginShop__not_cred(self):
        self.loginShop(USERS['emails']['email'][3], USERS['passwords']['password'][2])
        time.sleep(5)
        assert 'Wrong request format.' in self.driver.page_source

    def test_loginShop__failed_user_not_exist(self):
        self.loginShop(USERS['emails']['email'][2], USERS['passwords']['password'][1])
        time.sleep(5)
        assert 'Ein Benutzer mit dieser E-Mail ist nicht registriert' in self.driver.page_source

    def test_loginShop__successfully(self):
        self.suc_log()
        time.sleep(5)
        elem_menu = self.driver.find_element_by_xpath("(.//*[normalize-space(text())"
                                                      " and normalize-space(.)='Rechtliches'])"
                                                      "[1]/following::div[4]")
        self.assertIsNot(elem_menu, self.driver.page_source)

    def test_loginShop__logout_(self):
        self.suc_log()
        self.driver.find_element_by_xpath("(.//*[normalize-space(text())"
                                          " and normalize-space(.)='Rechtliches'])"
                                          "[1]/following::span[1]").click()
        time.sleep(5)
        assert 'Anmelden' in self.driver.page_source


if __name__ == '__main__':
    unittest.main()