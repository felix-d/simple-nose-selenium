simple-nose-selenium
*************

A simple Selenium WebDriver plugin for nose.

This plugin is a python3 only stripped down version of `nose-selenium <https://github.com/klrmn/nose-selenium>`_.

nosetests command line options
==============================

.. code-block:: bash

    $ nosetests --with-simple-nose-selenium --help
    Usage: nosetests [options]

    Options:
      ...
      --with-simple-nose-selenium   Enable plugin Simple Nose Selenium
      --browser=BROWSER             Run this type of browser (default ['FIREFOX'], options:
                                    [FIREFOX,  CHROME, SAUCELABS]

Example Commands
----------------

.. code-block:: bash

    $ nosetests --with-simple-nose-selenium --browser=FIREFOX


To run your tests on Saucelabs you need to set the required environment variables first.

.. code-block:: bash

    $ export SAUCELABS_USERNAME=foo
    $ export SAUCELABS_ACCESSKEY=123key
    $ export SAUCELABS_PLATFORM=windows
    $ export SAUCELABS_BROWSER_NAME=chrome
    $ export SAUCELABS_BROWSER_VERSION=4.1
    $ nosetests --with-simple-nose-selenium --browser=SAUCELABS


Inheriting from SeleniumTestCase
--------------------------------

SeleniumTestCase creates the webdriver and stores it in self.wd in its setUp()
and closes it in tearDown().

.. code-block:: python

    from nose_selenium import SeleniumTestCase


    class MyTestCase(SeleniumTestCase):

        def test_that_google_opens(self):
            self.wd.get("http://google.com")
            self.assertEqual(self.wd.title, "Google")
