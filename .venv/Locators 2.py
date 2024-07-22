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


driver.get("https://www.facebook.com/")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abcxyz123")      #tag-id
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys("xyz@123")         #tag,class & attribute
driver.find_element(By.CSS_SELECTOR,"button[data-testid=royal_login_button").click()        #tag-attribute
time.sleep(2)