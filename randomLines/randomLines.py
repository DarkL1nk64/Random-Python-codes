import pyautogui as pygui
import random

#What it does? opens up your paint, and draws random lines for fun and save

pygui.hotkey('win', 'r')
pygui.sleep(0.5)
pygui.typewrite("mspaint")
pygui.sleep(0.5)
pygui.press("enter")
pygui.sleep(0.5)
pygui.hotkey('win', 'up')
pygui.sleep(0.5)
pygui.moveTo(1905, 1030)
pygui.click()

scrnX, scrnY = pygui.size()
pygui.moveTo(scrnX/2, scrnY/2)

pygui.mouseDown(button='left')
for x in range(100):
	positionX = random.random()*scrnX
	positionY = random.random()*scrnY
	pygui.moveTo(positionX, positionY)
	pygui.sleep(0.01)

pygui.mouseUp(button='left')
pygui.sleep(1)
pygui.hotkey('ctrl', 's')
pygui.sleep(1)
pygui.typewrite(pygui.prompt('Insert a name'))
pygui.sleep(1)
pygui.press('enter')
pygui.sleep(1.5)
pygui.hotkey('alt', 'f4')
