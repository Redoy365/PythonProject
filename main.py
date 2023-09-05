from tkinter import *
from tkinter import ttk
from tkinter import messagebox
# my Module ===================
from Menu_Module import *
from Button_Module import *
from Treeview_Module import *
from LabelFrame_Module import *
# my Module ===================
import tkinter as tk

class Hospital:
    def __init__(self, root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1600x800+0+0")
        self.root.iconbitmap("G:\Python Tutorial W3\Python Mega Project\Hospital Managment System Mysql DB\icon.ico")

        Treeview_func(self)    #   Treeview_Module.py

        Button_func(self)   #   Button_Module.py

        LabelFrame_func(self)   #   LabelFrame_Module.py

        Menubar_func(root)   #   Menu_Module.py
       
root = Tk()
ob = Hospital(root)

myFrame = tk.Frame()
myFrame.pack()
root.mainloop()
