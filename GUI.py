import tkinter as tk
from math import sin, cos, sqrt
from tkinter import ttk


window = tk.Tk()

window.title('Python GUI')

window.resizable(False,False)

a_label = ttk.Label(window, text="A label from Hell")
a_label.grid(column=0, row=0)

def click_me():
    action.configure(text="I've been clicked")
    a_label.configure(foreground = 'red')
    a_label.configure(text = 'A red label')

#adding a button
action = ttk.Button(window, text= "Click me!!", command = click_me)
action.grid(column = 1, row=0)


# greeting = tk.Label(text='Python Rock', fg = 'white', bg = 'black')
# greeting.pack()
#=====================
# Start GUI
#=====================
window.mainloop()
