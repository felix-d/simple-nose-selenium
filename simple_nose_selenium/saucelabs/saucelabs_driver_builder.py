from selenium import webdriver

from simple_nose_selenium.util import get_environ


class SaucelabsDriverBuilder(object):
    def __init__(self):
        self.username = get_environ('SAUCELABS_USERNAME')
        self.access_key = get_environ('SAUCELABS_ACCESSKEY')
        self.platform = get_environ('SAUCELABS_PLATFORM')
        self.browser_name = get_environ('SAUCELABS_BROWSER_NAME')
        self.version = get_environ('SAUCELABS_BROWSER_VERSION')

    def build(self):
        return webdriver.Remote(
            command_executor=self.saucelabs_command_executor(),
            desired_capabilities=self.saucelabs_desired_capabilities(),
        )

    def saucelabs_command_executor(self):
        return 'http://{username}:{accesskey}@ondemand.saucelabs.com:80/wd/hub'.format(
            username=self.username,
            accesskey=self.access_key,
        )

    def saucelabs_desired_capabilities(self):
        return {
            'platform': self.platform,
            'browserName': self.browser_name,
            'version': self.version,
        }

