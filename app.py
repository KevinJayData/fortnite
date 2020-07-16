import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()

start = time.time()
current = time.time()

time_limit = 20
pyautogui.FAILSAFE = True

while current - start < time_limit:
    pyautogui.moveTo(screenWidth*0.25, screenHeight*0.25, duration=2, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    pyautogui.PAUSE = 3.14

    pyautogui.moveTo(screenWidth*0.75, screenHeight*0.25, duration=2, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    pyautogui.PAUSE = 2.5

    pyautogui.moveTo(screenWidth*0.75, screenHeight*0.75, duration=2, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    pyautogui.PAUSE = 0.4

    pyautogui.moveTo(screenWidth*0.25, screenHeight*0.75, duration=2, tween=pyautogui.easeInOutQuad)
    pyautogui.click()
    pyautogui.PAUSE = 1.2

    current = time.time()

