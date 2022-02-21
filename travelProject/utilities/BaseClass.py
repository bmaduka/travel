
import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("loadUp")
class BaseClass:
    pass

    def JSE(self, text):
        self.driver.execute_script("arguments[0].click();", text)

    def waiter(self, locator, text):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located((locator, text)))

    def selector(self, locator, text):
        drop_down = Select(locator)
        drop_down.select_by_value(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('C:\\Users\\pc\\PycharmProjects\\travel_site\\travelProject\\reports\\info'
                                          '.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)  # logger report level
        return logger
