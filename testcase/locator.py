from selenium.webdriver.common.by import By

'''
create classes that represent objects we want to find
'''


class MainPageLocators(object):
    # create a constant with how to locate each object
    GO_BUTTON = (By.ID, "submit")


class SearchResultsPageLocators(object):
    pass
