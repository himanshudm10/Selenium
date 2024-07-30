from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_options = Options()

serv_obj = Service("C:\Drivers\edge\msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.automationtesting.in/Register.html")
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id, 'checkbox')]")
print(len(checkboxes))

# Approach 1
# for i in range(len(checkboxes)):
#    checkboxes[i].click()

# Approach 2
# for checkbox in checkboxes:
#   checkbox.click()

# Select multiple checkboxes by choice
for checkbox in checkboxes:
   if checkbox.get_attribute('value') == "Cricket" or checkbox.get_attribute('value') == "Hockey":
       checkbox.click()

time.sleep(2)

# Clearing all the checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
       checkbox.click()

time.sleep(2)