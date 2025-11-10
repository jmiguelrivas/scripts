import pyautogui
import time

base = "XXX-"

print("You have 3 seconds to focus the password field...")
time.sleep(3)

for i in range(0,10000):
    pwd = base + f"{i:04d}"
    print(f"Trying: {pwd}")
    pyautogui.typewrite(pwd)
    pyautogui.press('enter')
    time.sleep(0.4)