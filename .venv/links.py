from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests as requests

edge_options = Options()

serv_obj = Service("C:\Drivers\edge\msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

links = driver.find_elements(By.XPATH,'//a')
print(len(links))
count = 0
for link in links:
    url = link.get_attribute('href')
    res = requests.head(url)
    if res.status_code>=400:
        print(url, " is broken")


# Broken Links
