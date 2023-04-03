from tkinter import * 
class Painter(Frame):
    """A simple paint program with color-, size- and shape options."""
    
    def __init__(self, master):
        
        # Set default values for color, size, shape, background color and font color and create master window
        self.given_color = "Black" 
        self.given_size = 3 
        self.given_shape = "Pencil" 
        self.given_bg = "White"
        self.given_font_color = "Black"
        self.master = master 
        self.appUI(master)
        
    # Create appUI function for user interface   
    def appUI(self, master):
        master.title("Painter")
        master.resizable(None, None)
        
        # Row and column configuration
        Grid.rowconfigure(self.master, 3, weight=1)
        for col in range(4):
            Grid.columnconfigure(self.master, col, weight=1)
        
        # Options
        color = ["Black", "Red", "Green", "Blue", "Yellow", "Orange", "Purple", "Brown", "White"]
        size = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        shape = ["Pencil","Circle", "Square", "Triangle"]
        
        # Create labels for optionmenu buttons using for loop
        label = ["Color", "Size", "Shape", "Background"]
        for col, label in enumerate(label):
            Label(master, text=label, font=("Georgia", 14)).grid(row=1, column=col, sticky="EW")
        
        # Create OptionMenu buttons using loop and their options + make them scalable left/right 
        color_var, size_var, shape_var, bg_var = StringVar(master), IntVar(master), StringVar(master), StringVar(master)
        dd_menus = [(color_var, color, self.set_color), (size_var, size, self.set_size), (shape_var, shape, self.set_shape), (bg_var, color, self.set_bg)]
        for col, (var, values, func) in enumerate(dd_menus):
            var.set(values[0])
            menu = OptionMenu(master, var, *values, command=func)    
            menu.config(font=("Georgia", 10), bg='#FFEFD5')
            menu.grid(row=2, column=col, sticky="NEW")    
        
        # Create canvas
        canvas_width = 1000
        canvas_height = 600
        self.canvas = Canvas(master, width=canvas_width, height=canvas_height, bg=self.given_bg)
        self.canvas.grid(columns=6, sticky="NSEW", padx= 5, pady=5)
        
        #Create clear canvas button
        clear_button = Button(master, text="Clear (ctrl+z)", font= ("Georgia", 10), bg='#FFEFD5', command=self.canvas_clear)
        clear_button.grid(row=4, column=0, sticky="W", padx=8, pady=8)
        master.bind("<Control-z>", self.canvas_clear)    
        
        # Mouse bindings 
        events = ["<B1-Motion>", "<ButtonPress-1>", "<ButtonRelease-1>"]
        handlers = [self.draw, self.press_mouse, self.release_mouse]
        for event, handler in zip(events, handlers):
            self.canvas.bind(event, handler)
            
    # Change color, size, shape
    def set_color(self, color):
        self.given_color = color
        self.master.configure(background=color)
        
    def set_size(self, size):
        self.given_size = size
    
    def set_shape(self, shape):
        self.given_shape = shape
        
    # Clear canvas
    def canvas_clear(self, event=None): # event=None is for keyboard binding so that the function can be called without an event)
        self.canvas.delete("all")

    # Change background color
    def set_bg(self, bg):
        self.given_bg = bg
        self.canvas.config(bg=self.given_bg)
        
        
    # Draw in realtime
    def draw(self, event):
        if self.given_shape == "Pencil": # So that line doesn't show if other shapes are selected
            x1, y1 = (event.x - 1), (event.y - 1)
            x2, y2 = (event.x + 1), (event.y + 1)
            self.canvas.create_line(x1, y1, x2, y2, fill=self.given_color, width=self.given_size)
    
    # Draw shapes from mouse click and release
    def press_mouse(self, event):
        self.press_x = event.x 
        self.press_y = event.y
    
    def release_mouse(self, event):
        x1, y1 = self.press_x, self.press_y
        x2, y2 = event.x, event.y
        if self.given_shape == "Circle":
            radius = ((x2-x1)**2 + (y2-y1)**2)**0.5 # Using circle formula (x-x1)^2 + (y-y1)^2 = r^2
            self.canvas.create_oval(x1-radius, y1-radius, x1+radius, y1+radius, fill=self.given_color, width=self.given_size, outline= "")
            
        elif self.given_shape == "Square":
            if x2 < x1: # Swap x1 and x2 if x2 is smaller than x1
                x1, x2 = x2, x1
            if y2 < y1: # Swap y1 and y2 if y2 is smaller than y1
                y1, y2 = y2, y1
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.given_color, width=self.given_size, outline= "")
            
        elif self.given_shape == "Triangle":
            self.canvas.create_polygon(x1, y1, x2, y2, x1-(x2-x1), y2, fill=self.given_color, width=self.given_size, outline= "")
        
def main():
    root = Tk() # Create root window
    Painter(root)
    root.mainloop()

if __name__ == "__main__": # Call main function
    main()

