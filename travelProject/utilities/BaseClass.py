import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("loadUp")
class BaseClass:
    pass

    def waiter(self, locator, text):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located((locator, text)))

    def selector(self, locator, text):
        drop_down = Select(locator)
        drop_down.select_by_value(text)
