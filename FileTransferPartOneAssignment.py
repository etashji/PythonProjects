import shutil
import os
from tkinter import filedialog
from tkinter import *
import tkinter as tk

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.config(bg = 'lightgray')

        self.lblSource = Label (self.master, text = 'Choose Your source folder:', font = ("Helvetica", 16), fg = 'black', bg = 'lightgray')
        self.lblSource.grid(row = 0, column = 0, padx = (30,0), pady = (30,0))

        self.btnSource = Button(self.master, text = "Browse", width = 10, height = 2, command = self.source)
        self.btnSource.grid(row = 1, column = 0, padx = (30,0), pady = (30,0))

        self.lblDestination = Label (self.master, text = 'Choose Your destination folder:', font = ("Helvetica", 16), fg = 'black', bg = 'lightgray')
        self.lblDestination.grid(row = 2, column = 0, padx = (30,0), pady = (30,0))

        self.btnDestination = Button(self.master, text = "Browse", width = 10, height = 2, command = self.destination)
        self.btnDestination.grid(row = 3, column = 0, padx = (30,0), pady = (30,0))

        self.lblCheck = Label (self.master, text = 'Initiate Check:', font = ("Helvetica", 16), fg = 'black', bg = 'lightgray')
        self.lblCheck.grid(row = 4, column = 0, padx = (30,0), pady = (30,0))

        self.btnCheck = Button(self.master, text = "Browse", width = 10, height = 2, command = self.check)
        self.btnCheck.grid(row = 5, column = 0, padx = (30,0), pady = (30,0))

    #set where the source of the files are
    def source(self):
        global folder_path
        source = filedialog.askdirectory()
        folder_path.set(source)
        files = os.listdir(source)

    def destination (self):
        global folder_path
        destination = filedialog.askdirectory()
        folder_path.set(destination)
        

    def check (self):
        files = os.listdir(source)
        for i in files:
            time = os.path.getmtime(i)
            if time.hour <= 24:
                shutil.move(source+i, destination)

if __name__ == "__main__":
    root = Tk()
    folder_path = StringVar()
    App = ParentWindow(root)
    root.mainloop()
