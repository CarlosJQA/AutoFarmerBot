from pyautogui import *
import pyautogui
import time
import win32api, win32com
import random
import subprocess

counter = 0

def doubleclick(x,y):
    win32api.SetCursorPos((x,y))
    pyautogui.doubleClick()
    time.sleep(random.uniform(0.1,0.5))

nombreJuego = ("Idle Slayer")

steam_path = "C:\Program Files (x86)\Steam\steam.exe"

command = [steam_path]

subprocess.Popen(command)

time.sleep(1)

click(233,58)    

click(83,185)

pyautogui.typewrite(nombreJuego)

time.sleep(0.5)

doubleclick(78,244)


#Search and open the game with opensteam.py
#subprocess.call(["python", "Documents\Programas python\opensteam.py"])

time.sleep(4)

def click(x,y):
    win32api.SetCursorPos((x,y))
    pyautogui.click()
    time.sleep(random.uniform(0.1,0.5))



def escape():
    pyautogui.keyDown('escape')
    time.sleep(0.2)
    pyautogui.keyUp('escape')


#Main menu click
click(815,22)

time.sleep(5)

#AFK earned coins and slayer points click
click(815,22)

#Minions menu
click(129,92)

click(500,979)

upgradePos = 376

time.sleep(0.5)

win32api.SetCursorPos((736, upgradePos))

#This loop will reclaim the rewards from the minions and send them again on a mission if you have the required amount of slayer points
while counter < 3:
    win32api.SetCursorPos((736, upgradePos))
    click(736, upgradePos)
    counter += 1
    upgradePos += 274
    time.sleep(0.2)
    if counter == 3:
        break


#Close game

escape()
time.sleep(1)
escape()

click(845,815)

#reset library search bar
subprocess.Popen(command)
time.sleep(0.5)
click(215,180)
#run cookieclicker script
subprocess.run(['python','C:\\Users\\CarlosJD\\Documents\\AutoFarmer\\cookieclicker.py'])