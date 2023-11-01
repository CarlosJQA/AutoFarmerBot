from pyautogui import *
import pyautogui
import time
import win32api, win32com
import random
import subprocess 
import keyboard
from PIL import Image
counter = 0

def holdclick(x,y):
    win32api.SetCursorPos((x,y))
    pyautogui.mouseDown()
    time.sleep(random.uniform(5,7.5))

def doubleclick(x,y):
    win32api.SetCursorPos((x,y))
    pyautogui.doubleClick()
    time.sleep(random.uniform(0.1,0.5))
nombreJuego = ("Legends of Idleon MMO")

steam_path = "C:\Program Files (x86)\Steam\steam.exe"

command = [steam_path]

#search and open the game from steam library
subprocess.Popen(command)

time.sleep(1)

click(233,58)    

click(83,185)

pyautogui.typewrite(nombreJuego)

time.sleep(0.5)

doubleclick(78,244)

#waiting for servers 
time.sleep(20)

#set to windowed full screen
click(1364, 249)
time.sleep(2)

#select elemental sorcerer char
click(659, 786)

#press play
click(1760,760)
time.sleep(random.uniform(4.5, 5.6))

#load claim button image for image recognition
image = Image.open('claim.PNG').convert('L')

#search image on screen
location = pyautogui.locateCenterOnScreen('claim.PNG')

#check if the image was found then click on image location
if location is not None:
    click(location[0], location[1])