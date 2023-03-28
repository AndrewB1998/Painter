import tkinter as tk #import tkinter module

class Calculator(tk.Frame): #create class Calculator
#root window
    def __init__(self, master): #create constructor
        self.appUI(master) #call appUI function
        
    def appUI(self, master): #create appUI function
        self.master = master #create master
        master.title("Pocket Calculator") #set title
        master.geometry("800x800") #set geometry
        master.resizable(width= None, height= None) #set resizable

def main(): #create main function
    root = tk.Tk() #create root window
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__": #call main function
    main()