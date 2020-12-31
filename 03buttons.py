from tkinter import *
root = Tk()
def myClick():
 myLabel =Label(root, text ="Look i Clicked").pack()

myButton = Button(root, text ="Click me!", padx=50 , pady=50,command =myClick,fg="#ffffff", bg="#000fff")

myButton.pack()

root.mainloop()
