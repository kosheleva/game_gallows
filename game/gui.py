from tkinter import *
import tkinter.font as font
from tkinter.messagebox import showinfo

""" Class GUI, contains methods to work with graphical interface """
class GUI:
    """ Window initialization """
    def __init__(self, width, height, title, opacity, bgColor):
        self._width = width
        self._height = height

        self._root = Tk()
        self.setWindowTitle(title)
        self.setWindowGeometry(width, height)
        self.setWindowOpacity(opacity)
        self.setWindowBackgroundColor(bgColor)

    
    """ Set window title """
    def setWindowTitle(self, title):
        self._root.title(title)


    """ Set window geometry """
    def setWindowGeometry(self, width, height):
        # Define user screen width and height
        screenWidth = self._root.winfo_screenwidth()
        screenHeight = self._root.winfo_screenheight()
 
        # Calculate Starting X and Y coordinates for Window
        centerX = round((screenWidth / 2) - (width / 2))
        centerY = round((screenHeight / 2) - (height / 1.5))

        self._root.geometry(f'{width}x{height}+{centerX}+{centerY}')

        self._root.resizable(width=False, height=False)


    """ Set window opacity """
    def setWindowOpacity(self, opacity):
        self._root.wm_attributes('-alpha', opacity)


    """ Set window color """
    def setWindowBackgroundColor(self, bgColor):
        self._root['bg'] = bgColor
        for child in self._root.winfo_children():
            child['bg'] = bgColor


    """ Display main window for game """
    def display(self):
        self._root.mainloop()


    """ Create frame """
    def openFrame(self, width, height, bgColor):
        frame = Frame(self._root, width=width, height=height, background=bgColor)
        return frame


    """ Locate frame """
    def packFrame(self, frame, side, padx, pady):
        frame.pack(side=side, padx=padx, pady=pady)


    """ Create button """
    def createButton(self, frame, size, text, contentPadx, contentPady, padx, pady, width, height, highlightbackground, side, command):
        btnTextFont = font.Font(size=size)
        btnText = ''

        # Check if we get text or unicode
        if type(text) is str:
            btnText = text
        if type(text) is int:
            btnText = chr(text)

        rulesBtn = Button(
            frame, 
            text = btnText, 
            padx=contentPadx, 
            pady=contentPady, 
            width=width, 
            height=height, 
            highlightbackground = highlightbackground, 
            command=command
        )
        rulesBtn['font'] = btnTextFont
        rulesBtn.pack(padx=padx, pady=pady, side=side)


    """ Create pop-up """
    def createPopup(self, title, content):
        showinfo(title, content)


    """ Close main window """
    def closeWindow(self):
        self._root.destroy()


    """ Create canvas for drawing """
    def createCanvas(self, width, height, background):
        canvas = Canvas(self._root, width=width, height=height, background=background, highlightthickness=0)
        canvas.pack(side='left')

        return canvas
    

    """ Create label """
    def createLabel(self, frame, text, side, padx, pady, bgColor):
        label = Label(frame, text=text)  
        label.pack(pady= pady, padx = padx, side=side)                                                                                          
        label.config(bd=5, bg=bgColor)   
        return label              


    """ Method to draw a line on a canvas """
    def drawLine(self, canvas, x1, y1, x2, y2, fillColor, width):
        canvas.create_line(x1,y1,x2,y2, fill=fillColor, width=width) 


    """ Method to draw a circle on a canvas """
    def drawCircle(self, canvas, x1, y1, x2, y2, fillColor, width, outlineColor):
        canvas.create_oval(x1,y1,x2,y2, fill=fillColor, width=width, outline=outlineColor) 




    