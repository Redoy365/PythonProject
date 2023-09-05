from tkinter import *
from tkinter import ttk

import mysql.connector

def LabelFrame_func(self):
     
        self.Nameoftablets = StringVar()
        self.Ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTables = StringVar()
        self.Lot = StringVar()
        self.IssueDate = StringVar()
        self.Expdate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.FurtherInfo = StringVar()
        self.BloodPressure = StringVar()
        self.Storage = StringVar()
        self.Medication = StringVar()
        self.PretientId = StringVar()
        self.NHSnumber = StringVar()
        self.Pname = StringVar()
        self.DBO = StringVar()
        self.address = StringVar()

 #self.hospital_table = ttk.Treeview(Dataframe_base, columns=("nameoftables","ref","dose","nooftables","lot","issuedate","expdate","dailydose","storage",
   #                                                                 "nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
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

        # =======================    Dataframe Left  =======================
        # =======================    Dataframe Left  =======================
        # =======================    Dataframe Left  =======================
        # Label  1  ==========>
        lblNameTablet = Label(DataframeLeft, text=" Name of Tablets ",anchor="w",  font=("arial", 12, "bold"))
        lblNameTablet.place(relx=0.01, rely=0, relheight=0.09, relwidth=0.20)
        # Combobox  1 ========>
    
        comboNameTable = ttk.Combobox(DataframeLeft,textvariable = self.Nameoftablets, font=("times new roman",12,"bold"))
        comboNameTable["values"] = ("Nice", "Corona Vacacine","Acetaminophen", "Adderall", "Amlodipine", "Ativan","Corona Vacacine","Acetaminophen", "Adderall")
        comboNameTable.current()
        comboNameTable.place(relx=0.20, rely=0, relheight=0.09, relwidth=0.29)
        # Label  2 =========>
        RefenceLayout2 = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Refence No : ",anchor=W, width=18)
        RefenceLayout2.place(relx=0.01, rely=0.11, relheight=0.09, relwidth=0.20)
        RefenceEntry2 = Entry(DataframeLeft,textvariable=self.Ref, font=("times new roman",12,"bold"))#=================Ref
        RefenceEntry2.place(relx=0.20, rely=0.11, relheight=0.09, relwidth=0.29)
        # Label  3 =========>
        RefenceLayout3 = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Dose : ",anchor=W, width=18)
        RefenceLayout3.place(relx=0.01, rely=0.22, relheight=0.09, relwidth=0.20)
        RefenceEntry3 = Entry(DataframeLeft,textvariable=self.Dose, font=("times new roman",12,"bold"))#=================Dose
        RefenceEntry3.place(relx=0.20, rely=0.22, relheight=0.09, relwidth=0.29)
        # Label  4 =========>
        RefenceLayout4 = Label(DataframeLeft, font=("arial", 12, "bold"), text=" No Of Tablets : ",anchor=W, width=18)
        RefenceLayout4.place(relx=0.01, rely=0.33, relheight=0.09, relwidth=0.20)
        RefenceEntry4 = Entry(DataframeLeft, textvariable=self.NumberofTables, font=("times new roman",12,"bold"))#=================Nameoftablets
        RefenceEntry4.place(relx=0.20, rely=0.33, relheight=0.09, relwidth=0.29)
        # Label  5 =========>
        RefenceLayout5 = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Lot : ",anchor=W, width=18)
        RefenceLayout5.place(relx=0.01, rely=0.44, relheight=0.09, relwidth=0.20)
        RefenceEntry5 = Entry(DataframeLeft, textvariable=self.Lot , font=("times new roman",12,"bold"))#====================Lot
        RefenceEntry5.place(relx=0.20, rely=0.44, relheight=0.09, relwidth=0.29)
        # Label  6 =========>
        RefenceLayout6 = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Issue Date : ",anchor=W, width=18)
        RefenceLayout6.place(relx=0.01, rely=0.55, relheight=0.09, relwidth=0.20)
        RefenceEntry6 = Entry(DataframeLeft,textvariable= self.IssueDate, font=("times new roman",12,"bold"))#==============IssueDate
        RefenceEntry6.place(relx=0.20, rely=0.55, relheight=0.09, relwidth=0.29)
        # Label  7 =========>
        RefenceLayout7 = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Exp Date : ",anchor=W, width=18)
        RefenceLayout7.place(relx=0.01, rely=0.66, relheight=0.09, relwidth=0.20)
        RefenceEntry7 = Entry(DataframeLeft, textvariable= self.Expdate, font=("times new roman",12,"bold"))#===============Expdate
        RefenceEntry7.place(relx=0.20, rely=0.66, relheight=0.09, relwidth=0.29)
        # Label  8 =========>
        RefenceLayout8 = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Daily Dose : ",anchor=W, width=18)
        RefenceLayout8.place(relx=0.01, rely=0.77, relheight=0.09, relwidth=0.20)
        RefenceEntry8 = Entry(DataframeLeft,textvariable=self.DailyDose, font=("times new roman",12,"bold"))#================DailyDose
        RefenceEntry8.place(relx=0.20, rely=0.77, relheight=0.09, relwidth=0.29)
        # Label  9 =========>
        RefenceLayout9 = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Side Effect : ",anchor=W, width=18)
        RefenceLayout9.place(relx=0.01, rely=0.88, relheight=0.09, relwidth=0.20)
        RefenceEntry9 = Entry(DataframeLeft,textvariable=self.SideEffect, font=("times new roman",12,"bold"))#===========SideEffect
        RefenceEntry9.place(relx=0.20, rely=0.88, relheight=0.09, relwidth=0.29)
        # =======================    Dataframe Right  =======================
        # =======================    Dataframe Right  =======================
        # =======================    Dataframe Right  =======================
        # Label  1 =========>
        RefenceLayout11 = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Further Information : ",anchor=W, width=18)
        RefenceLayout11.place(relx=0.50, rely=0.0, relheight=0.09, relwidth=0.20)
        RefenceEntry11 = Entry(DataframeLeft,textvariable=self.FurtherInfo, font=("times new roman",12,"bold"))#=============
        RefenceEntry11.place(relx=0.70, rely=0.0, relheight=0.09, relwidth=0.29)
        # Label  2 =========>
        RefenceLayout22 = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Blood Pressure : ",anchor=W, width=18)
        RefenceLayout22.place(relx=0.50, rely=0.11, relheight=0.09, relwidth=0.20)
        RefenceEntry22 = Entry(DataframeLeft,textvariable=self.BloodPressure , font=("times new roman",12,"bold"))#==========BloodPressure
        RefenceEntry22.place(relx=0.70, rely=0.11, relheight=0.09, relwidth=0.29)
        # Label  3 =========>
        RefenceLayout33 = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Storage Advice : ",anchor=W, width=18)
        RefenceLayout33.place(relx=0.50, rely=0.22, relheight=0.09, relwidth=0.20)
        RefenceEntry33 = Entry(DataframeLeft,textvariable=self.Storage ,font=("times new roman",12,"bold"))#=================Storage
        RefenceEntry33.place(relx=0.70, rely=0.22, relheight=0.09, relwidth=0.29)
        # Label  4 =========>
        RefenceLayout44 = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Medication : ",anchor=W, width=18)
        RefenceLayout44.place(relx=0.50, rely=0.33, relheight=0.09, relwidth=0.20)
        RefenceEntry44 = Entry(DataframeLeft,textvariable=self.Medication, font=("times new roman",12,"bold"))#===============Medication
        RefenceEntry44.place(relx=0.70, rely=0.33, relheight=0.09, relwidth=0.29)
        # Label  5 =========>
        RefenceLayout55 = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Patient Id : ",anchor=W, width=18)
        RefenceLayout55.place(relx=0.50, rely=0.44, relheight=0.09, relwidth=0.20)
        RefenceEntry55 = Entry(DataframeLeft,textvariable=self.PretientId, font=("times new roman",12,"bold"))#=============PretientId
        RefenceEntry55.place(relx=0.70, rely=0.44, relheight=0.09, relwidth=0.29)
        # Label  6 =========>
        RefenceLayout66 = Label(DataframeLeft, font=("arial", 12, "bold"), text=" NHS Number : ",anchor=W, width=18)
        RefenceLayout66.place(relx=0.50, rely=0.55, relheight=0.09, relwidth=0.20)
        RefenceEntry66 = Entry(DataframeLeft,textvariable=self.NHSnumber, font=("times new roman",12,"bold"))#======NHSnumber
        RefenceEntry66.place(relx=0.70, rely=0.55, relheight=0.09, relwidth=0.29)
        # Label  7 =========>
        RefenceLayout77 = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Patient Name : ",anchor=W, width=18)
        RefenceLayout77.place(relx=0.50, rely=0.66, relheight=0.09, relwidth=0.20)
        RefenceEntry77 = Entry(DataframeLeft,textvariable=self.Pname, font=("times new roman",12,"bold"))#==========Pname
        RefenceEntry77.place(relx=0.70, rely=0.66, relheight=0.09, relwidth=0.29)
        # Label  8 =========>
        RefenceLayout88 = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Date Of Birth : ",anchor=W, width=18)
        RefenceLayout88.place(relx=0.50, rely=0.77, relheight=0.09, relwidth=0.20)
        RefenceEntry88 = Entry(DataframeLeft,textvariable=self.DBO , font=("times new roman",12,"bold"))#============DBO
        RefenceEntry88.place(relx=0.70, rely=0.77, relheight=0.09, relwidth=0.29)
        # Label  9 =========>
        RefenceLayout99 = Label(DataframeLeft, font=("arial", 12, "bold"), text=" Patient Address : ",anchor=W, width=18)
        RefenceLayout99.place(relx=0.50, rely=0.88, relheight=0.09, relwidth=0.20)
        RefenceEntry99 = Entry(DataframeLeft,textvariable=self.address, font=("times new roman",12,"bold"))#============Address
        RefenceEntry99.place(relx=0.70, rely=0.88, relheight=0.09, relwidth=0.29)

        # =========================   Textview Right  ============================
        # =========================   Textview Right  ============================
        # =========================   Textview Right  ============================

        textview = Text(DataframeRight, font=("times new roman",13,"bold"))
        textview.place(relx=0, rely=0, relheight=1, relwidth=1)
