import unittest
from selenium import webdriver
import page
import secrets


class PythonOrgSearch(unittest.TestCase):
    # set up will run before each test
    def setUp(self):
        # initialize driver with path to chrome driver in my personal environment
        self.driver = webdriver.Chrome("/Users/cody/dev/practice/selenium-trial/chromedriver 2")
        # opens web page
        self.driver.get("https://arcane-atoll-75350.herokuapp.com/")

    '''
    any method that's name starts with test
    will run between set up and tear down. 
    set up and tear down will run each time
    example: * on file run * - 
    setUp -> test_one - > tearDown -> setUp  -> testTwo -> tearDown
    this is functionality of unittest
    '''

    def test_title_matches(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()

    def test_log_in(self):
        mainPage = page.MainPage(self.driver)
        mainPage.click_log_in_button()
        email_field_element = page.EmailFieldElement()
        email_field_element = secrets.email
        password_field_element = page.PasswordFieldElement()
        password_field_element = secrets.password
        logInPage = page.LogInPage(self.driver)
        logInPage.click_log_in_button()
        homePage = page.HomePage(self.driver)
        assert homePage.is_logged_in()

    # tear down will run after each test
    def tearDown(self):
        # close web page
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
