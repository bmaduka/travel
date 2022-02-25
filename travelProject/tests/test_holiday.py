# !chromedriver_binary was installed by pip!

import pytest

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from TestData.HomePageData import HomePageData
from pageObjects.holidayPage import HolidayPage

from pageObjects.homePage import HomePage

from utilities.BaseClass import BaseClass


# import sys
# sys.path.append('/')


class TestHoliday(BaseClass):
    def test_holiday(self, getData):
        driver = self.driver
        log = self.getLogger()
        driver.get("https://www.onthebeach.co.uk/")
        homepage = HomePage(self.driver)
        holidaypage = HolidayPage(self.driver)
        try:
            setting = homepage.getSetting()
            self.JSE(setting)
            homepage.getRecset().click()
            close = homepage.getClose()
            self.JSE(close)
            log.info("cookie preference was selected")
        except:
            pass

        self.waiter(By.XPATH, "//input[@name='destination']")

        homepage.getDestination().send_keys(getData["destination"])

        homepage.getFlight().click()
        self.waiter(By.XPATH, "//section[@class='search-form']/div/section/div[2]/div/button")
        homepage.getCheckbx().send_keys(Keys.ENTER)
        self.waiter(By.XPATH, "//label[@for='search[departure_points]']")
        airports = homepage.getAirports()
        for airport in airports:

            if getData["homeAirport"] in airport.text:
                self.JSE(airport)

                break
        homepage.getDeparture_date().click()
        month = homepage.getMonth()
        while month.text != getData["month"]:
            nxt = homepage.get_nxt()
            self.JSE(nxt)

        dates = homepage.getDates()

        for date in dates:
            if getData["travelDate"] in date.text:
                self.JSE(date)

                break
        homepage.getSearch_fields().click()
        self.selector(homepage.getNights(), getData["nights"])
        driver.execute_script("document.getElementsByTagName('span')[75].click();")
        self.selector(homepage.getRoom(), getData["room"])
        self.selector(homepage.getChild(), getData["num_child"])
        self.selector(homepage.getInfant(), getData["num_inf"])
        self.selector(homepage.getAge(), getData["childAge"])
        homepage.getDestination().send_keys(getData["destination"])
        homepage.getHoliday_search().click()
        self.waiter(By.XPATH, "//div[@class='input-counter__quantity']")
        log.info("holiday search button clicked")
        num_bags = holidaypage.getNum_bags()
        while num_bags.text != "3":
            add_bag = holidaypage.getAdd_bag()
            self.JSE(add_bag)
            time.sleep(5)
            num_bags = holidaypage.getNum_bags()
        pages = holidaypage.getPages()
        for i in range(0, len(pages)):
            holidays = holidaypage.getHolidays()
            for holiday in holidays:
                if getData["holiday"] in holiday.text:
                    choice = holiday.find_element(By.XPATH,
                                                  "parent::section/parent::header/parent::div/section[2]/footer/div/a")
                    self.JSE(choice)
                    time.sleep(2)
                    break
            else:
                try:
                    nxt = holidaypage.getNxt()
                    self.JSE(nxt)
                    time.sleep(3)
                    continue
                except:
                    log.info("no match found!")
                    break

        time.sleep(3)
        holidaypage.getBasket().click()
        log.info("desired holiday was added to basket")

        try:
            holidaypage.getNotice().click()

        except:
            pass
        time.sleep(2)
        driver.execute_script("document.getElementsByTagName('button')[15].click();")

    @pytest.fixture(params=HomePageData.test_Data)
    def getData(self, request):
        return request.param
        # driver.save_screenshot('screen_shot.png')
