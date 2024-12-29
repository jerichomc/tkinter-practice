from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename() #returns file path from chosen file
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(text="Button", command=openFile)
button.pack()

window.mainloop()