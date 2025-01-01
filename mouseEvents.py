from tkinter import *

def doSomething(event):
    print(f"Hello {str(event.x)}")

window = Tk()

window.bind("<Button-1>", doSomething) #button-1 = left click, 2 = middle, 3 = right


window.mainloop()
