# !chromedriver_binary was installed by pip!
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from pageObjects.holidayPage import HolidayPage
from pageObjects.homePage import HomePage
from utilities.BaseClass import BaseClass


class TestHoliday(BaseClass):
    def test_holiday(self):
        driver = self.driver
        homepage = HomePage(self.driver)
        holidaypage = HolidayPage(self.driver)
        setting = homepage.getSetting()
        driver.execute_script("arguments[0].click();", setting)
        homepage.getRecset().click()
        close = homepage.getClose()
        driver.execute_script("arguments[0].click();", close)
        self.waiter(By.XPATH, "//input[@name='destination']")
        homepage.getDestination().send_keys("Barcelona")
        homepage.getFlight().click()
        self.waiter(By.XPATH, "//section[@class='search-form']/div/section/div[2]/div/button")
        homepage.getCheckbx().send_keys(Keys.ENTER)
        self.waiter(By.XPATH, "//label[@for='search[departure_points]']")
        airports = homepage.getAirports()
        for airport in airports:
            if "London Airports" in airport.text:
                driver.execute_script("arguments[0].click();", airport)
                break
        homepage.getDeparture_date().click()
        month = homepage.getMonth()
        while month.text != "April 2022":
            nxt = homepage.get_nxt()
            driver.execute_script("arguments[0].click();", nxt)
        dates = homepage.getDates()

        for date in dates:
            if "17" in date.text:
                driver.execute_script("arguments[0].click();", date)
                break
        homepage.getSearch_fields().click()
        self.selector(homepage.getNights(), "8-10")
        driver.execute_script("document.getElementsByTagName('span')[75].click();")
        self.selector(homepage.getRoom(), "2")
        self.selector(homepage.getChild(), "1")
        self.selector(homepage.getInfant(), "1")
        self.selector(homepage.getAge(), "10")
        homepage.getDestination().send_keys("Barcelona")
        homepage.getHoliday_search().click()
        self.waiter(By.XPATH, "//div[@class='input-counter__quantity']")
        num_bags = holidaypage.getNum_bags()
        while num_bags.text != "3":
            add_bag = holidaypage.getAdd_bag()
            driver.execute_script("arguments[0].click();", add_bag)
            time.sleep(5)
            num_bags = holidaypage.getNum_bags()
        pages = holidaypage.getPages()

        for i in range(0, len(pages)):
            holidays = holidaypage.getHolidays()
            for holiday in holidays:
                if "BCN" in holiday.text:
                    #choice = holiday.homepage().getChoice()
                    choice = holiday.find_element(By.XPATH,
                                                  "parent::section/parent::header/parent::div/section[2]/footer/div/a")
                    driver.execute_script("arguments[0].click();", choice)
                    time.sleep(3)
                    break
            else:
                try:
                    nxt = holidaypage.getNxt()
                    # nxt = driver.find_element(By.XPATH,
                    # "//div/button/span[@class='pagination__icon pagination__icon--right']")
                    driver.execute_script("arguments[0].click();", nxt)
                    time.sleep(3)
                    continue
                except:
                    break

        time.sleep(3)
        holidaypage.getBasket().click()

        try:
            holidaypage.getNotice().click()

        except:
            pass
        time.sleep(2)
        driver.execute_script("document.getElementsByTagName('button')[15].click();")
        # driver.save_screenshot('screen_shot.png')
