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
        lbltitle.pack(side=TOP, fill=X)
        # =======================    Dataframe   =======================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE,height=400)
        Dataframe.pack(side=TOP, fill=X)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,font=("arial",12,"bold"), text="Patient Information")
        DataframeLeft.place(relwidth=0.6,height=350)

        # separator = ttk.Separator(root, orient='vertical')
        # separator.place(relx=0.61, rely=0.2, relwidth=0.009, relheight=0.4)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,font=("arial",12,"bold"), text="Patient Information")
        DataframeLeft.place(relx=0.6,rely=0,relwidth=0.4,height=350)

root = Tk()
ob = Hospital(root)

root.mainloop()