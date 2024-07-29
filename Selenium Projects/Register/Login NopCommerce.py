from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_options = Options()

serv_obj = Service("C:\Drivers\edge\msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

gender = driver.find_element(By.ID,"gender-male")
gender.click()
first_name = driver.find_element(By.ID,"FirstName")
first_name.send_keys("Himanshu")
last_name = driver.find_element(By.ID,"LastName")
last_name.send_keys("Dubey")
dob = driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[1]/option[11]')
dob.click()
month = driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[2]/option[7]')
month.click()
year = driver.find_element(By.XPATH,'//*[@id="main"]/div/div/div/div[2]/form/div[1]/div[2]/div[4]/div/select[3]/option[88]')
year.click()
email = driver.find_element(By.ID,"Email")
email.send_keys("abc@gmail.com")
password = driver.find_element(By.ID,"Password")
password.send_keys("Selenium123")
cmf_password = driver.find_element(By.ID,"ConfirmPassword")
cmf_password.send_keys("Selenium123")
register = driver.find_element(By.ID,"register-button")
register.click()

