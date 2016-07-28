simple-nose-selenium
*************

A simple Selenium WebDriver plugin for nose.

This plugin is a python3 stripped down version of `nose-selenium <https://github.com/klrmn/nose-selenium>`_.

nosetests command line options
==============================

.. code-block:: bash

    $ nosetests --with-nose-selenium --help
    Usage: nosetests [options]

    Options:
      ...
      --with-nose-selenium  Enable plugin NoseSelenium: None
                            [NOSE_WITH_NOSE_SELENIUM]
      --browser=BROWSER     Run this type of browser (default ['FIREFOX'], options
                            for local [FIREFOX,  CHROME]

Example Commands
----------------

.. code-block:: bash

    $ nosetests --with-nose-selenium --browser=FIREFOX

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
