import pyautogui as gui
import random, time

ui = gui.prompt("Enter wordlist path: ")
ui_open = open(ui, 'r')

time.sleep(3)
for x in ui_open:
	gui.write(x)
	gui.press('Enter')
	time.sleep(.5)
	gui.press('backspace', presses=6)


