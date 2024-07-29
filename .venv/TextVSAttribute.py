from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

edge_options = Options()

serv_obj = Service("C:\Drivers\edge\msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)


driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()
time.sleep(2)
emailbox = driver.find_element(By.XPATH,'//*[@id="FirstName"]')
button = driver.find_element(By.XPATH,'//*[@id="register-button"]')
emailbox.send_keys("xyz@gmail.com")
print("Text Captured: ", emailbox.text)
print("Attribute Captured: ", emailbox.get_attribute('value'))          # Attribute = value
print("Text Captured for BUTTON: ", button.text)
print("Attribute Captured for BUTTON: ", button.get_attribute('type'))  # Attribute = type
time.sleep(2)