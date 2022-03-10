

import chromedriver_binary
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


@pytest.mark.smoke
class TestHoliday3(BaseClass):
    def test_holiday3(self):
        driver = self.driver
        driver.get("https://www.expedia.co.uk/")
        driver.find_element(By.XPATH, "//button[contains(@class, 'osano-cm-denyAll')]").click()
        driver.find_element(By.XPATH, "//span[contains(text(), 'Things to do')]").click()
        driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Things to do')]").click()
        x = driver.find_element(By.ID, "location-field-location")
        x.send_keys("Barcelona")
        x.send_keys(Keys.ENTER)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]").click()

        driver.quit()

