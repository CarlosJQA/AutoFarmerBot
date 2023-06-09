from tkinter import * 
import subprocess
from tkinter import Button
import customtkinter
import os 

def call_script(script_name):
    scrip_path = os.path.join("Documents", "Programas Python", script_name)
    subprocess.call(["python", scrip_path])


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.title("Autofarmer")
root.geometry('400x240')
#root.resizable(False, False)

frame = Frame(root)
frame.grid()

button = customtkinter.CTkButton(master=root, text="Idle Slayer", command=lambda: call_script("idleslayer.py"))
button.place(relx= 0.5, rely= 0.5, anchor= CENTER)

button2 = customtkinter.CTkButton(master=root, text="Idle Wasteland", command=lambda: call_script("idlewasteland.py"))
button2.place(relx= 0.5, rely= 0.3, anchor= CENTER)


root.mainloop()