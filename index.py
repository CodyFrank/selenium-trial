import secrets
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

PATH = "/Users/cody/dev/practice/selenium-trial/chromedriver 2"

driver = webdriver.Chrome(PATH)
email = secrets.email
password = secrets.password

driver.get("https://arcane-atoll-75350.herokuapp.com/")
log_in = driver.find_element_by_css_selector("ul.navbar-nav li:nth-child(2) div .nav-link")
log_in.click()
email_field = driver.find_element_by_id("email")
password_field = driver.find_element_by_id("password")
email_field.send_keys(email)
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# time.sleep(2)
# driver.quit()
