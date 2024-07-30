from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.edge.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_options = Options()

serv_obj = Service("C:\Drivers\edge\msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.automationtesting.in/Register.html")
dropdown_country = Select(driver.find_element(By.XPATH,'//*[@id="Skills"]'))

#Capture all the options and print them

all_options = dropdown_country.options
print(len(all_options))
for option in all_options:
    print(option.text)
time.sleep(5)
# Selecting One Option from the drop down list
dropdown_country.select_by_visible_text("Adobe Photoshop")
time.sleep(2)

#Selecting from drop down without using in built functions

for option in all_options:
    if option.text=="Analytics":
        option.click()

