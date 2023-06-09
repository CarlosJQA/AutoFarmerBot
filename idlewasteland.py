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

nombreJuego = ("Idle Wasteland")

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

#selecting screen resolution



