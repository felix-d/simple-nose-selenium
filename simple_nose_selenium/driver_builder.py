from selenium import webdriver

from simple_nose_selenium.simple_nose_selenium import CHROME, FIREFOX, SAUCELABS
from simple_nose_selenium.saucelabs import SaucelabsDriverBuilder


class DriverBuilder(object):
    def __init__(self, browser):
        self.browser = browser

    def build(self):
        driver = None

        if self.browser == FIREFOX:
            driver = webdriver.Firefox()
        elif self.browser == CHROME:
            driver = webdriver.Chrome()
        elif self.browser == SAUCELABS:
            driver = SaucelabsDriverBuilder().build()

        return driver
