from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import random
import time
import datetime
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1600x800+0+0")
        # =======================   Header Layout ===========================
        lbltitle = Label(self.root, bd=20, relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman",50,"bold"))
        lbltitle.place(relx=0, rely=0, relheight=0.15, relwidth=1)
        # =======================    Dataframe Layout  =======================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE,height=400)
        Dataframe.place(relx=0, rely=0.15, relheight=0.5, relwidth=1)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=0, pady=2, font=("arial",12,"bold"), text="Patient Information")
        DataframeLeft.place(relx=0, rely=0, relheight=1, relwidth=0.6)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,font=("arial",12,"bold"), text="Patient Information")
        DataframeRight.place(relx=0.6, rely=0, relheight=1, relwidth=0.4)
        # ===========================   Button Layout =========================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(relx=0, rely=0.65, relheight=0.1, relwidth=1)
        # ===========================   DataBase  Layout  =====================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(relx=0, rely=0.75, relheight=0.25, relwidth=1)
        # =======================    Dataframe Left  =======================
        # =======================    Dataframe Left  =======================
        # =======================    Dataframe Left  =======================
        # Label  1  ==========>
        lblNameTablet = Label(DataframeLeft, text=" Name of Tablet ",anchor="w",  font=("arial", 12, "bold"))
        lblNameTablet.place(relx=0.01, rely=0, relheight=0.09, relwidth=0.20)
        # Combobox  1 ========>
        n = tk.StringVar()
        comboNameTable = ttk.Combobox(DataframeLeft, font=("times new roman",12,"bold"), textvariable = 0)
        comboNameTable["values"] = ("Nice", "Corona Vacacine","Acetaminophen", "Adderall", "Amlodipine", "Ativan","Corona Vacacine","Acetaminophen", "Adderall")
        comboNameTable.current()
        comboNameTable.place(relx=0.20, rely=0, relheight=0.09, relwidth=0.29)
        # Label  2 =========>
        RefenceLayout = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Refence No : ",anchor=W, width=18)
        RefenceLayout.place(relx=0.01, rely=0.11, relheight=0.09, relwidth=0.20)
        # Entry  2 =========>
        RefenceEntry = Entry(DataframeLeft, font=("times new roman",12,"bold"))
        RefenceEntry.place(relx=0.20, rely=0.11, relheight=0.09, relwidth=0.29)
        # Label  3 =========>
        RefenceLayout = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Refence No : ",anchor=W, width=18)
        RefenceLayout.place(relx=0.01, rely=0.22, relheight=0.09, relwidth=0.20)
        # Entry  3 =========>
        RefenceEntry = Entry(DataframeLeft, font=("times new roman",12,"bold"))
        RefenceEntry.place(relx=0.20, rely=0.22, relheight=0.09, relwidth=0.29)
        # Label  4 =========>
        RefenceLayout = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Refence No : ",anchor=W, width=18)
        RefenceLayout.place(relx=0.01, rely=0.33, relheight=0.09, relwidth=0.20)
        # Entry  4 =========>
        RefenceEntry = Entry(DataframeLeft, font=("times new roman",12,"bold"))
        RefenceEntry.place(relx=0.20, rely=0.33, relheight=0.09, relwidth=0.29)
        # Label  5 =========>
        RefenceLayout = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Refence No : ",anchor=W, width=18)
        RefenceLayout.place(relx=0.01, rely=0.44, relheight=0.09, relwidth=0.20)
        # Entry  5 =========>
        RefenceEntry = Entry(DataframeLeft, font=("times new roman",12,"bold"))
        RefenceEntry.place(relx=0.20, rely=0.44, relheight=0.09, relwidth=0.29)
        # Label  6 =========>
        RefenceLayout = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Refence No : ",anchor=W, width=18)
        RefenceLayout.place(relx=0.01, rely=0.55, relheight=0.09, relwidth=0.20)
        # Entry  6 =========>
        RefenceEntry = Entry(DataframeLeft, font=("times new roman",12,"bold"))
        RefenceEntry.place(relx=0.20, rely=0.55, relheight=0.09, relwidth=0.29)
        # Label  7 =========>
        RefenceLayout = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Refence No : ",anchor=W, width=18)
        RefenceLayout.place(relx=0.01, rely=0.66, relheight=0.09, relwidth=0.20)
        # Entry  7 =========>
        RefenceEntry = Entry(DataframeLeft, font=("times new roman",12,"bold"))
        RefenceEntry.place(relx=0.20, rely=0.66, relheight=0.09, relwidth=0.29)
        # Label  8 =========>
        RefenceLayout = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Refence No : ",anchor=W, width=18)
        RefenceLayout.place(relx=0.01, rely=0.77, relheight=0.09, relwidth=0.20)
        # Entry  8 =========>
        RefenceEntry = Entry(DataframeLeft, font=("times new roman",12,"bold"))
        RefenceEntry.place(relx=0.20, rely=0.77, relheight=0.09, relwidth=0.29)
        # Label  9 =========>
        RefenceLayout = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Refence No : ",anchor=W, width=18)
        RefenceLayout.place(relx=0.01, rely=0.88, relheight=0.09, relwidth=0.20)
        # Entry  9 =========>
        RefenceEntry = Entry(DataframeLeft, font=("times new roman",12,"bold"))
        RefenceEntry.place(relx=0.20, rely=0.88, relheight=0.09, relwidth=0.29)
        # =======================    Dataframe Right  =======================
        # =======================    Dataframe Right  =======================
        # =======================    Dataframe Right  =======================
        # Label  1 =========>
        RefenceLayout = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Future Informatopn : ",anchor=W, width=18)
        RefenceLayout.place(relx=0.50, rely=0.0, relheight=0.09, relwidth=0.20)
        # Entry  1 =========>
        RefenceEntry = Entry(DataframeLeft, font=("times new roman",12,"bold"))
        RefenceEntry.place(relx=0.70, rely=0.0, relheight=0.09, relwidth=0.29)
        # Label  2 =========>
        RefenceLayout = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Future Informatopn : ",anchor=W, width=18)
        RefenceLayout.place(relx=0.50, rely=0.11, relheight=0.09, relwidth=0.20)
        # Entry  2 =========>
        RefenceEntry = Entry(DataframeLeft, font=("times new roman",12,"bold"))
        RefenceEntry.place(relx=0.70, rely=0.11, relheight=0.09, relwidth=0.29)
        # Label  3 =========>
        RefenceLayout = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Future Informatopn : ",anchor=W, width=18)
        RefenceLayout.place(relx=0.50, rely=0.22, relheight=0.09, relwidth=0.20)
        # Entry  3 =========>
        RefenceEntry = Entry(DataframeLeft, font=("times new roman",12,"bold"))
        RefenceEntry.place(relx=0.70, rely=0.22, relheight=0.09, relwidth=0.29)
        # Label  4 =========>
        RefenceLayout = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Future Informatopn : ",anchor=W, width=18)
        RefenceLayout.place(relx=0.50, rely=0.33, relheight=0.09, relwidth=0.20)
        # Entry  4 =========>
        RefenceEntry = Entry(DataframeLeft, font=("times new roman",12,"bold"))
        RefenceEntry.place(relx=0.70, rely=0.33, relheight=0.09, relwidth=0.29)
        # Label  5 =========>
        RefenceLayout = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Future Informatopn : ",anchor=W, width=18)
        RefenceLayout.place(relx=0.50, rely=0.44, relheight=0.09, relwidth=0.20)
        # Entry  5 =========>
        RefenceEntry = Entry(DataframeLeft, font=("times new roman",12,"bold"))
        RefenceEntry.place(relx=0.70, rely=0.44, relheight=0.09, relwidth=0.29)
        # Label  6 =========>
        RefenceLayout = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Future Informatopn : ",anchor=W, width=18)
        RefenceLayout.place(relx=0.50, rely=0.55, relheight=0.09, relwidth=0.20)
        # Entry  6 =========>
        RefenceEntry = Entry(DataframeLeft, font=("times new roman",12,"bold"))
        RefenceEntry.place(relx=0.70, rely=0.55, relheight=0.09, relwidth=0.29)
        # Label  7 =========>
        RefenceLayout = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Future Informatopn : ",anchor=W, width=18)
        RefenceLayout.place(relx=0.50, rely=0.66, relheight=0.09, relwidth=0.20)
        # Entry  7 =========>
        RefenceEntry = Entry(DataframeLeft, font=("times new roman",12,"bold"))
        RefenceEntry.place(relx=0.70, rely=0.66, relheight=0.09, relwidth=0.29)
        # Label  8 =========>
        RefenceLayout = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Future Informatopn : ",anchor=W, width=18)
        RefenceLayout.place(relx=0.50, rely=0.77, relheight=0.09, relwidth=0.20)
        # Entry  8 =========>
        RefenceEntry = Entry(DataframeLeft, font=("times new roman",12,"bold"))
        RefenceEntry.place(relx=0.70, rely=0.77, relheight=0.09, relwidth=0.29)
        # Label  9 =========>
        RefenceLayout = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Future Informatopn : ",anchor=W, width=18)
        RefenceLayout.place(relx=0.50, rely=0.88, relheight=0.09, relwidth=0.20)
        # Entry  9 =========>
        RefenceEntry = Entry(DataframeLeft, font=("times new roman",12,"bold"))
        RefenceEntry.place(relx=0.70, rely=0.88, relheight=0.09, relwidth=0.29)




root = Tk()
ob = Hospital(root)

root.mainloop()