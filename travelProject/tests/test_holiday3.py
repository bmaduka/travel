import time

import chromedriver_binary
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@pytest.mark.smoke
class TestHoliday3:
    def test_holiday3(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)

        driver.get("https://www.expedia.co.uk/")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(@class, 'osano-cm-denyAll')]").click()
        driver.find_element(By.XPATH, "//span[contains(text(), 'Things to do')]").click()
        driver.find_element(By.XPATH, "//button[contains(@aria-label, 'Things to do')]").click()
        x = driver.find_element(By.ID, "location-field-location")
        x.send_keys("Barcelona")
        x.send_keys(Keys.ENTER)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Search')]").click()
        time.sleep(3)
