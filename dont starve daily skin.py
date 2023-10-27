from pyautogui import *
import pyautogui
import time
import win32api, win32com
import random
import subprocess



def doubleclick(x,y):
    win32api.SetCursorPos((x,y))
    pyautogui.doubleClick()
    time.sleep(random.uniform(0.1, 0.5))

nombreJuego = ("Dont Starve")
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
#waiting for log in and main menu screen load
time.sleep(35)
#click on daily gift
click(969,626)
time.sleep(6)
#close game
click(1894,11)
time.sleep(0.5)
#reset library search bar
subprocess.Popen(command)
time.sleep(0.5)
click(215,180)
#run idleslayer script
subprocess.run(['python','C:\\Users\\CarlosJD\\Documents\\Programas python\\idleslayer.py'])