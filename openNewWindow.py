from tkinter import *

def create_window():
    new_window = Toplevel() # top level creates a new window 'on top' of other windows, when 'bottom' level windows are closed all above windows will also close

    old_window.destroy() #close out of old window

old_window = Tk() #Tk is a new independent window, not linked with any 'below'

Button(old_window, text="create new window", command=create_window).pack()

old_window.mainloop()
