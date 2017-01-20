import os
from unittest2 import TestCase

from nose.plugins import Plugin
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


BROWSER = None
CHOICES = ['CHROME', 'FIREFOX', 'SAUCELABS']


class SimpleNoseSelenium(Plugin):
    name = 'simple-nose-selenium'

    def options(self, parser, env=os.environ):
        super().options(parser, env)
        parser.add_option(
            "--browser",
            action="store",
            default="FIREFOX",
            dest="browser",
            help=(
                "Run this type of browser (default FIREFOX)"
                "Choices: [{}]".format(', '.join(CHOICES))
            ),
        )


    def configure(self, options, conf):
        global BROWSER
        super().configure(options, conf)
        if self.enabled:
            BROWSER = options.browser
            self._check_options_validity(BROWSER, CHOICES)

    def _check_options_validity(self, item, list_options, flag="--browser"):
        if item not in list_options:
            raise TypeError(
                "{} not in available options for {}: {}".format(
                    item, flag, ",".join(list_options))
            )


def build_webdriver():
    global BROWSER

    wd = None

    if BROWSER == 'FIREFOX':
        wd = webdriver.Firefox()
    elif BROWSER == 'CHROME':
        wd = webdriver.Chrome()
    elif BROWSER == 'SAUCELABS':
        wd = webdriver.Remote(
            command_executor=saucelabs_command_executor(),
            desired_capabilities=saucelabs_desired_capabilities(),
        )
    else:
        raise TypeError("WebDriver does not have a driver for local {}".format(BROWSER))

    wd.implicitly_wait(60)
    return wd


def get_environ(var):
    env = os.environ.get(var, None)
    if env is None:
        raise TypeError('Environment variable {} needs to be set.'.format(var))
    return env


def saucelabs_command_executor():
    username = get_environ('SAUCELABS_USERNAME')
    accesskey = get_environ('SAUCELABS_ACCESSKEY')

    return 'http://{username}:{accesskey}@ondemand.saucelabs.com:80/wd/hub'.format(
        username=username,
        accesskey=accesskey,
    )


def saucelabs_desired_capabilities():
    platform = get_environ('SAUCELABS_PLATFORM')
    browser_name = get_environ('SAUCELABS_BROWSER_NAME')
    version = get_environ('SAUCELABS_BROWSER_VERSION')
    return {
        'platform': platform,
        'browserName': browser_name,
        'version': version,
    )


class SeleniumTestCase(TestCase):

    def setUp(self):
        self.wd = build_webdriver()

    def tearDown(self):
        self.wd.quit()

