from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

edge_options = Options()

serv_obj = Service("C:\Drivers\edge\msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)


driver.get("https://money.rediff.com/gainers")
print(driver.title)
print(driver.current_url)
print(driver.page_source)
