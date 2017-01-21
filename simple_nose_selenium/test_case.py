from unittest2 import TestCase

from simple_nose_selenium.simple_nose_selenium import global_config, SAUCELABS
from simple_nose_selenium.driver_builder import DriverBuilder
from simple_nose_selenium.saucelabs import SaucelabsClient


class SeleniumTestCase(TestCase):

    def setUp(self):
        self.wd = DriverBuilder(global_config['browser']).build()
        self.wd.implicitly_wait(60)

    def tearDown(self):
        if global_config['browser'] == SAUCELABS:
            SaucelabsClient().update_success_status(self.wd)
        self.wd.quit()
