from locator import *
from element import BasePageElement


class EmailFieldElement(BasePageElement):
    locator = "email"


class PasswordFieldElement(BasePageElement):
    locator = "password"


# each webpage will have its own page class that inherits from BasePage
class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    # returns bool of whether or not the title matches expected title
    def is_title_matches(self):
        return "Shopping List" in self.driver.title

    def click_log_in_button(self):
        element = self.driver.find_element(*MainPageLocators.LOG_IN_BUTTON)
        element.click()


class LogInPage(BasePage):
    def click_log_in_button(self):
        element = self.driver.find_element(*LogInPageLocators.LOG_IN_BUTTON)
        element.click()


class HomePage(BasePage):
    def is_logged_in(self):
        return "Welcome Selenium" not in self.driver.page_source
