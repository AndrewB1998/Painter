from tkinter import *   #import tkinter

class Painter(Frame): #create class Painter
    def __init__(self, master): #create constructor
        self.appUI(master) #call appUI function
        
    def appUI(self, master): #create appUI function
        self.master = master #create master
        master.title("Pocket Calculator") #set title
        master.resizable(width= None, height= None) #set resizable
        canvas_width = 800
        canvas_height = 600
        self.canvas = Canvas(master, width=canvas_width, height=canvas_height, bg="white") #create canvas
        self.canvas.pack(fill=BOTH, expand=YES)
        self.canvas.bind("<B1-Motion>", self.draw)

    def draw(self, event): #create draw function
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.canvas.create_line(x1, y1, x2, y2, fill="black")    

def main(): #create main function
    root = Tk() #create root window
    app = Painter(root)
    root.mainloop()

if __name__ == "__main__": #call main function
    main()