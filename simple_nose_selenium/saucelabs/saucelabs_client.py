from sauceclient import SauceClient

from simple_nose_selenium.util import get_environ


class SaucelabsClient(object):
    def __init__(self):
        username = get_environ('SAUCELABS_USERNAME')
        access_key = get_environ('SAUCELABS_ACCESSKEY')
        self.sauce_client = SauceClient(username, access_key)

    def update_success_status(self, driver):
        self.sauce_client.jobs.update_job(driver.session_id, passed=True)
