from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "https://www.python.org/events/python-events/"

firefoxdriver = "C:\\Users\\Nazeem Khan\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver"
driver = webdriver.Firefox(executable_path=firefoxdriver)

driver.get(URL)

time.sleep(1)

events_times = driver.find_elements(By.CSS_SELECTOR, ".list-recent-events time")
event_names=driver.find_elements(By.CSS_SELECTOR, ".list-recent-events.menu a")

#     print(events_times.text
events={}
# for event in event_names:
#     print(event.text)
for n in range (len(events_times)):
    events[n]={
        "time":events_times[n].text,
        "name":event_names[n].text
    }
print(events)   
for event in events:
    print(f"time: {events[event]['time']}\nname: {events[event]['name']}")
time.sleep(3)

# dirver.quit()
