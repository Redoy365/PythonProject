from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1600x800+0+0")
        # =======================   Header  ===========================
        lbltitle = Label(self.root, bd=20, relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman",50,"bold"))
        lbltitle.place(relx=0, rely=0, relheight=0.15, relwidth=1)
        # =======================    Dataframe   =======================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE,height=400)
        Dataframe.place(relx=0, rely=0.15, relheight=0.5, relwidth=1)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,font=("arial",12,"bold"), text="Patient Information")
        DataframeLeft.place(relx=0, rely=0, relheight=1, relwidth=0.6)

        # separator = ttk.Separator(root, orient='vertical')
        # separator.place(relx=0.61, rely=0.2, relwidth=0.009, relheight=0.4)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,font=("arial",12,"bold"), text="Patient Information")
        DataframeLeft.place(relx=0.6, rely=0, relheight=1, relwidth=0.4)
        # ===========================   Button  =========================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(relx=0, rely=0.65, relheight=0.1, relwidth=1)
        # ===========================   DataBase    =====================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(relx=0, rely=0.75, relheight=0.25, relwidth=1)

root = Tk()
ob = Hospital(root)

root.mainloop()