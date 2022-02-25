import time

import chromedriver_binary

from selenium import webdriver
# !chromedriver_binary was installed by pip!
from selenium.webdriver.common.keys import Keys
import pyautogui
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--enable-popup-blocking")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.onthebeach.co.uk/")
driver.implicitly_wait(5)


setting = driver.find_element(By.XPATH, "//button/span[contains(text(),'Settings')]")
driver.execute_script("arguments[0].click();", setting)
driver.find_element(By.ID, "ccc-recommended-settings").click()


close = driver.find_element(By.XPATH, "//div[@class='input-select__clear']/button/span")
driver.execute_script("arguments[0].click();", close)
wait = WebDriverWait(driver, 20)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='destination']")))
where_to = driver.find_element(By.XPATH, "//input[@name='destination']")

# driver.execute_script("arguments[0].click();", where_to)
where_to.send_keys("Barcelona")
driver.find_element(By.XPATH, "//div[@class='tabset']/button[1]").click()
wait.until(expected_conditions.presence_of_element_located(
    (By.XPATH, "//section[@class='search-form']/div/section/div[2]/div/button")))
#try--driver.find_element(By.XPATH, "//div[@class='email-catcher__close']")
checkbx = driver.find_element(By.XPATH, "//section[@class='search-form']/div/section/div[2]/div/button")
checkbx.send_keys(Keys.ENTER)
# driver.execute_script("document.getElementsByTagName('span')[53].click();")
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//label[@for='search[departure_points]']")))
airports = driver.find_elements(By.XPATH, "//label[@for='search[departure_points]']")
for airport in airports:
    if "Bristol" in airport.text:
        driver.execute_script("arguments[0].click();", airport)
        break

driver.find_element(By.XPATH, "//button[@class='search-field-button']/span[contains(text(), 'Departure Date')]").click()

month = driver.find_element(By.XPATH, "//p[@class='datepicker__title']")
while month.text != "April 2022":
    Next = driver.find_element(By.XPATH, "//button/span[contains(@class, 'icon icon--arrow-right')]")
    driver.execute_script("arguments[0].click();", Next)

dates = driver.find_elements(By.XPATH, "//button[@class='datepicker__button']")
for date in dates:
    if "17" in date.text:
        driver.execute_script("arguments[0].click();", date)
        break

driver.find_element(By.XPATH, "//div/div[2]/div[@class='search-fields__field']/button").click()
nights = Select(driver.find_element(By.XPATH, "//div/div[2]/div[@class='field']/div[@class='field__wrap']/select"))
nights.select_by_value("8-10")

driver.execute_script("document.getElementsByTagName('span')[75].click();")
sel_room = Select(driver.find_element(By.XPATH, "//select[@name='search[number_of_rooms]']"))
sel_room.select_by_value("2")
sel_child = Select(driver.find_element(By.XPATH, "//select[@name='search[children]']"))
sel_child.select_by_value("1")
sel_inf = Select(driver.find_element(By.XPATH, "//select[@name='search[infants]']"))
sel_inf.select_by_value("1")
sel_age = Select(driver.find_element(By.XPATH, "//select[contains(@name,'search[child_ages')]"))
sel_age.select_by_value("10")

where_to.send_keys("Barcelona")
driver.find_element(By.XPATH,
                    "//section[@class='search-fields']/div[5]/div[@class='search-fields__field']/button").click()

wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='input-counter__quantity']")))
num_bags = driver.find_element(By.XPATH, "//div[@class='input-counter__quantity']")
while num_bags.text != "3":
    add_bag = driver.find_element(By.XPATH, "//span[contains(@class,'icon--symbol-plus')]")
    driver.execute_script("arguments[0].click();", add_bag)
    time.sleep(5)
    # wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='input-counter__quantity']")))
    num_bags = driver.find_element(By.XPATH, "//div[@class='input-counter__quantity']")

pages = driver.find_elements(By.XPATH, "//div[@class='pagination__page-number-wrapper']/button")
for i in range(0, len(pages)):
    holidays = driver.find_elements(By.XPATH, "//section/h2[@class='holiday-finder-results__hotel-name']")
    for holiday in holidays:
        if "Atenas" in holiday.text:
            choice = holiday.find_element(By.XPATH,
                                          "parent::section/parent::header/parent::div/section[2]/footer/div/a")
            driver.execute_script("arguments[0].click();", choice)
            break
    else:
        try:
            nxt = driver.find_element(By.XPATH, "//div/button/span[@class='pagination__icon pagination__icon--right']")
            driver.execute_script("arguments[0].click();", nxt)
            # time.sleep(4)
            continue
        except:
            break

# time.sleep(3)
driver.find_element(By.XPATH, "//button[contains(@class,'button--primary button--push-down')]").click()
# time.sleep(3)
try:
    driver.find_element(By.XPATH, "//span[contains(@class,'notice__close')]").click()
except:
    pass
# time.sleep(2)
driver.execute_script("document.getElementsByTagName('button')[15].click();")
driver.save_screenshot('screen_shot.png')
image = pyautogui.screenshot()
image.save("shot.png")

time.sleep(5)
