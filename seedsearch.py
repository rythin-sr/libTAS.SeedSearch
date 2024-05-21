import pyautogui
import time

base = pyautogui.locateOnScreen('base.png')
x = base[0]
y = base[1]
ispaused = False
starting_time = 1 #system time at which the search should start

while(True):
	pyautogui.moveTo(x+25, y+580) #unpause
	pyautogui.click()
	pyautogui.moveTo(x+400, y+630) #start game
	pyautogui.click()

	#wait for movie to play out
	while(not ispaused):
		try:
			if pyautogui.locateOnScreen('pause.png')[0] != 0:
				ispaused = True
		except pyautogui.ImageNotFoundException:
			ispaused = False

    time.sleep(1)

	pyautogui.screenshot("output/screenshot_"+ str(starting_time) + ".png") #save screenshot
	pyautogui.moveTo(x+630, y+630) #stop game
	pyautogui.click()
	pyautogui.moveTo(x+221, y+545) #increment system time
	time.sleep(0.5)
	pyautogui.click()
	starting_time = starting_time + 1
	ispaused = False

