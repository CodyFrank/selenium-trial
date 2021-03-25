from selenium.webdriver.common.by import By

'''
create classes that represent objects we want to find
'''


class MainPageLocators(object):
    # create a constant with how to locate each object
    LOG_IN_BUTTON = (By.CSS_SELECTOR, "ul.navbar-nav li:nth-child(2) div .nav-link")


class LogInPageLocators(object):
    LOG_IN_BUTTON = (By.CSS_SELECTOR, ".btn-dark")
