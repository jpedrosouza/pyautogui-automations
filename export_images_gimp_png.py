import pyautogui
import time

pyautogui.moveTo(1158, 1079)

pyautogui.click()

for i in range(20):
    # Open export panel

    pyautogui.hotkey('ctrl', 'e')

    # Click in firt export button

    pyautogui.moveTo(639, 746)
    pyautogui.click()

    time.sleep(2)

    # Click in second export button

    pyautogui.moveTo(1028, 778)
    pyautogui.click()

    # Select image from editor

    pyautogui.moveTo(234, 71)
    pyautogui.click()

    # Remove image from editor

    pyautogui.moveTo(255, 77)
    pyautogui.click()