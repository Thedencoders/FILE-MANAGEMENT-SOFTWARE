from tkinter import *
from tkinter import messagebox,ttk



root = Tk()
root.title("Main page")
root.geometry("900x700")

b1 = Button(root ,text = "Organise" ,font = ("arial",40,"bold"))
b1.pack()

b2 = Button(root ,text = "phone" ,font = ("arial",40,"bold"))
b2.pack()

b3 = Button(root ,text = "activities" ,font = ("arial",40,"bold"))
b3.pack()

b4 = Button(root ,text = "resotore" ,font = ("arial",40,"bold"))
b4.pack()

b5 = Button(root ,text = "about us" ,font = ("arial",40,"bold"))
b5.pack()

root.mainloop()
