import time

import chromedriver_binary
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@pytest.mark.smoke
class TestHoliday2:
    def test_holiday2(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)

        driver.get("https://www.kayak.co.uk/")
        time.sleep(2)
        driver.find_element(By.XPATH, "//span[contains(text(),'No thanks')]").click()
        driver.find_element(By.XPATH, "//div[contains(text(),'To?')]").click()
        '''
        action = ActionChains(driver)
        #action.move_to_element(driver.find_element(By.XPATH, "//div[contains(text(),'To?')]")).click().perform()
        action.move_to_element(y).click().perform()
        '''
        x = driver.find_element(By.XPATH, "//input[@placeholder='To?']")
        x.send_keys("Bristol")
        x.send_keys(Keys.ENTER)
        driver.find_element(By.XPATH, "//button[@aria-label='Search']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//div[@aria-label='Close']").click()
        print(driver.title)
        # results = driver.find_elements(By.XPATH, "//div[@class='resultInner']")
        # result.find_element(By.XPATH, "//div/div[2]/div/div[2]/div/div/div[2]/div[2]/div/div").click()

        time.sleep(3)
