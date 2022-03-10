
import time
import chromedriver_binary

from selenium import webdriver

import pytest

# from selenium.webdriver import firefox

# from selenium.webdriver.firefox import webdriver
# from selenium.webdriver.chrome import webdriver


driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope='class')
def loadUp(request):
    global driver

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--enable-popup-blocking")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore")
    # chrome_options.add_argument("headless")

    driver = webdriver.Chrome(options=chrome_options)
    # driver.get("https://www.onthebeach.co.uk/")
    driver.implicitly_wait(7)
    request.cls.driver = driver

    yield
    time.sleep(1)
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


# cmd -  pytest -k test_holiday --html=..\reports\report.html
'''
@pytest.fixture(scope="class")
def loadUp(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
    elif browser_name == "IE":
        print("IE driver")
    driver.get("https://www.onthebeach.co.uk/")
    driver.maximize_window()
    driver.implicitly_wait(7)
    request.cls.driver = driver
    yield
    driver.close()
'''
