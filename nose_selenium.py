import os
from unittest2 import TestCase

from nose.plugins import Plugin
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

BROWSER = None


class NoseSelenium(Plugin):

    name = 'simple-nose-selenium'

    def options(self, parser, env=os.environ):

        Plugin.options(self, parser, env)
        parser.add_option("--browser",
                          action="store",
                          default=env.get("SELENIUM_BROWSER", "FIREFOX"),
                          dest="browser",
                          help="Run this type of browser (default FIREFOX)" +
                            "Choices: [CHROME, FIREFOX]"
        )

    def configure(self, options, conf):
        Plugin.configure(self, options, conf)
        if self.enabled:
            self.ingest_options(options)
            self._check_options_validity(BROWSER, self._valid_browsers_for_local)

    def ingest_options(self, options):
        global BROWSER
        BROWSER = options.browser

    @property
    def _valid_browsers_for_local(self):
        return ["FIREFOX", "CHROME"]

    def _check_options_validity(self, item, list_options, flag="--browser"):
        if item not in list:
            raise TypeError(
                "{} not in available options for {}: {}".format(
                    item, flag, ",".join(list_options))
            )


def build_webdriver(name="", tags=[], public=False):
    """Create and return the desired WebDriver instance."""
    global BROWSER

    wd = None

    if BROWSER == "FIREFOX":
        wd = webdriver.Firefox()
    elif BROWSER == "CHROME":
        wd = webdriver.Chrome()
    else:
        raise TypeError(
            "WebDriver does not have a driver for local %s".format(BROWSER))

    # We give it a base implicty wait timeout
    wd.implicitly_wait(60)
    return wd


class SeleniumTestCase(TestCase):

    def setUp(self):
        self.wd = build_webdriver()

    def tearDown(self):
        self.wd.quit()

