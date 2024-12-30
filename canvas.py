from tkinter import *

#canvas = widget used to draw graphs, plots, images in a window

window = Tk()

canvas = Canvas(window, height=500, width=500)
# blueLine = canvas.create_line(0,0,500,500, fill="blue", width=5) #starting coordinates and ending coordinates
# redLine = canvas.create_line(500,0,0,500, fill="red", width=5)
# canvas.create_rectangle(50,50,250,250)
canvas.create_arc(0,0,500,500,fill="red", extent=180, width=10)
canvas.create_arc(0,0,500,500,fill="white", extent=180,start=180, width=10)
canvas.create_oval(190,190,310,310, fill="white", width=10)
canvas.pack()

window.mainloop()
