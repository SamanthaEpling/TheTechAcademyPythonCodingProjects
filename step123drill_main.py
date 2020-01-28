# Python Version:   3.8.1
#
# Author:           Samantha Epling
#
# Date:             January 27, 2020
#
# Purpose:          Drill assignment for Step 123 of Python Course,
#                   The Tech Academy, Create a GUI with a button
#                   widget and a text widget that invokes a dialog
#                   modal which allows user to select a folder
#                   directory from their system and show their
#                   selection.
#
# Tested OS:        This code was written and tested to work with
#                   Windows 10

import tkinter as tk
from tkinter import *
from tkinter import filedialog


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(800,200)
        self.master.maxsize(800,200)


        self.master.title("Directory Finder")
        self.master.config(bg="gainsboro")

        self.btn_browse1 = tk.Button(self.master,width=15,height=1,text="Select Directory", command=lambda: self.OpenDir())
        self.btn_browse1.grid(row=0,column=0,padx=(20,0),pady=(45,0),sticky=W)

        self.varDirectName = StringVar()
        self.txt_1 = tk.Entry(self.master,text=self.varDirectName,width=85)
        self.txt_1.grid(row=0,column=1,columnspan=4,padx=(25,0),pady=(45,0),sticky=E)
    
    def OpenDir(self):
        self.varsavedDirectName = filedialog.askdirectory()
        self.varDirectName.set(self.varsavedDirectName)
        print(self.varDirectName.get())

          
if __name__== "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
