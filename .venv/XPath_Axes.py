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


driver.get("https://money.rediff.com/gainers")
time.sleep(2)
text = driver.find_element(By.XPATH,"//a[contains(text(), 'Mansi Finance')]/self::a").text
text2 = driver.find_elements(By.XPATH,"//a[contains(text(), 'Mansi Finance')]/ancestor::tr/descendant::*")
print(len(text2))
for txt in text2:
    print(txt)
time.sleep(4)