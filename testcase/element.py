from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):

    # sets page element to value
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    # gets page elements value and returns it
    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(drivver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")
