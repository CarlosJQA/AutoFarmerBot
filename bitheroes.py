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
    time.sleep(random.uniform(0.1, 0.5))

def click(x,y):
    win32api.SetCursorPos((x,y))
    pyautogui.click()
    time.sleep(random.uniform(0.1, 0.5))

def resetlibrarysearchbar():
    subprocess.Popen(command)
    time.sleep(0.5)
    click(215,180)

nombreJuego = ("Bit Heroes")
steam_path = "C:\Program Files (x86)\Steam\steam.exe"
command = [steam_path]
#Search and open the game with opensteam.py
subprocess.Popen(command)

time.sleep(1)

click(233,58)    

click(83,185)

pyautogui.typewrite(nombreJuego)

time.sleep(0.5)
doubleclick(78,244)
#waiting time for log in
time.sleep(50)
doubleclick(78,244)
#daily rewards
click(638,732)
click(910,254)

#quit game
click(1243,14)
resetlibrarysearchbar()