from pyautogui import *
import pyautogui
import time
import win32api, win32com
import random
import subprocess

def click(x,y):
    win32api.SetCursorPos((x,y))
    pyautogui.click()
    time.sleep(random.uniform(0.1,0.5))

def doubleclick(x,y):
    win32api.SetCursorPos((x,y))
    pyautogui.doubleClick()
    time.sleep(random.uniform(0.1,0.5))

counter = 0
upgradePosY = 387
nombreJuego = ("Cookie Clicker")

steam_path = "C:\Program Files (x86)\Steam\steam.exe"

command = [steam_path]

#opening steam and searching for game
subprocess.Popen(command)

time.sleep(1)

click(233,58)    

click(83,185)

pyautogui.typewrite(nombreJuego)

time.sleep(0.5)

doubleclick(78,244)
time.sleep(5)

#loop for buildings upgrades
while counter < 6:
    win32api.SetCursorPos((1749, upgradePosY))
    click(1749, upgradePosY)
    counter += 1
    upgradePosY += 63
    time.sleep(0.1)
    if counter == 6:
        break
    
time.sleep(random.uniform(0.8, 1))
#close game
click(1903,7)
#reset steam search bar
subprocess.Popen(command)
time.sleep(0.5)
click(215,180)
#run bitheroes.script
subprocess.run(['python','C:\\Users\\CarlosJD\\Documents\\AutoFarmer\\bitheroes.py'])