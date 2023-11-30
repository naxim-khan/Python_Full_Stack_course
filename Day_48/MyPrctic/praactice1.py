import pyautogui
import time


time.sleep(1)

pyautogui.click('win')

word="Chrome"
for litter in word:
    pyautogui.click(litter)
    time.sleep(1)

    pyautogui.click('enter')