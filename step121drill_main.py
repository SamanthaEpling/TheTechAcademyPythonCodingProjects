# Python Version:   3.8.1
#
# Author:           Samantha Epling
#
# Date:             January 24, 2020
#
# Purpose:          Drill assignment for Step 121 of Python Course,
#                   The Tech Academy, Recreate a provided image of a
#                   GUI using Python 3 and the Tkinter module.
#
# Tested OS:        This code was written and tested to work with
#                   Windows 10


from tkinter import *
import tkinter as tk

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,200)
        self.master.maxsize(500,200)


        self.master.title("Check files")
        self.master.configure(bg="gainsboro")

        self.btn_browse1 = tk.Button(self.master,width=15,height=1,text="Browse...")
        self.btn_browse1.grid(row=0,column=0,padx=(20,0),pady=(45,0),sticky=W)
        self.btn_browse2 = tk.Button(self.master,width=15,height=1,text="Browse...")
        self.btn_browse2.grid(row=1,column=0,padx=(20,0),pady=(15,0),sticky=W)
        self.btn_check = tk.Button(self.master,width=15,height=2,text="Check for files...")
        self.btn_check.grid(row=2,column=0,padx=(20,0),pady=(15,0),sticky=W)
        self.btn_close = tk.Button(self.master,width=15,height=2,text="Close Program")
        self.btn_close.grid(row=2,column=4,columnspan=1,padx=(25,0),pady=(15,0),sticky=E)

        self.txt_1 = tk.Entry(self.master,text='',width=45)
        self.txt_1.grid(row=0,column=1,columnspan=4,padx=(25,0),pady=(45,0),sticky=E)
        self.txt_2 = tk.Entry(self.master,text='',width=45)
        self.txt_2.grid(row=1,column=1,columnspan=4,padx=(25,0),pady=(15,0),sticky=E)
        
        
if __name__== "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
