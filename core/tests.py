from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.
class GeneralFunctionalTests(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_navigate_site(self):
        self.browser.get('http://127.0.0.1:8000/')
        assert 'Django' in self.browser.title

class LoginTest(LiveServerTestCase):
  def testLogin(self):
    selenium = webdriver.Chrome()
    selenium.get('http://127.0.0.1:8000/')
    username = selenium.find_elements_by_class_name("username")
    password = selenium.find_elements_by_class_name("password")
    submit = selenium.find_element_by_id('loginsubmit')
    username.send_keys('admin@email.com')
    password.send_keys('admin1')
    submit.send_keys(Keys.RETURN)