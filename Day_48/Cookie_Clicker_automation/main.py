from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

URL = "https://orteil.dashnet.org/cookieclicker/"
firefoxdriver = "C:\\Users\\Nazeem Khan\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver"
driver = webdriver.Firefox()

driver.get(URL)

# Wait for the element with ID "bigCookie" to be clickable (loaded and ready)
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "bigCookie"))
)

# Click the "langSelect-EN" element to change the language
lang = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "langSelect-EN"))
)
lang.click()

# Loop to click the "bigCookie" element
i=0
time.sleep(2)
print("It's started")
# for i in range(0,20):
while True:
    # time.sleep(0.01)
    
    # Re-locate the "bigCookie" element inside the loop to avoid staleness
    element = driver.find_element(By.ID, "bigCookie")
    # element.click()
    pyautogui.click(x=element.location['x']+200, y=element.location['y']+200)
    # print(i)
    # i+=1
   
# Close the WebDriver
driver.quit()
