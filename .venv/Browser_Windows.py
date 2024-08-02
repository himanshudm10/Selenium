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

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(2)

window_id = driver.current_window_handle
print(window_id)

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(2)

#Opening  all the browser windows
windows = driver.window_handles
for window in windows:
    driver.switch_to.window(window)
    print (driver.title)

#Closing Specific Browser Window
for window in windows:
    driver.switch_to.window(window)
    if driver.title =='OrangeHRM':
        driver.close()

time.sleep(2)