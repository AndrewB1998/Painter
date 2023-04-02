from tkinter import * 
class Painter(Frame):
    """A simple paint program with color-, size- and shape options."""
     
    def __init__(self, master):
        self.master = master 
        
        #Set default values for color, size, shape, background color
        self.given_color = "Black" 
        self.given_size = 3 
        self.given_shape = "Line" 
        self.given_bg = "White"
         
        self.appUI(master)
        
    #create appUI function for user interface   
    def appUI(self, master):
        master.title("Painter")
        master.resizable(None, None)
        
        #Row and column configuration
        Grid.rowconfigure(self.master,3,weight=1)
        Grid.columnconfigure(self.master,1,weight=1)  
        Grid.columnconfigure(self.master,2,weight=1) 
        Grid.columnconfigure(self.master,3,weight=1) 
        Grid.columnconfigure(self.master,4,weight=1)
        Grid.columnconfigure(self.master,5,weight=1)
            
        
        #Options
        color = ["Black", "Red", "Green", "Blue", "Yellow", "Orange", "Purple", "Brown", "White"]
        size = [1,2,3,4,5,6,7,8,9,10]
        shape = ["Line","Circle", "Square", "Triangle"]
        
        #Create labels for optionmenu buttons
        color_label = Label(master, text="Color:")
        color_label.grid(row=1, column=1, sticky="EW")

        size_label = Label(master, text="Size:")
        size_label.grid(row=1, column=2, sticky="EW")

        shape_label = Label(master, text="Shape:")
        shape_label.grid(row=1, column=3, sticky="EW")

        bg_label = Label(master, text="Background:")
        bg_label.grid(row=1, column=4, sticky="EW")
        
        bg_label = Label(master, text="Clear Canvas (Ctrl+z):")
        bg_label.grid(row=1, column=5, sticky="EW")
        
        #Create OptionMenu buttons, their options and make them scalable left/right
        self.color_var = StringVar(master)
        self.color_var.set(color[0])
        self.color_menu = OptionMenu(master, self.color_var, *color, command= self.set_color)
        self.color_menu.grid(row=2, column=1, sticky="EW")

        self.size_var = IntVar(master)
        self.size_var.set(size[2])
        self.size_menu = OptionMenu(master, self.size_var, *size, command= self.set_size)
        self.size_menu.grid(row=2, column=2, sticky="EW")
        
        self.shape_var = StringVar(master)
        self.shape_var.set(shape[0])
        self.shape_menu = OptionMenu(master, self.shape_var, *shape, command= self.set_shape)
        self.shape_menu.grid(row=2, column=3, sticky="EW")
        
        self.bg_var = StringVar(master)
        self.bg_var.set(color[0])
        self.bg_menu = OptionMenu(master, self.bg_var, *color, command= self.set_bg)
        self.bg_menu.grid(row=2, column=4, sticky="EW")
        
        self.clear_button = Button(master, text="Clear", command= self.canvas_clear)
        self.clear_button.grid(row=2, column=5, sticky="EW")
        master.bind("<Control-z>", self.canvas_clear)        

        
        
        #Create canvas and mouse bindings
        canvas_width = 1000
        canvas_height = 600
        self.canvas = Canvas(master, width=canvas_width, height=canvas_height, bg="white")
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonPress-1>", self.press_mouse)
        self.canvas.bind("<ButtonRelease-1>", self.release_mouse)
        self.canvas.grid(columns=6, sticky="NSEW")    
        
        
        
    #Change color, size, shape
    def set_color(self, color):
        self.given_color = color   
         
    def set_size(self, size):
        self.given_size = size
    
    def set_shape(self, shape):
        self.given_shape = shape
        
    #Clear canvas
    def canvas_clear(self, event=None): #event=None is for keyboard binding so that the function can be called without an event)
        self.canvas.delete("all")
        

    #Change background color
    def set_bg(self, bg):
        self.given_bg = bg
        self.canvas.config(bg=self.given_bg)
        
    #Draw in realtime
    def draw(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_line(x1, y1, x2, y2, fill=self.given_color, width=self.given_size)
    
    #Draw shapes from mouse click and release
    def press_mouse(self, event):
        self.press_x = event.x 
        self.press_y = event.y
    
    def release_mouse(self, event):
        x1, y1 = self.press_x, self.press_y
        x2, y2 = event.x, event.y
        if self.given_shape == "Circle":
            radius = ((x2-x1)**2 + (y2-y1)**2)**0.5 # using circle formula (x-x1)^2 + (y-y1)^2 = r^2
            self.canvas.create_oval(x1-radius, y1-radius, x1+radius, y1+radius, fill=self.given_color, width=self.given_size, outline= "")
            
        elif self.given_shape == "Square":
            if x2 < x1: #swap x1 and x2 if x2 is smaller than x1
                x1, x2 = x2, x1
            if y2 < y1: #swap y1 and y2 if y2 is smaller than y1
                y1, y2 = y2, y1
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.given_color, width=self.given_size, outline= "")
            
        elif self.given_shape == "Triangle":
            self.canvas.create_polygon(x1, y1, x2, y2, x1-(x2-x1), y2, fill=self.given_color, width=self.given_size, outline= "")
        
def main():
    root = Tk() #create root window
    Painter(root)
    root.mainloop()


if __name__ == "__main__": #call main function
    main()

