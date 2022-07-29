import logging
import tkinter as tk
from tkinter import *
from tkinter import ttk

# logging options
logging.basicConfig(level=logging.INFO, format='(%(levelname)-s) %(asctime)s %(message)s', datefmt='%d-%m %H:%M:%S')


class Font():
    # define tuples containing Font data
    title = ('Verdana', 25, 'bold')
    subtitle = ('Calibri', 16, 'bold')
    textbox = ('Calibri', 14)
    entry = ('Calibri', 14, 'bold')
    color_entry = '#464646'

class Variables():
    # define gui variables here to be accessed by any object
    padx = 5
    pady = 2

class Mainloop(tk.Tk): # inherit from tk.Tk()
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) # inherit tk.Tk().__init__
        tk.Tk.wm_title(self, 'AutoCOSHH v4')
        logging.info('Main window instantiated')
        
        # instantiate ttk parent container
        parent_container = ttk.Frame(self, padding='6 3 6 6')
        parent_container.grid(column=0, row=0, sticky=NSEW)
        parent_container.rowconfigure(0, weight=1)
        parent_container.columnconfigure(0, weight=1)

        # instantiate ttk.Frame objects (pages)
        self.mainpage = MainPage(parent_container, self)
        self.formdetails = SecondaryPage(parent_container, self)
        
        # configure ttk.Frame objects
        self.formdetails.grid(row=0, column=0, sticky=NSEW)
        self.mainpage.grid(row=0, column=0, sticky=NSEW)
        
        # create pages dictionary for navigation
        self.frames = { MainPage: self.mainpage, FormDetailsPage: self.formdetails }
        
        # call go to page function
        self.show_frame(MainPage)

    # define go to page function
    def show_frame(self, controller):
        frame = self.frames[controller]
        frame.tkraise()
        logging.info(f'{controller.__name__} object raised')

    # define program functions here and call them using controller.func() from given page


class MainPage(ttk.Frame): # inherit from ttk.Frame() class
    '''MainPage object'''
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent) # inherit ttk.Frame.__init__

        # page content here

class FormDetailsPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        # page content here


app = AutoCoshh()
app.mainloop()
