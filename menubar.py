from tkinter import *

def openFile():
    print("File has been opened")

def saveFile():
    print("file has been saved")

def cut():
    print("You have cut")

def copy():
    print("you have copied")

def paste():
    print("You have pasted")

window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("MV Boli", 10)) #adds onto menu instead of window
menubar.add_cascade(label="file", menu=fileMenu) #dropdown menu 
fileMenu.add_command(label="open", command=openFile) #adds items in the dropdown for file
fileMenu.add_command(label="save", command=saveFile)
fileMenu.add_separator() #serperates options within a menu
fileMenu.add_command(label="exit", command=quit)

editMenu = Menu(menubar, tearoff=0, font=("MV Boli", 10))
menubar.add_cascade(label="edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

window.mainloop()

#adding images
#fileMenu.add_command(label=x, command=y, image=imageVariable, compound='left')
