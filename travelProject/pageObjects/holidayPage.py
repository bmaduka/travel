from selenium.webdriver.common.by import By


class HolidayPage:
    def __init__(self, driver):
        self.driver = driver

    num_bags = (By.XPATH, "//div[@class='input-counter__quantity']")
    add_bag = (By.XPATH, "//span[contains(@class,'icon--symbol-plus')]")
    pages = (By.XPATH, "//div[@class='pagination__page-number-wrapper']/button")
    holidays = (By.XPATH, "//section/h2[@class='holiday-finder-results__hotel-name']")
    choice = (By.XPATH, "parent::section/parent::header/parent::div/section[2]/footer/div/a")
    nxt_page = (By.XPATH, "//div/button/span[@class='pagination__icon pagination__icon--right']")
    basket = (By.XPATH, "//button[contains(@class,'button--primary button--push-down')]")
    notice = (By.XPATH, "//span[contains(@class,'notice__close')]")

    def getNum_bags(self):
        return self.driver.find_element(*HolidayPage.num_bags)

    def getAdd_bag(self):
        return self.driver.find_element(*HolidayPage.add_bag)

    def getPages(self):
        return self.driver.find_elements(*HolidayPage.pages)

    def getHolidays(self):
        return self.driver.find_elements(*HolidayPage.holidays)

    def getChoice(self):
        return self.driver.find_element(*HolidayPage.choice)

    def getNxt(self):
        return self.driver.find_element(*HolidayPage.nxt_page)

    def getBasket(self):
        return self.driver.find_element(*HolidayPage.basket)

    def getNotice(self):
        return self.driver.find_element(*HolidayPage.notice)
