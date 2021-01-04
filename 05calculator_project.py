from tkinter import *
root = Tk()
root.title("Simple Calculator")

#entry filed
e= Entry(root,width = 50,fg="#ffffff",bg="#019875", borderwidth = 5 )
e.grid(row=0, column = 0, columnspan =3,padx =10,pady=10)
#e.insert(0,"Enter your name here")

# button function
#  
def button_click(number):
 current = e.get()
 e.delete(0,END)
 e.insert(0,str(current)+str(number))

def button_clear():
 e.delete(0,END)

def button_add():
 first_number = e.get()
 global f_num
 global math
 math="add"
 f_num = int(first_number)
 e.delete(0,END)

def botton_subtract():
 first_number = e.get()
 global f_num
 global math
 math="subtract"
 f_num = int(first_number)
 e.delete(0,END)

def botton_mutiply():
 first_number = e.get()
 global f_num
 global math
 math="multiply"
 f_num = int(first_number)
 e.delete(0,END)

def botton_division():
 first_number = e.get()
 global f_num
 global math
 math="division"
 f_num = int(first_number)
 e.delete(0,END)

def button_equal():
 second_number = e.get()
 e.delete(0,END)
 if(math=="add"):
  e.insert(0,f_num + int(second_number))
 if(math=="subtract"):
  e.insert(0,f_num - int(second_number))
 if(math=="multiply"):
  e.insert(0,f_num * int(second_number))
 if(math=="division"):
  e.insert(0,f_num / int(second_number))


# Define Buttons
button_1 =Button(root,text ="1", padx=40, pady=20, command=lambda: button_click(1), fg="#ffffff", bg="#E5958E")
button_2 =Button(root,text ="2", padx=40, pady=20, command=lambda: button_click(2), fg="#ffffff", bg="#E5958E")
button_3 =Button(root,text ="3", padx=40, pady=20, command=lambda: button_click(3), fg="#ffffff", bg="#E5958E")
button_4 =Button(root,text ="4", padx=40, pady=20, command=lambda: button_click(4), fg="#ffffff", bg="#E5958E")
button_5 =Button(root,text ="5", padx=40, pady=20, command=lambda: button_click(5), fg="#ffffff", bg="#E5958E")
button_6 =Button(root,text ="6", padx=40, pady=20, command=lambda: button_click(6), fg="#ffffff", bg="#E5958E")
button_7 =Button(root,text ="7", padx=40, pady=20, command=lambda: button_click(7), fg="#ffffff", bg="#E5958E")
button_8 =Button(root,text ="8", padx=40, pady=20, command=lambda: button_click(8), fg="#ffffff", bg="#E5958E")
button_9 =Button(root,text ="9", padx=40, pady=20, command=lambda: button_click(9), fg="#ffffff", bg="#E5958E")
button_0 =Button(root,text ="0", padx=40, pady=20, command=lambda: button_click(0), fg="#ffffff", bg="#E5958E")

button_add =Button(root,text ="+",padx=39,pady=20,command=button_add, fg="#ffffff", bg="#FFBA00")
button_subtract =Button(root,text ="-",padx=39,pady=20,command=botton_subtract, fg="#ffffff", bg="#FFBA00")
button_multiply =Button(root,text ="x",padx=39,pady=20,command=botton_mutiply, fg="#ffffff", bg="#FFBA00")
button_division =Button(root,text ="/",padx=39,pady=20,command=botton_division, fg="#ffffff", bg="#FFBA00")

button_equal =Button(root,text ="=",padx=95,pady=20,command=button_equal, fg="#ffffff", bg="#FFBA00")
button_clear =Button(root,text ="Clear",padx=82,pady=20,command=button_clear, fg="#ffffff", bg="#FFBA00")

#put buttons on the screen
button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_0.grid(row = 4, column = 0)
button_clear.grid(row = 4, column = 1, columnspan=2)
button_add.grid(row = 5, column = 0)
button_equal.grid(row = 5, column = 1, columnspan=2)
button_subtract.grid(row = 6, column = 0)
button_multiply.grid(row = 6, column = 1)
button_division.grid(row = 6, column =2)



myButton = Button(root, text ="Enter Your Name", padx=50 , pady=50,borderwidth=5,fg="#ffffff", bg="#EB9532")



root.mainloop()
