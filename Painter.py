from tkinter import * 

#create class Painter
class Painter(Frame): 
    def __init__(self, master): #create constructor
        self.master = master 
        self.given_color = "Black" #set default color to black
        self.given_size = 1 #set default size to 1
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
        Grid.columnconfigure(self.master,3,weight=1)   
        
        #Options
        color = ["Black", "Red", "Green", "Blue", "Yellow", "Orange", "Purple", "Brown", "White"]
        size = [1,2,3,4,5,6,7,8,9,10]
        shape = ["Circle", "Square", "Triangle"]
        
        
        #Create OptionMenu buttons, their options and set them on top row
        self.color_var = StringVar(master)
        self.color_var.set(color[0])
        self.color_menu = OptionMenu(master, self.color_var, *color, command= self.set_color)
        self.color_menu.grid(row=0, column=0, sticky="NSEW")

        self.size_var = IntVar(master)
        self.size_var.set(size[0])
        self.size_menu = OptionMenu(master, self.size_var, *size, command= self.set_size)
        self.size_menu.grid(row=0, column=1, sticky="NSEW")
        
        self.shape_var = StringVar(master)
        self.shape_var.set(shape[0])
        self.shape_menu = OptionMenu(master, self.shape_var, *shape)
        self.shape_menu.grid(row=0, column=2, sticky="NSEW")
        
        
        #Create canvas
        canvas_width = 1000
        canvas_height = 600
        self.canvas = Canvas(master, width=canvas_width, height=canvas_height, bg="white")
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.grid(columnspan=3, sticky="NSEW")    
        
        #Change color
    def set_color(self, color):
        self.given_color = color   
         
    def set_size(self, size):
        self.given_size = size
        
         #Draw
    def draw(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_line(x1, y1, x2, y2, fill= self.given_color, width= self.given_size)  
        
def main():
    root = Tk() #create root window
    Painter(root)
    root.mainloop()


if __name__ == "__main__": #call main function
    main()
