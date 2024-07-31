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

driver.get("https://testpages.herokuapp.com/styled/alerts/alert-test.html")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="promptexample"]').click()

alternate_window = driver.switch_to.alert

print(alternate_window.text)
time.sleep(2)
alternate_window.send_keys("Hey! JS Prompt")
time.sleep(2)
alternate_window.accept()
time.sleep(5)

# handling Pop-Up
driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="pass_div"]/input[3]').click()
driver.switch_to.alert.accept()

# Authentication Pop-Up

driver.get("https://authorized:password001@testpages.eviltester.com/styled/auth/basic-auth-results.html")
time.sleep(5)
driver.maximize_window()
