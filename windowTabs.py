from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window) #widget that manages a collection of windows and displays

tab1 = Frame(notebook) #new frame for tab1
tab2 = Frame(notebook)

notebook.add(tab1, text="tab 1")
notebook.add(tab2, text="tab 2")
notebook.pack(expand=True, fill="both") #expand = expand to fill any space not otherwise used
                                        #fill will fill space on x and y axis

Label(tab1, text="hello tab 1", width=50, height=25).pack() #tab1 argument is the parent element
Label(tab2, text="hello tab 2", width=50, height=25).pack()


window.mainloop()
