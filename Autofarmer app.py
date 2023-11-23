from tkinter import * 
import subprocess
from tkinter import Button
import customtkinter
from customtkinter import *
import os 
from PIL import Image

#Autofarmer logo path and settings
autofarmer_logo = CTkImage(dark_image=Image.open("C:\\Users\\CarlosJD\\Documents\\AutoFarmer\\Icons\\Farmerbot.png"), size=(200,200))
#Don't Starve Together logo path and settings
dontstarve_logo = CTkImage(dark_image=Image.open("C:\\Users\\CarlosJD\\Documents\\AutoFarmer\\Icons\\dontstarvetogetherlogo.png"), size=(50,50))
#Cookie clicker Logo path and settings
cookie_logo = CTkImage(dark_image=Image.open("C:\\Users\\CarlosJD\\Documents\\AutoFarmer\\Icons\\cookie.png"), size=(50,50))
#Idle slayer logo path and settings
idleslayer_logo = CTkImage(dark_image=Image.open("C:\\Users\\CarlosJD\\Documents\\AutoFarmer\\Icons\\idleslayer.png"), size=(50,50))
#bit heroes logo path and settings
bitheroes_logo = CTkImage(dark_image=Image.open("C:\\Users\\CarlosJD\\Documents\\AutoFarmer\\Icons\\bitheroes.png"), size=(70,70))


def call_script(script_name):
    base_path = "C:\\Users\\CarlosJD\\Documents\\AutoFarmer"
    scrip_path = os.path.join(base_path, script_name)
    subprocess.call(["python", scrip_path])


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.title("Autofarmer")
root.geometry('920x640')
root.resizable(False, False)

frame = Frame(root)
frame.grid()

#Labels

logo_label = CTkLabel(master=root,image=autofarmer_logo, text="") 
logo_label.place(relx= 0.2, rely= 0.5, anchor= CENTER)

dst_label = CTkLabel(master=root,image=dontstarve_logo, text="") 
dst_label.place(relx= 0.42, rely= 0.1, anchor= E)

cookie_label = CTkLabel(master=root,image=cookie_logo, text="") 
cookie_label.place(relx= 0.42, rely= 0.3, anchor= E)

idleslayer_label = CTkLabel(master=root,image=idleslayer_logo, text="")
idleslayer_label.place(relx= 0.42, rely= 0.5, anchor= E)

bitheroes_logo = CTkLabel(master=root,image=bitheroes_logo, text="")
bitheroes_logo.place(relx= 0.42, rely= 0.7, anchor= E)

button = customtkinter.CTkButton(master=root, text="Idle Slayer", border_width=1, border_color="white", fg_color="#000000", hover_color="#1e1e1f", command=lambda: call_script("idleslayer.py"))
button.place(relx= 0.5, rely= 0.5, anchor= CENTER)

button2 = customtkinter.CTkButton(master=root, text="Cookie Clicker",border_width=1, border_color="white", fg_color="#000000", hover_color="#1e1e1f",command=lambda: call_script("cookieclicker.py"))
button2.place(relx= 0.5, rely= 0.3, anchor= CENTER)

button3 = customtkinter.CTkButton(master=root, text="Dont Starve",border_width=1, border_color="white", fg_color="#000000", hover_color="#1e1e1f",command=lambda: call_script("dont starve daily skin.py"))
button3.place(relx= 0.5, rely= 0.1, anchor= CENTER)

button4 = customtkinter.CTkButton(master=root, text="Bit Heroes",border_width=1, border_color="white", fg_color="#000000", hover_color="#1e1e1f", command=lambda: call_script("bitheroes.py"))
button4.place(relx= 0.5, rely= 0.7, anchor= CENTER)

button5 = customtkinter.CTkButton(master=root, text="Legends of Idleon MMO", border_width=1, border_color="white", fg_color="#000000", hover_color="#1e1e1f", command=lambda: call_script("idleon.py"))
button5.place(relx= 0.5, rely= 0.9, anchor= CENTER)

root.mainloop()