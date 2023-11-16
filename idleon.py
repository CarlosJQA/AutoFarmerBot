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
upgradePosY = 347
upgradePosX = 585
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

def find_squirrel():
    picture = pyautogui.screenshot(region=(164,121,1276,722))
    width, height = picture.width, picture.height

    for x in range(0,1276,10):
        for y in range(0,722,10):
            r,g,b = picture.getpixel((x,y))

            if b == 126:
                click(x+180, y+131)
                time.sleep(0.05)
                break


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
#loop for claim ez access stuff
while counter < 2:
    win32api.SetCursorPos((707, upgradePosY))
    click(707, upgradePosY)
    counter += 1
    upgradePosY += 95
    time.sleep(0.1)
    if counter == 2:
        counter = 0
        break

#click arcade
click(1318,583)

#claim arcade balls
click(1556,75)

#launch arcade balls
holdclick(1724,970)
time.sleep(random.uniform(1.2, 1.5))

#waiting for arcade minigame
time.sleep(random.uniform(20, 20.5))

#close arcade
click(1814,72)
time.sleep(random.uniform(1,1.5))


#click codex button
click(1385,980)

#click gaming menu
click(1717,557)
#click harvest all button
click(1338,84)
time.sleep(random.uniform(2,2.5))
#click sprinkler
click(1171,501)
#click harvest all button
click(1338,84)
time.sleep(random.uniform(2,2.5))
#Squirrel claim acorn function
find_squirrel()
time.sleep(random.uniform(6,7))
#click fertilizer upgrades
click(1648,201)
#fertilizer upgrades loop
while counter < 3:
    win32api.SetCursorPos((upgradePosX, 507))
    click(upgradePosX, 507)
    counter += 1
    upgradePosX += 370
    time.sleep(0.1)
    if counter == 3:
        counter = 0
        break

#close game
time.sleep(2)
click(1894,13)
time.sleep(0.5)
#reset library search bar
resetlibrarysearchbar()