import tkinter as tk
from tkinter import*

from tkinter import messagebox as mb


root = Tk()
root.geometry("312x124")  # this is for the size of the box
root.resizable(0, 0)  # this is to prevent from resizing the rootr box
root.title("GUESS THE PIN")

a = Label(root, text ="Welcome to Guess the PIN Game", bg="sky blue")
a.pack()

a = Label(root, text ="Please enter your 4 digit pin")
a.pack()

pin = "1234" #that's the given pin (correct pin)

#pin entry
pin_entry = Entry(root, show='*')
pin_entry.pack()

def trylogin(): 
    
    if pin == pin_entry.get():
        mb.showinfo("--CORRECT--", "Yeah! You WON")    

    else:
        mb.showerror("--WRONG--", "Wrong pin")

#when you press this button, trylogin is called
button = Button(root, text="Try", bg="plum2", command = trylogin) 
button.pack()

root.mainloop()
