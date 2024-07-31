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

driver.get("https://demo.automationtesting.in/Frames.html")

# Switching to different frames

driver.find_element(By.XPATH,'//a[normalize-space()="Iframe with in an Iframe"]').click()

outerframe = driver.find_element(By.XPATH,'//*[@id="Multiple"]/iframe')
driver.switch_to.frame(outerframe)

innerframe = driver.find_element(By.XPATH,'/html/body/section/div/div/iframe')
driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH,'/html/body/section/div/div/div/input').send_keys("Hello IFrame")
time.sleep(2)


