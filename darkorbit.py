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
import pwinput

def click(x,y):
    win32api.SetCursorPos((x,y))
    pyautogui.click()
    time.sleep(random.uniform(0.1, 0.5))

counter = 0
path = "C:\\Users\\CarlosJD\\Dark Orbit\\DarkOrbit.exe"
command = path
password =pwinput.pwinput(prompt='Password: ')


subprocess.Popen(command)
time.sleep(4)
#login clicks
click(963,422)
click(1252, 457)
#type primary password
pyautogui.typewrite(password)
keyboard.press_and_release("enter")
time.sleep(2)
#connect to server
click(962,640)
time.sleep(2)
#loop for closing news updates
while counter < 2:
    click(964,474)
    counter +=1
    if counter == 2:
        break

#click play
click(980,221)
time.sleep(10)
#close game
click(1896, 6   )