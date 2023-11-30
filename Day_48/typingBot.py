from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time

URL="https://www.ratatype.com/typing-test/test/"
# URL="https://monkeytype.com/"

firefoxdriver = "C:\\Users\\Nazeem Khan\\Downloads\\geckodriver-v0.33.0-win64\\geckodriver"

driver = webdriver.Firefox(executable_path=firefoxdriver)
driver.get(URL)

time.sleep(2)
# Find the text to type
text_element = driver.find_element(By.CSS_SELECTOR, ".mainTxt")
# print('Click words')
# time.sleep(3)
# text_element = driver.find_elements(By.CLASS_NAME, "word")
# time.sleep(2)
# words=""
print('Text Find Successfully!!!')
# for word in text_element:
#     words += word.text+" "


# print(words)
# print('test started....')
# # for word in words:
# #     pyautogui.typewrite(word)
# pyautogui.write(words)


# print('Completed>>.')

text = text_element.text
time.sleep(1)
# print(txt.text)
# Type the text without delays
# print('Started...')
# # pyautogui.write(text)

length=len(text)
char=0

while True:
    pyautogui.press(text[char])
    char+=1
    if char == length:
        break


# print("Completed!!!")

# driver.quit()






