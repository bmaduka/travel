import os.path
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

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(self):
        pytest_html = self.config.pluginmanager.getplugin("html")
        outcome = yield
        report = outcome.get_result()
        extra = getattr(report, "extra", [])
        if report.when == "call":
            # always add url to report
            extra.append(pytest_html.extras.url("https://www.expedia.co.uk/"))
            xfail = hasattr(report, "wasxfail")
            if (report.skipped and xfail) or (report.failed and not xfail):
                # only add additional html on failure
                report_directory = os.path.dirname(self.config.option.htmlpath)
                # file_name = str(int(round(time.time()*1000)))+".png"
                file_name = report.nodeid.replace("::", "_") + ".png"
                destinationFile = os.path.join(report_directory, file_name)
                self.driver.save_screenshot(destinationFile)
                if file_name:
                    html = '<div><img src = "%s" alt="screenshot" style="width:300px;height=200px"' 'onclick="window' \
                           '.open(this.src)" align="right"/></div>' % file_name
                    extra.append(pytest_html.extras.html(html))
            report.extra = extra

    def pytest_html_report_title(self):
        self.title = "Python Automation Report"
