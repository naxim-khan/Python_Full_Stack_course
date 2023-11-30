from numpy import bytes_
from selenium import webdriver
from selenium.webdriver.common import By
import time 

URL="https://www.python.org/events/"

firefoxdriver="C:\\Users\\Nazeem Khan\\Downloads\\geckodriver-v0.33.0-win64"

driver=webdriver.Firefox(executable_path=firefoxdriver)

driver.get(URL)

time.sleep(2)

content=driver.find_element(By.CLASS_NAME,'list-recent-events menu')




print(content)