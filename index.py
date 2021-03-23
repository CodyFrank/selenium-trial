from selenium import webdriver
import time
PATH = "/Users/cody/dev/practice/selenium-trial/chromedriver 2"

driver = webdriver.Chrome(PATH)

driver.get("https://selenium-python.readthedocs.io/")
print(driver.title)
time.sleep(2)
driver.quit()
