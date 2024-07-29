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
# driver.implicitly_wait(10)                   # implicit wait
mywait = WebDriverWait(driver, 10)     # explicit wait
driver.get("https://www.google.com")
searchbox = driver.find_element(By.ID,"APjFqb")
searchbox.send_keys("What is wait command in Selenium")
searchbox.submit()


result = mywait.until(EC.presence_of_element_located((By.XPATH,'//h3[text()="Selenium Wait Commands: Implicit, Explicit, and Fluent Wait"]')))
result.click()
driver.quit()