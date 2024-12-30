from tkinter import *

def doSomething(event):
    print("button pressed")

def keyPressed(event):
    # print(f"you pressed: {event.keysym}")
    label.config(text=event.keysym) # will display whatver key was pressed

window = Tk()

window.bind("<Return>", doSomething) #will call a function if a certain key is pressed
window.bind("<Escape>", quit)
window.bind("<Key>", keyPressed)

label = Label(window, font=("Helvetica", 80))
label.pack()


window.mainloop()
