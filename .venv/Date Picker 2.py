from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select




serv_obj = Service("C:\Drivers\edge\msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.ID,"dob").click()

month = Select(driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div[1]/div/select[1]'))
month.select_by_visible_text("Jun")

year = Select(driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div[1]/div/select[2]'))
year.select_by_visible_text("1990")

dates = driver.find_elements(By.XPATH,'//*[@id="ui-datepicker-div"]/table/tbody/tr/td/a')
for date in dates:
    if date.text=="20":
        date.click()
        break



time.sleep(5)