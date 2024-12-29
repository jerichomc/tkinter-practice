from tkinter import *
from tkinter import colorchooser #add submodule
from tkinter import messagebox

def submit():
    input = text.get("1.0", END) #retrieves beginning and end of text input
    messagebox.showinfo(title="message", message=input)

def click():
    color = colorchooser.askcolor() #brings up color choice menu, saves choice to variable
    colorHex = color[1] #in ask color the second index is the hex code for the color, this is what you want to access
    window.config(bg=colorHex) #sets background to chosen

window = Tk()
window.geometry("420x420") #sets window size

button = Button(text="click me", command=click)
button.place(x=10, y=10)

text = Text(window,
            bg="light yellow",
            font=("Ink Free", 20,),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="red") #creates text window
text.place(x=10, y=50)

button2 = Button(window, text="submit", command=submit)
button2.place(x=10, y=250)

window.mainloop()
