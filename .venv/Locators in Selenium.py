from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.edge.service import Service
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_options = Options()

serv_obj = Service("C:\Drivers\edge\msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)


driver.get("https://automationexercise.com/")
driver.maximize_window()
time.sleep(3)
li_tags = driver.find_elements(By.CLASS_NAME, "nav nav-pills nav-stacked")
links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))
print(len(li_tags))

