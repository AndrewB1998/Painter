import tkinter as tk #import tkinter module

class Calculator(tk.Frame): #create class Calculator
#root window
    def __init__(self, master): #create constructor
        self.master = master #create master
        master.title("Pocket Calculator") #set title
        master.geometry("300x300") #set geometry
        master.resizable(0,0) #set resizable
        

#execute
root = tk.Tk() #create root window
app = Calculator(root)
root.mainloop()