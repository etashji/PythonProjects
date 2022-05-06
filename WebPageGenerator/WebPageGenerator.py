from tkinter import * # This imports everything from tkinter
import tkinter as tk # This assigns a labelt to tkinter as tk
import webbrowser as browser # This imports the webbrowser module

class ParentWindow(Frame): #This creates the class that contains all the content for creating the program
    def __init__ (self, master): # This initializes the tkinter gui
        Frame.__init__ (self) 

        self.varContent = StringVar() # This saves the varContent variable as StringVar()
        
        self.master = master #This saves the master
        self.master.resizable(width = False, height = False) # This makes the form not resizeable
        self.master.geometry('{}x{}'.format(700, 400)) #This sets the dimension of the form
        self.master.config(bg = 'lightgray') #This sets the background of the form

        self.lbl_content = Label(self.master, text = "What do you want your website to say?", font = ("Times New Roman", 16)) # This creates the first label
        self.lbl_content.grid(row = 0, column = 0, padx = (30,0), pady = (30,0)) # This creates the grid for the label

        self.txtContent = Entry(self.master, text = self.varContent, font = ("Helvetica", 16), fg = 'black', bg = 'lightgray') #This creates the input for the content
        self.txtContent.grid(row = 1, column = 0, pady = (30, 0))# This assigns the grid for the content.

        self.btnSubmit = Button(self.master, text = "Create Website", width = 10, height = 2, command = self.submit) # This creates a button to create the website
        self.btnSubmit.grid(row = 2, column = 0, sticky = NE) # This assigns the grid for the button
 
    def submit(self): # This creates the submit function for use with the button
        cn = self.varContent.get() # This assigns the user's input from the form as a variable.
        f = open("main.html", "w") # This opens the main.html form.
        f.truncate() # This truncates the form, and eliminates all previous content in the form.
        f = open("main.html", "a") # This allows the form to be appended
        f.write(cn) # This writes the user's content to the form.

        my_browser = browser.get('windows-default') # This gets the user's default web browser.
        my_browser.open_new('main.html') # This opens the file in the user's browser.

        

if __name__ == "__main__": #This initializes all the code.
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

       
