from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

PATH = "/Users/cody/dev/practice/selenium-trial/chromedriver 2"

driver = webdriver.Chrome(PATH)

driver.get("https://arcane-atoll-75350.herokuapp.com/")
log_in = driver.find_element_by_css_selector("ul.navbar-nav li:nth-child(2) div .nav-link")
log_in.click()

# time.sleep(2)
# driver.quit()
