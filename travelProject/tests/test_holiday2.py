import time

import chromedriver_binary
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


@pytest.mark.smoke
class TestHoliday2(BaseClass):
    def test_holiday2(self):
        self.driver.get("https://www.kayak.co.uk/")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//span[contains(text(),'No thanks')]").click()
        self.driver.find_element(By.XPATH, "//div[contains(text(),'To?')]").click()
        '''
        action = ActionChains(driver)
        #action.move_to_element(driver.find_element(By.XPATH, "//div[contains(text(),'To?')]")).click().perform()
        action.move_to_element(y).click().perform()
        '''
        x = self.driver.find_element(By.XPATH, "//input[@placeholder='To?']")
        x.send_keys("Bristol")
        x.send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, "//button[@aria-label='Search']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[@aria-label='Close']").click()
        print(self.driver.title)

        time.sleep(3)
