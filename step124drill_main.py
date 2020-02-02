# Python Version:   3.8.1
#
# Author:           Samantha Epling
#
# Date:             January 31, 2020
#
#                   Total Drill Annihilation
#
# Purpose:          Step 124, Drill assignment combine all previous drills,
#                   to create one monster GUI that browses, selects, and
#                   records specific .txt files in directories.
#
# Tested OS:        This code was written and tested to work with
#                   Windows 10

import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import sqlite3
from shutil import *
from shutil import move


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(800,300)
        self.master.maxsize(800,300)


        self.master.title("Monster Directory Finder")
        self.master.config(bg="gainsboro")

        self.lbl_fname = tk.Label(self.master,text='Source directory:',bg="gainsboro")
        self.lbl_fname.grid(row=0,column=0,padx=(20,0),pady=(15,0),sticky=W)
        self.lbl_lname = tk.Label(self.master,text='Destination directory:',bg="gainsboro")
        self.lbl_lname.grid(row=2,column=0,padx=(20,0),pady=(15,0),sticky=W)

        self.btn_browse1 = tk.Button(self.master,width=15,height=1,text="Browse...", \
                                     command=lambda: self.OpenDir1())
        self.btn_browse1.grid(row=1,column=0,padx=(20,0),pady=(15,0),sticky=W)
        self.btn_browse2 = tk.Button(self.master,width=15,height=1,text="Browse...", \
                                     command=lambda: self.OpenDir2())
        self.btn_browse2.grid(row=3,column=0,padx=(20,0),pady=(15,0),sticky=W)
        self.btn_check = tk.Button(self.master,width=15,height=2,text="Check for .txt files...", \
                                   command=lambda: self.ChooseFile())
        self.btn_check.grid(row=4,column=0,padx=(20,0),pady=(30,0),sticky=W)
        self.btn_close = tk.Button(self.master,width=15,height=2,text="Close Program")
        self.btn_close.grid(row=4,column=4,columnspan=1,padx=(25,0),pady=(30,0),sticky=E)

        self.varDirectName1 = StringVar()
        self.txt_1 = tk.Entry(self.master,text=self.varDirectName1,width=85)
        self.txt_1.grid(row=1,column=1,columnspan=4,padx=(25,0),pady=(15,0),sticky=E)
        self.varDirectName2 = StringVar()
        self.txt_2 = tk.Entry(self.master,text=self.varDirectName2,width=85)
        self.txt_2.grid(row=3,column=1,columnspan=4,padx=(25,0),pady=(15,0),sticky=E)

    def OpenDir1(self):
        self.varsavedDirectName1 = filedialog.askdirectory()
        self.varDirectName1.set(self.varsavedDirectName1)
        print(self.varDirectName1.get())

    def OpenDir2(self):
        self.varsavedDirectName2 = filedialog.askdirectory()
        self.varDirectName2.set(self.varsavedDirectName2)
        print(self.varDirectName2.get())
        
    conn = sqlite3.connect('txtfile.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, col_ftypes TEXT, \
            col_ftimestamp INTEGER)")
        conn.commit()
    conn.close()

    def ChooseFile(self):
        fPath = self.varsavedDirectName1
        for file_name in os.listdir(fPath):
            if file_name.endswith(".txt"):
                txtfile = file_name
                abPath = os.path.join(fPath, txtfile)
                varTXTPath = abPath
                varTSTXTfile = os.path.getmtime(abPath)
                print(varTXTPath)
                print(varTSTXTfile)
                self.CloneFile()
                print('this is my CloneFile function running')

    def CloneFile(self):
        varTXTPath = StringVar()
        varTXTPath.shutil.move(self.varsavedDirectName1, self.varsavedDirectName2)
        print('this is my CloneFile function running')
                    
    conn = sqlite3.connect('txtfile.db')
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_files(col_ftypes, col_ftimestamp) VALUES (?,?)",\
                    (varTXTPath, varTSTXTfile))
        conn.commit()
    conn.close()       

if __name__== "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
