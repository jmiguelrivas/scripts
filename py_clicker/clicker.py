import pyautogui
import time

# Give yourself a few seconds to switch to the window you want to click
time.sleep(3)

# Move the mouse to a position (x=500, y=300)
pyautogui.moveTo(500, 300, duration=0.5)  # duration in seconds for smooth movement

# Click at the current mouse position
pyautogui.click()

# Or move and click in one command
pyautogui.click(x=600, y=400)
