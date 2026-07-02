from selenium import webdriver 
from selenium.webdriver.chrome.service import services 
from selenium.webdriver.common.by import by
import time

driver = webdriver.chrome()

driver.get("https://www.google.com")

time.sleep(5)

driver.quit()