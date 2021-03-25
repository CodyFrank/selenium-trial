import secrets
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

PATH = "/Users/cody/dev/practice/selenium-trial/chromedriver 2"

driver = webdriver.Chrome(PATH)
email = secrets.email
password = secrets.password

driver.get("https://arcane-atoll-75350.herokuapp.com/")
log_in = driver.find_element_by_css_selector("ul.navbar-nav li:nth-child(2) div .nav-link")
log_in.click()

try:
    email_field = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, "email"))
    )
    password_field = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((By.ID, "password"))
    )
    email_field.send_keys(email)
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    # time.sleep(5)
    # driver.quit()
except:
    driver.quit()
