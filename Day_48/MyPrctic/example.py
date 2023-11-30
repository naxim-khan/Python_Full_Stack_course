import pyautogui 
import time
word="Chrome"
pyautogui.press('win')

time.sleep(0.5)

for letter in word:
    pyautogui.press(letter)
    # print()

pyautogui.press('enter')

time.sleep(1)
# pyautogui.press('win')
for i in range(0,10):
    pyautogui.press('tab')

pyautogui.press('enter')

time.sleep(2)
passw="Chrome@471972"

for p in passw:
    pyautogui.press(p)

pyautogui.press('enter')

pyautogui.keyDown('ctrl')
pyautogui.press('l')
pyautogui.keyUp('ctrl')

url="www.google.com"

for letter in url:
    pyautogui.press(letter)

pyautogui.press('enter')