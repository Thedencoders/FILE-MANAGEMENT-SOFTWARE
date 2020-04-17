from tkinter import *
from tkinter import messagebox
from tkinter import ttk,filedialog
import os
def browser():
    root2 = Tk()
    root2.withdraw()
    folder = filedialog.askdirectory()
    source.set(folder)
    root2.mainloop()

    
def organiser():
    root1 = Tk()
    global source
    source = StringVar()
    root1.title("Organiser")
    root1.geometry("900x700")

    root1.config(background = 'black')
    rows = 0
    while rows < 50:
        root1.rowconfigure(rows , weight = 1)
        root1.columnconfigure(rows, weight = 1)
        rows +=1
    def next_tab(tab):
        s = source.get()
        if os.path.exists(s):
            nb.tab(tab, state= 'normal' )
            nb.select(tab)
        else:
            messagebox.showinfo('ALERT!','Enter correct path!')
            source.set('')
    nb = ttk.Notebook(root1)
    nb.grid(row = 0,column = 0,columnspan = 55 , rowspan = 55, sticky = 'NESW')

    tab1 = ttk.Frame(nb)
    nb.add(tab1, text="Source folder")

    l1 = Label(tab1 , text = 'Source folder  ')
    l1.grid(column = 0,row = 0)

    e1 = Entry(tab1,textvariable = source ,width = 70)
    
    e1.grid(row = 0,column = 1)
    b1 = Button(tab1,text = "Browse",command = browser)
    b1.grid(row=0,column=2)
        
    

    tab2 = ttk.Frame(nb)
    nb.add(tab2, text="Destination",state = 'disabled')

    
    tab3 = ttk.Frame(nb)
    nb.add(tab3, text="Parameters",state = 'disabled')


    tab4 = ttk.Frame(nb)
    nb.add(tab4, text="Exception",state = 'disabled')


    tab5 = ttk.Frame(nb)
    nb.add(tab5, text="confirmation",state = 'disabled')

    tab6 = ttk.Frame(nb)
    nb.add(tab6, text="execution",state = 'disabled')

    b2 = Button(tab1,text="Next",command=lambda: next_tab(tab2))
    b2.grid(row = 1,column = 0)
    








    root1.mainloop()
organiser()
