# Python Version:   3.8.1
#
# Author:           Samantha Epling
#
# Date:             January 24, 2020
#
# Purpose:          Drill assignment for Step 122 of Python Course,
#                   The Tech Academy, Create a GUI with a button
#                   widget and a text widget that invokes a dialog
#                   modal which allows user to select a folder
#                   directory from their system and show their
#                   selection.
#
# Tested OS:        This code was written and tested to work with
#                   Windows 10


from tkinter import *
import tkinter as tk


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)


        self.master.title("Directory Finder")
        self.master.configure(bg="gainsboro")

        self.btn_browse1 = tk.Button(self.master,width=15,height=1,text="Select",command=lambda: OpenDir(self))
        self.btn_browse1.grid(row=0,column=0,padx=(20,0),pady=(45,0),sticky=W)

        self.txt_1 = tk.Entry(self.master,text='',width=45)
        self.txt_1.grid(row=0,column=1,columnspan=4,padx=(25,0),pady=(45,0),sticky=E)

        self.selection1 = Listbox(self.master,exportselection=0)
        self.selection1.bind('<<ListboxSelect>>',lambda event: PrintDir(self))
        self.selection1.grid(row=2,column=0,rowspan=1,columnspan=5,padx=(20,0),pady=(15,0),sticky=N+E+S+W)

        def OpenDir(self):
            base = Tk()
            base.directory = tkfiledialog.askdirectory()
            def PrintDir(self):
                print(result)
            
            
    
        

            
if __name__== "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
