

import chromedriver_binary
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


@pytest.mark.smoke
class TestHoliday2(BaseClass):
    def test_holiday2(self):
        self.driver.get("https://www.kayak.co.uk/")

        self.driver.find_element(By.XPATH, "//span[contains(text(),'No thanks')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(text(),'To?')]").click()

        x = self.driver.find_element(By.XPATH, "//input[@placeholder='To?']")
        x.send_keys("Bristol")
        x.send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, "//button[@aria-label='Search']").click()

        self.driver.find_element(By.XPATH, "//div[@aria-label='Close']").click()
        print(self.driver.title)

