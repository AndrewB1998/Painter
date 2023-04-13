from tkinter import * 
import Data as dt
class Painter(Frame):
    """A simple paint program with color-, size- and shape options."""
    
    def __init__(self, master):
        self.master = master
        self.appUI(master)
        
    # Create appUI function for user interface   
    def appUI(self, master):
        master.title("Painter")
        master.resizable(None, None)
        master.minsize(950,400)
        
        # Set default values for color, size, shape, background color and font color and create master window
        self.given_color = "Black" 
        self.given_size = 3 
        self.given_shape = "Pencil" 
        self.given_bg = "White"
        self.given_font_color = "Black"
        self.given_font = "Georgia"
        self.objects = []
        
        # Row and column configuration
        Grid.rowconfigure(self.master, 3, weight=1)
        for col in range(5):
            Grid.columnconfigure(self.master, col, weight=1)
        
        # Create labels for optionmenu buttons
        for col, label in enumerate(dt.label):
            Label(master, text=label, font=("Georgia", 14)).grid(row=1, column=col, sticky="EW")
        
        # Create OptionMenu buttons using loop and their options + make them scalable left/right 
        color_var, shape_var, bg_var, font_var = StringVar(master), StringVar(master), StringVar(master), StringVar(master)
        dd_menus = [(color_var, dt.color, self.set_color), (shape_var, dt.shape, self.set_shape), (bg_var, dt.color, self.set_bg), (font_var, dt.fonts, self.set_font)]
        for col, (var, values, func) in enumerate(dd_menus):
            var.set(values[0])
            menu = OptionMenu(master, var, *values, command=func)    
            menu.config(font=("Georgia", 10), height=2, bg='#FFEFD5', cursor="hand2")
            menu.grid(row=2, column=col, sticky="NEW")    
        
        # Create canvas
        canvas_width = 1000
        canvas_height = 600
        self.canvas = Canvas(master, width=canvas_width, height=canvas_height, cursor="crosshair", bg=self.given_bg)
        self.canvas.grid(columns=5, sticky="NSEW", padx= 5, pady=5)

        #Size slider
        self.size_slider = Scale(master, bg='#FFEFD5', from_=0, to=20, orient=HORIZONTAL, variable=self.given_size, command=self.set_size)
        self.size_slider.grid(row=2, column=4, sticky="NSEW")
        
        # Clear canvas button
        clear_button = Button(master, text="Clear all", font= ("Georgia", 10), bg='#FFEFD5', cursor="hand2", command=self.canvas_clear)
        clear_button.grid(row=4, column=0, sticky= "NSEW", padx=5, pady=5)
        master.bind("<Control-z>", self.canvas_clear)    
        
        # Info button
        self.info_button = Button(master, text="Info", font= ("Georgia", 10), bg='#FFEFD5', cursor="hand2", command= self.info)
        self.info_button.grid(row=4, column=4, sticky="NSEW", padx=5, pady=5)
        self.info_button.config(state="normal")
        
        # Text entry box and button
        self.entry_box = Text(master, height=2)
        self.entry_box.grid(row=4, column=1,columns=2, padx=5, pady=5, sticky="NSEW")
        self.save_button = Button(master, text="Save text", font= ("Georgia", 10), width=25, bg='#FFEFD5', cursor="hand2", command=self.save)
        self.save_button.grid(row=4, column=3, padx=5, pady=5, sticky="NSW")
        
        # Mouse bindings 
        handlers = [self.draw, self.press_mouse, self.release_mouse]
        for event, handler in zip(dt.events, handlers):
            self.canvas.bind(event, handler)
            
    # Set functions
    def set_color(self, color):
        self.given_color = color
        self.master.configure(background=color)
    
    def set_shape(self, shape):
        self.given_shape = shape
        
    def save(self):
        self.saved_text = self.entry_box.get("1.0", "end-1c")
        self.given_shape = "Text"
    
    def set_size(self, size):
        self.given_size = size
        
    def set_font(self, font):
        self.given_font = font
        
    def set_bg(self, bg):
        self.given_bg = bg
        self.canvas.config(bg=self.given_bg)  
    
    # Window close and button unlock
    def destroy(self, info_win, info_button):
        info_win.destroy()
        info_button.config(state="normal")
        
    
    # User guide button and window
    def info(self, txt=dt.info_text):
        # Create info window
        info_win = Toplevel(self.master)
        info_win.geometry("400x450")
        info_win.resizable(False, False)
        info_win.title("Info")
        info_win.bind("<Destroy>", lambda event: self.info_button.config(state="normal")) #for button lock if closed from "x"
        Label(info_win, text=txt, wraplength=300, anchor="w", font=("Georgia", 10)).pack()
        ok_button = Button(info_win, text="OK", font=("Georgia", 10), bg='#FFEFD5', cursor="hand2", command=lambda: self.destroy(info_win, self.info_button))
        ok_button.pack(side="bottom", fill="x", padx=5, pady=5)
        self.info_button.config(state="disabled") # Lock button until window is closed
    
    # Canvas clear. Event=None is for keyboard binding so that the function can be called without an event)
    def canvas_clear(self, event=None): 
        if event is None:
            self.canvas.delete("all")
        if objects := self.canvas.find_all():
            self.canvas.delete(objects[-1])
        
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
        
        elif self.given_shape == "Line":
            self.canvas.create_line(x1, y1, x2, y2, fill=self.given_color, width=self.given_size)
        
        elif self.given_shape == "Text":
            self.canvas.create_text(x1, y1, text= self.saved_text, fill=self.given_color, font=(self.given_font, self.given_size))
            
def main():
    root = Tk() # Create root window
    Painter(root)
    root.mainloop()

if __name__ == "__main__": # Call main function
    main()


