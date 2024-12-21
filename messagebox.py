from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title="Info Box", message="Text inside box")
    # messagebox.showwarning(title="Warning!", message="VIRUS DETECTED")
    messagebox.showerror(title="Error", message="Something went wrong")
    messagebox.askokcancel(title="ask ok cancel", message="Yes?")


window = Tk()

button =Button(window, command=click, text="click me")
button.pack()

window.mainloop()