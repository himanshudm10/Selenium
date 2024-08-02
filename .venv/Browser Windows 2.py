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

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="Wikipedia1_wikipedia-search-input"]').send_keys("Selenium")
driver.find_element(By.XPATH,'//*[@id="Wikipedia1_wikipedia-search-form"]/div/span[2]/span[2]/input').click()


driver.find_element(By.LINK_TEXT,"Selenium").click()
driver.find_element(By.LINK_TEXT,"Selenium in biology").click()
driver.find_element(By.LINK_TEXT,"Selenium (software)").click()
driver.find_element(By.LINK_TEXT,"Selenium disulfide").click()
time.sleep(2)

windows = driver.window_handles
for window in windows:
    driver.switch_to.window(window)
    print(driver.title)
driver.quit()