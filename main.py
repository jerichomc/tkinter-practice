from tkinter import *

window = Tk() #instantiate an instance of a window
window.geometry("640x640") #height and width of window
window.title("practice tkinter") #titles window box

#labels
#photo = PhotoImage(file="/path") can pass in image=photo in label construction to make the label an image
#if you want text and an image on the label you can compound="bottom" to have both
label = Label(window, text="Label",
 font=("Arial", 40, "bold"),
  fg="#81BFDA", bg="#F5F0CD",
  relief=RAISED,
  bd=10,
  padx=20, pady=20,) #creates label
label.pack() #puts label on screen
# label.place(x=320, y=10) #places label in a specific spot

#Buttons
count = 0
def click():
    global count #this makes the poutside variable usable in the function
    count += 1
    print(f"You've hit the button {count} times")

button = Button(window,
text="Click me",
command=click,
font = ("Arial", 30),
fg="#81BFDA",
bg="#FADA7A",
 activeforeground="#81BFDA",
 activebackground="#FADA7A",
state=ACTIVE)
button.pack()
#if you use state=DISABLED the button will be disabled
# can use image=photo and compund='top' same as labels

#entry widgets
def submit():
    username = entry.get()
    print(f"Hello {username}")
    entry.config(state=DISABLED) #disables entry box after username is submitted  
def delete():
    entry.delete(0, END) #will delete characters from index 0 to end
def backspace():
    entry.delete(len(entry.get())-1, END) #removes last character

entry = Entry(window,
font=("Arial", 20),
fg="#81BFDA",
bg="white")
#use show="*" for passwords to hide password
entry.insert(0, "Username") #0 is the starting index, this is default text

entry.pack(side=LEFT)

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(side=RIGHT)

del_button = Button(window, text="Delete", command=delete)
del_button.pack(side=RIGHT)

backspace_button = Button(window, text="Backspace", command=backspace)
backspace_button.pack(side=RIGHT)

#Checkbox buttons
def display():
    if (x.get()==1): #If button is checked they agree 
        print("You agree")
    else: 
        print("You disagree")
x = IntVar()#default returns a 1 or 0

check_button = Checkbutton(window,
text="check this",
font=("Arial", 10, "bold"),
bg="#FADA7A",
variable=x,
onvalue=1,
offvalue=0,
command=display,
fg="#81BFDA",
activebackground="#FADA7A",
activeforeground="#81BFDA",
padx=25,
pady=10)
check_button.place(x=5, y=440)
#can pass image=photo and compound="left" here the same way

#radio buttons
food = ["pizza", "burger", "sushi"]
def order():
    if (x.get()==0):
        print("Pizza")
    elif (x.get()==1):
        print("Burger")
    elif (x.get()==2):
        print("Sushi")
    else:
        print("Wat")

x = IntVar()
for index in range(len(food)): #creates one radio button per item in list
    radio_button = Radiobutton(window,
     text=food[index], #adds text to buttons
      variable=x, #groups radio buttons together if they share same variable
       value=index, #assigns each radio button different value
       padx=25, #adds padding on x axis
       font=("Impact", 10),
       indicatoron=0, #eliminate circle indicators
       width =100, #width of radio buttons
       command=order, #sets command to function
       )
    #image = foodimages[index] would add an image to each button in the for loop

    radio_button.pack(anchor=W) #anchors them west

#icon = PhotoImage(file="logo.png") converts photo to usable image
# window.iconphoto(True, icon) will set the window icon to this photo

window.config(background="#F5F0CD") #sets bg color


window.mainloop() # will show the window on screen and listen for events




