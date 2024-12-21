from tkinter import *

def submit():
    print(f"The temperature is: {str(scale.get())} degrees C")

def menu_submit():
    food = []

    for i in listbox.curselection():
        food.insert(i, listbox.get(i))

    print("You have ordered: ") #This function will print out everything ordered
    for i in food:
        print(i)
    

def add():
    listbox.insert(listbox.size(),entryBox.get()) #reads what is in entry box and adds it to list
    listbox.config(height=listbox.size()) #adjusts size of box as item is added

def delete():
    for index in reversed(listbox.curselection()): #reversed deletes in descending order so the indices dont change
        listbox.delete(index) #deletes current selections
    listbox.config(height=listbox.size())


window = Tk()
window.geometry("640x640")

scale = Scale(window, from_=100, to=0, #creates a scale from 1 to 100
              length=600,
              orient=VERTICAL, #or horizontal
              font=("Arial", 10, "bold"),
              tickinterval=10, #numeric indicators on scale
              showvalue=1, # iff set to 0 hides current value
              troughcolor="#69EAFF",
              fg="#FF1C00",
              bg="black",
 ) 
scale.set(0) #will auto set to argument passed in
scale.pack(side=LEFT)

button = Button(window, text="Submit", command=submit)
button.pack(side=LEFT)

#listbox
listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 20),
                  width=12,
                  selectmode=MULTIPLE, #MULTIPLE allows you to select multiple items


                )
listbox.pack(pady=10)

listbox.insert(1, "Pizza")
listbox.insert(2, "Pasta")
listbox.insert(3, "Bread")
listbox.insert(4, "Salad")
listbox.insert(5, "Soup")

listbox.config(height=listbox.size()) #changes height dynamically based on # of items

entryBox = Entry(window)
entryBox.pack(pady=5)

submitButton = Button(window, text="submit", command=menu_submit)
submitButton.pack(pady=5)

addButton = Button(window, text="add", command=add)
addButton.pack(pady=5)

delButton = Button(window, text="delete", command=delete)
delButton.pack(pady=5)

window.mainloop()

