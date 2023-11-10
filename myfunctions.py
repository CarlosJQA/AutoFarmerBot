from pyautogui import *
import pyautogui
import time
from PIL import Image
from io import BytesIO
from PIL import ImageOps
import win32api, win32com

#Function for image recognition
def detect_image_and_click():
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


#Basic function for clicking
def click(x,y):
    win32api.SetCursorPos((x,y))
    pyautogui.click()
    time.sleep(random.uniform(0.1, 0.5))

#Basic function for hold clicking
def holdclick(x,y):
    win32api.SetCursorPos((x,y))
    pyautogui.mouseDown()
    time.sleep(random.uniform(5,7.5))

#Function for reseting steam library search bar
def resetlibrarysearchbar():
    subprocess.Popen(command)
    time.sleep(0.5)
    click(215,180)