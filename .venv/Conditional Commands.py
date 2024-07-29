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

searchbox = driver.find_element(By.XPATH,'//*[@id="small-searchterms"]')
print(searchbox.is_displayed())
print(searchbox.is_enabled())
radiobutton = driver.find_element(By.XPATH,'//*[@id="gender-male"]')
print(radiobutton.is_selected())

driver.find_element(By.XPATH,'//*[@id="gender-male"]').click()
print(radiobutton.is_selected())
time.sleep(1)