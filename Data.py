# Data.py

# User guide
info_text = '''
        Welcome to the Painter app!
        
        Hold your left mouse button down and move the mouse to draw.
        
        You can choose your color, font and shape from the dropdown menus. Use slider to change size
        
        For shapes, hold and release the left mouse button to draw.
        
        You can also write text, save it and insert the text in the canvas by selecting the "Text" shape.
        
        To delete the last drawn object, press Ctrl+z. To delete all objects, press the "Clear all" button.
        
        To change the background color, choose a color from the background dropdown menu.
        '''

# Options, labels, mouse events
color = ["Black", "Red", "Green", "Blue", "Yellow", "Orange", "Purple", "Brown", "White"]
size = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shape = ["Pencil", "Line", "Text", "Circle", "Square", "Triangle"]
label = ["Color", "Shape", "Background", "Font", "Size"]
fonts = ["Georgia", "Arial", "Times", "Courier", "Verdana", "Helvetica"]
events = ["<B1-Motion>", "<ButtonPress-1>", "<ButtonRelease-1>"]


