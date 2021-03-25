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

    '''
    any method that's name starts with test
    will run between set up and tear down. 
    set up and tear down will run each time
    example: * on file run * - 
    setUp -> test_one - > tearDown -> setUp  -> testTwo -> tearDown
    this is functionality of unittest
    '''

    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_found()

    # tear down will run after each test
    def tearDown(self):
        # close web page
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
