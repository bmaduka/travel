from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    setting = (By.XPATH, "//button/span[contains(text(),'Settings')]")
    recommend_set = (By.ID, "ccc-recommended-settings")
    close = (By.XPATH, "//div[@class='input-select__clear']/button/span")
    destination = (By.XPATH, "//input[@name='destination']")
    flight_from = (By.XPATH, "//div[@class='tabset']/button[1]")
    checkbx = (By.XPATH, "//section[@class='search-form']/div/section/div[2]/div/button")
    airports = (By.XPATH, "//label[@for='search[departure_points]']")
    departure_date = (By.XPATH, "//button[@class='search-field-button']/span[contains(text(), 'Departure Date')]")
    month = (By.XPATH, "//p[@class='datepicker__title']")
    nxt = (By.XPATH, "//button/span[contains(@class, 'icon icon--arrow-right')]")
    dates = (By.XPATH, "//button[@class='datepicker__button']")
    search_fields = (By.XPATH, "//div/div[2]/div[@class='search-fields__field']/button")
    nights = (By.XPATH, "//div/div[2]/div[@class='field']/div[@class='field__wrap']/select")
    select_room = (By.XPATH, "//select[@name='search[number_of_rooms]']")
    sel_child = (By.XPATH, "//select[@name='search[children]']")
    sel_inf = (By.XPATH, "//select[@name='search[infants]']")
    sel_age = (By.XPATH, "//select[contains(@name,'search[child_ages')]")
    holiday_search = (By.XPATH, "//section[@class='search-fields']/div[5]/div[@class='search-fields__field']/button")



    def getSetting(self):
        return self.driver.find_element(*HomePage.setting)

    def getRecset(self):
        return self.driver.find_element(*HomePage.recommend_set)

    def getClose(self):
        return self.driver.find_element(*HomePage.close)

    def getDestination(self):
        return self.driver.find_element(*HomePage.destination)

    def getFlight(self):
        return self.driver.find_element(*HomePage.flight_from)

    def getCheckbx(self):
        return self.driver.find_element(*HomePage.checkbx)

    def getAirports(self):
        return self.driver.find_elements(*HomePage.airports)

    def getDeparture_date(self):
        return self.driver.find_element(*HomePage.departure_date)

    def getMonth(self):
        return self.driver.find_element(*HomePage.month)

    def get_nxt(self):
        return self.driver.find_element(*HomePage.nxt)

    def getDates(self):
        return self.driver.find_elements(*HomePage.dates)

    def getSearch_fields(self):
        return self.driver.find_element(*HomePage.search_fields)

    def getNights(self):
        return self.driver.find_element(*HomePage.nights)

    def getRoom(self):
        return self.driver.find_element(*HomePage.select_room)

    def getChild(self):
        return self.driver.find_element(*HomePage.sel_child)

    def getInfant(self):
        return self.driver.find_element(*HomePage.sel_inf)

    def getAge(self):
        return self.driver.find_element(*HomePage.sel_age)

    def getHoliday_search(self):
        return self.driver.find_element(*HomePage.holiday_search)


