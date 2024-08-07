from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait




serv_obj = Service("C:\Drivers\edge\msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://jqueryui.com/datepicker/")
frame = driver.find_element(By.XPATH,'//*[@id="content"]/iframe')
driver.switch_to.frame(frame)

month = "June"
year = "2025"
date = "10"

driver.find_element(By.XPATH,'//*[@id="datepicker"]').click()

while True:
    mon = driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/span[1]').text
    yr = driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/span[2]').text

    if mon == month and yr == year:
        break

    else:
        driver.find_element(By.XPATH, '//*[@id="ui-datepicker-div"]/div/a[2]').click()

time.sleep(2)

dates = driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']/table/tbody/tr/td/a")

for dat in dates:
    if dat.text == date:
        dat.click()
        break

time.sleep(2)


