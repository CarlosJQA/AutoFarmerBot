from pyautogui import *
import pyautogui
import time
import win32api, win32com
import random
import subprocess 
import keyboard
from PIL import Image
from io import BytesIO
from PIL import ImageOps
counter = 0

def holdclick(x,y):
    win32api.SetCursorPos((x,y))
    pyautogui.mouseDown()
    time.sleep(random.uniform(5,7.5))

def doubleclick(x,y):
    win32api.SetCursorPos((x,y))
    pyautogui.doubleClick()
    time.sleep(random.uniform(0.1,0.5))

def click(x,y):
    win32api.SetCursorPos((x,y))
    pyautogui.click()
    time.sleep(random.uniform(0.1, 0.5))

def resetlibrarysearchbar():
    subprocess.Popen(command)
    time.sleep(0.5)
    click(215,180)

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
time.sleep(random.uniform(5, 7))

#load original image
image = Image.open('claim.PNG')

#search image on screen
location = pyautogui.locateOnScreen('claim.PNG', confidence= 0.8)
print("Location:", location)
time.sleep(1)
#check if the image was found 
if location is not None:
    #take a screenshot of screen region
    left, top = location[0], location[1]
    width, height = image.width, image.height
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    #Compare original image with screenshot
    similarity = image == screenshot
    print("Similarity:", similarity)
    time.sleep(2)

    if similarity is not None:
        #click claim button
         click(location[0], location[1])
         print("Image was found")
    
    else:
        print('image was not found')
    

#click codex
click(1385,980)
#click quick ref
click(1170,214)
#click ez access
click(912,843)

#close game
click(1894,13)
time.sleep(0.5)
#reset library search bar
resetlibrarysearchbar()