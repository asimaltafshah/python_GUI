from tkinter import *
root = Tk()
#entry filed
e= Entry(root,width = 50,fg="#ffffff",bg="#019875",borderwidth =5 )
e.pack()
e.insert(0,"Enter your name here")

# button function 
def myClick():
 hello = "Hello  " + e.get()
 myLabel =Label(root, text =hello)
 myLabel.pack()
myButton = Button(root, text ="Enter Your Name", padx=50 , pady=50,command =myClick,borderwidth=5,fg="#ffffff", bg="#EB9532")

myButton.pack()

root.mainloop()
