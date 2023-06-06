import subprocess
import time
from pyautogui import *
import pyautogui

import win32api
import random

nombreJuego = input("Introduce el nombre del juego ")

steam_path = "C:\Program Files (x86)\Steam\steam.exe"

command = [steam_path]

subprocess.Popen(command)

time.sleep(1)

def click(x,y):
    win32api.SetCursorPos((x,y))
    pyautogui.click()
    time.sleep(random.uniform(0.2, 0.5))

def doubleclick(x,y):
    win32api.SetCursorPos((x,y))
    pyautogui.doubleClick()
    time.sleep(random.uniform(0.2, 0.5))

click(233,58)    

click(83,185)

pyautogui.typewrite(nombreJuego)

time.sleep(0.5)

doubleclick(78,244)