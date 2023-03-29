from tkinter import * 

#create class Painter
class Painter(Frame): 
    def __init__(self, master): #create constructor
        self.master = master 
        self.appUI(master) #call appUI function
        
    #create appUI function for user interface   
    def appUI(self, master):
        master.title("Painter")
        master.resizable(None, None)
        
        #Row and column configuration
        Grid.rowconfigure(self.master,1,weight=1)
        Grid.columnconfigure(self.master,0,weight=1)  
        Grid.columnconfigure(self.master,1,weight=1) 
        Grid.columnconfigure(self.master,2,weight=1)      
        
        #Buttons
        self.button1 = Button(master, height=2, text="Color", command= lambda: self.dropDownMenu())
        self.button2 = Button(master, height=2, text="Size", command= lambda: self.dropDownMenu())
        self.button3 = Button(master, height=2, text="Shape", command= lambda: self.dropDownMenu())
        
        #Button placement, sticky is used to stretch the widget to fill the entire cell
        self.button1.grid(row=0, column=0, sticky= "NSEW")
        self.button2.grid(row=0, column=1, sticky= "NSEW")
        self.button3.grid(row=0, column=2, sticky= "NSEW")
        
        #Canvas properties
        canvas_width = 1000
        canvas_height =600
        self.canvas = Canvas(master, width=canvas_width, height=canvas_height, bg="white")
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.grid(columnspan=3, padx=5, pady=5, sticky= "NSEW")      
        
    def draw(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_line(x1, y1, x2, y2, fill= "black", width=5)  

    #def dropDownMenu(self):
        #TBDcreate drop down menu for color, size and shape and their functions

def main():
    root = Tk() #create root window
    Painter(root)
    root.mainloop()


if __name__ == "__main__": #call main function
    main()
