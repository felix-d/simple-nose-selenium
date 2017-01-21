import os

from nose.plugins import Plugin

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

global_config = dict()
CHROME = 'CHROME'
FIREFOX = 'FIREFOX'
SAUCELABS = 'SAUCELABS'
CHOICES = [CHROME, FIREFOX, SAUCELABS]



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
        global global_config
        super().configure(options, conf)
        if self.enabled:
            global_config['browser'] = options.browser
            self.check_options_validity(global_config['browser'], CHOICES)

    def check_options_validity(self, item, list_options, flag="--browser"):
        if item not in list_options:
            raise TypeError(
                "{} not in available options for {}: {}".format(
                    item, flag, ",".join(list_options))
            )

