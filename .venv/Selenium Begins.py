#Test Case
#1 Open Web Browser(Microsoft Edge)
#2 Open URL https://opensource-demo.orangehrmlive.com/
#3 Enter Username (Admin)
#4 Enter Password (admin123)
#5 Click on login
#6 Capture title of the homepage.
#7 Verify title of the page: OrangeHRM
#8 Close Browser
#------------------------------------------------------------------

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.edge.service import Service
serv_obj = Service("C:\Drivers\edge\msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys("admin123")
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

actual_title = driver.title
if actual_title == "OrangeHRM":
    print("Test Passed")
else:
    print("Test Failed")
time.sleep(10)
