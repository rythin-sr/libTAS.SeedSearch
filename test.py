import pyautogui
import time

base = pyautogui.locateOnScreen('base.png')
x = base[0]
y = base[1]

pyautogui.moveTo(x+25, y+580) #unpause
time.sleep(2)
pyautogui.moveTo(x+400, y+630) #start game
time.sleep(2)
pyautogui.moveTo(x+630, y+630) #stop game
time.sleep(2)
pyautogui.moveTo(x+221, y+545) #increment system time
