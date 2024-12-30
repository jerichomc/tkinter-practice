from tkinter import *
from tkinter.ttk import *
import time

def start():
    tasks = 10
    x = 0
    while(x < tasks):
        time.sleep(1) #adds a delay so the bar doesnt auto fill
        bar['value']+=10 #everytime button is hit it will fill bar by 10
        x += 1
        percent.set(str((x/tasks) * 100) +"%")
        text.set(str(x)+"/"+str(tasks)+" tasks completed")
        window.update_idletasks() #will update the window after every iteration



window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=300)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent).pack()
taskLabel = Label(window, textvariable=text).pack()


button = Button(window, text="Download", command=start).pack()

window.mainloop()
