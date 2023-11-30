import pyautogui
import time
print("waiting...")
time.sleep(2)
print("Presing...")
pyautogui.press('win')
print("pressed")

word="Google Chrome"

for letter in word:
    pyautogui.press(letter)
    time.sleep(0.1)
time.sleep(1)
pyautogui.press('enter')
pyautogui.press('tab')


# pyautogui.press('win')

for i in range(0,1):
    time.sleep(1)
    pyautogui.press('tab')
    print(f"tab pressed {i} times")

time.sleep(1)
# pyautogui.press('enter')

# url=("https://www.youtube.com")

# for letter in url:
#     time.sleep(0.1)
#     pyautogui.press(letter)

# pyautogui.hold('ctrl')
# pyautogui.hold('l')
# pyautogui.keyUp('ctrl')
# pyautogui.keyUp('l')
# pyautogui.press('enter')