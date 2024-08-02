from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait




serv_obj = Service("C:\Drivers\edge\msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
rows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
print(rows)

columns = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print(columns)


#Printing data from all rows and columns

for r in range(2,rows+1):
    for c in range(1, columns+1):
        data = driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]")
        print(data.text, end="    ")
    print("\n")