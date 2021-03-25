import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):
    # set up will run before each test
    def setUp(self):
        # initialize driver with path to chrome driver in my personal environment
        self.driver = webdriver.Chrome("/Users/cody/dev/practice/selenium-trial/chromedriver 2")
        # opens web page
        self.driver.get("http://www.python.org")

    # tear down will run after each test
    def tearDown(self):
        # close web page
        self.driver.quit()
