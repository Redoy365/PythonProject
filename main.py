from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import random
import time
import datetime
import webbrowser
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1600x800+0+0")
        self.root.iconbitmap("icon.ico")

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
        # ===========================   Button Layout =========================
        Dataframe_btn = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe_btn.place(relx=0, rely=0.65, relheight=0.1, relwidth=1)
        
        # ===========================   DataBase  Layout  =====================
        Dataframe_base = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe_base.place(relx=0, rely=0.75, relheight=0.25, relwidth=1)

        def fetch_all_data():
            conn = mysql.connector.connect(host = "localhost",username = "Redoy365",password="a4t23zaRedoy", database = "mydata")
            my_Cursor = conn.cursor()
            my_Cursor.execute("SELECT * FROM hospital")
            myresult = my_Cursor.fetchall()

            for x in myresult:
                print(x)

        
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

        # =========================   Textview Right ============================
        # =========================   Textview Right ============================
        # =========================   Textview Right ============================

        textview = Text(DataframeRight, font=("times new roman",13,"bold"))
        textview.place(relx=0, rely=0, relheight=1, relwidth=1)


        #===========================================  Functionality Declaration ==================================
        #===========================================  Functionality Declaration ==================================
        #===========================================  Functionality Declaration ==================================

        def Prescription_add():
             print("in function")
             if self.Nameoftablets.get() == "" or self.Ref.get() == "":
                print("in if")
                messagebox.showerror("Error","All fiels are required")
             else:
                print("in else")
                conn = mysql.connector.connect(host = "localhost",username = "Redoy365",password="a4t23zaRedoy", database = "mydata")
                my_Cursor = conn.cursor()
                my_Cursor.execute("INSERT INTO hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                                        self.Nameoftablets.get(),
                                                                                                        self.Ref.get(),
                                                                                                        self.Dose.get(),
                                                                                                        self.NumberofTables.get(),
                                                                                                        self.Lot.get(),
                                                                                                        self.IssueDate.get(),
                                                                                                        self.Expdate.get(),
                                                                                                        self.DailyDose.get(),
                                                                                                        self.Storage.get(),
                                                                                                        self.NHSnumber.get(),
                                                                                                        self.Pname.get(),
                                                                                                        self.DBO.get(),
                                                                                                        self.address.get()
                                                                                                        ))
                
                conn.commit()
                conn.close()

                self.Nameoftablets.set("")
                self.Ref.set("")
                self.Dose.set("")
                self.NumberofTables.set("")
                self.Lot.set("")
                self.IssueDate.set("")
                self.Expdate.set("")
                self.DailyDose.set("")
                self.Storage.set("")
                self.NHSnumber.set("")
                self.Pname.set("")
                self.DBO.set("")
                self.address.set("")
                self.SideEffect.set("")
                self.FurtherInfo.set("")
                self.BloodPressure.set("")
                self.Medication.set("")
                self.PretientId.set("")
                messagebox.showinfo("Record Hase been inserted")


        
        def Reset_para():
            self.Nameoftablets.set("")
            self.Ref.set("")
            self.Dose.set("")
            self.NumberofTables.set("")
            self.Lot.set("")
            self.IssueDate.set("")
            self.Expdate.set("")
            self.DailyDose.set("")
            self.Storage.set("")
            self.NHSnumber.set("")
            self.Pname.set("")
            self.DBO.set("")
            self.address.set("")
            self.SideEffect.set("")
            self.FurtherInfo.set("")
            self.BloodPressure.set("")
            self.Medication.set("")
            self.PretientId.set("")
           
            messagebox.showinfo("Reset successful")

        def func(self):
            x = messagebox.askquestion("askquestion", "Are you sure?")
            
            if x == "yes":
                print("Yes")
            else:
                print("No")
                

        def Prescription_show(self):
            conn = mysql.connector.connect(host = "localhost",username = "Redoy365",password="a4t23zaRedoy", database = "mydata")
            my_Cursor = conn.cursor()
            my_Cursor.execute("SELECT * FROM hospital")
            rows = my_Cursor.fetchall()
            
            if len(rows) != 0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for i in rows:
                    self.hospital_table.insert("",END, values=i)
                conn.commit()
            conn.close()
            
        
            

                    # ===========================   Button Layout =========================
                    # ===========================   Button Layout =========================
                    # ===========================   Button Layout =========================

        #   Button  1   ==============
        button1 = Button(Dataframe_btn, font=("arial",13,"bold"),padx=10,pady=10,bg="green", fg= "white", text="Prescription", command=Prescription_show)
        button1.place(relx=0, rely=0.01, relheight=1, relwidth=0.16)
        #   Button  2   ==============
        button2 = Button(Dataframe_btn, font=("arial",13,"bold"),padx=10,pady=10,bg="green", fg= "white", text="Prescription Add", command=Prescription_add)
        button2.place(relx=0.161, rely=0.01, relheight=1, relwidth=0.16)
        #   Button  3   ==============
        button3 = Button(Dataframe_btn, font=("arial",13,"bold"),padx=10,pady=10,bg="green", fg= "white", text="Update")
        button3.place(relx=0.322, rely=0.01, relheight=1, relwidth=0.16)
        #   Button  4   ==============
        button4 = Button(Dataframe_btn, font=("arial",13,"bold"),padx=10,pady=10,bg="green", fg= "white", text="Delete")
        button4.place(relx=0.483, rely=0.01, relheight=1, relwidth=0.16)
        #   Button  5   ==============
        button5 = Button(Dataframe_btn, font=("arial",13,"bold"),padx=10,pady=10,bg="green", fg= "white", text="Clear", command=Reset_para)
        button5.place(relx=0.644, rely=0.01, relheight=1, relwidth=0.16)
        #   Button  6   ==============
        button6 = Button(Dataframe_btn, font=("arial",13,"bold"),padx=10,pady=10,bg="green", fg= "white", text="Exit", command=func)
        button6.place(relx=0.805, rely=0.01, relheight=1, relwidth=0.16)
        #   Button  7   ==============
        button7 = Button(Dataframe_btn, font=("arial",13,"bold"),padx=10,pady=10,bg="green", fg= "red", text="+ H")
        button7.place(relx=0.967, rely=0.01, relheight=1, relwidth=0.03)

        # ========================================  Table   Table   Table   Table ===================================
        # ========================================  Table   Table   Table   Table ===================================
        # ========================================  Table   Table   Table   Table ===================================
        scroll_x = ttk.Scrollbar(Dataframe_base, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Dataframe_base, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Dataframe_base, columns=("nameoftables","ref","dose","nooftables","lot","issuedate","expdate","dailydose","storage",
                                                                    "nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftables", text="Name of Tables")
        self.hospital_table.heading("ref", text="Reference No : ")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftables", text="No Of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"] = "headings"

        self.hospital_table.column("nameoftables",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftables",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        # self.Prescription_pair()
        self.hospital_table.pack(fill=BOTH, expand=1)

        
        # ======================================================
        # ======================================================
        # ======================================================
        mydatabase_ = mysql.connector.connect(
        host = "localhost",
        username = "Redoy365",
        password = "a4t23zaRedoy",
        database = "mydata"
        )

        mycursor = mydatabase_.cursor()

        mycursor.execute("SELECT * FROM hospital")

        myresult = mycursor.fetchall()
        print(myresult[0])

        i=1
        for x in myresult:

            self.hospital_table.insert('',i,text="",values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12]))
            i=i+1

        self.hospital_table.pack()

           
root = Tk()
ob = Hospital(root)
# ================================================ MenuBar MenuBar MenuBar =============================================
# ================================================ MenuBar MenuBar MenuBar =============================================
# ================================================ MenuBar MenuBar MenuBar =============================================
# ================================================ MenuBar MenuBar MenuBar =============================================
# ================================================ MenuBar MenuBar MenuBar =============================================
# ============================================
# ============================================
def viewhelp():
    webbrowser.open(
        "https://www.bing.com/search?q=get+help+with+notepad+in+windows&filters=guid:%224466414-en-dia%22%20lang:%22en%22&form=T00032&ocid=HelpPane-BingIA"
    )

menubar = Menu(root)
# ================= file file ============================
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)
# __________________________________________
file.add_command(label="New", accelerator="Ctrl+N")
file.add_command(label="New Window", command=None, accelerator="Ctrl+Shift+N")

sub_file_open = Menu(file, tearoff=0)
sub_file_open.add_command(label="Open File", command="None")
sub_file_open.add_command(label="Open Folder", command="None")
file.add_cascade(label="Open ..", menu=sub_file_open)

file.add_command(label="Save", command=None, accelerator="Ctrl+S")
file.add_command(label="Save As ..", command=None, accelerator="Ctrl+Shift+S")
file.add_separator()
file.add_command(label="Page Setup .. ", command=None)
file.add_command(label="Print .. ", command=None, accelerator="Ctrl+P")
file.add_separator()
file.add_command(label="Exit", command=exit, accelerator="Ctrl+W")

# ==================== edit edit =============================================
edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit)
# __________________________________________________________________
edit.add_command(label="Undo", command="None", accelerator="Ctrl+Z")
edit.add_command(label="Redo", command="None", accelerator="Ctrl+Y")
edit.add_separator()
edit.add_command(label="Cut", command="None", accelerator="Ctrl+X")
edit.add_command(label="Copy", command="None", accelerator="Ctrl+C")
edit.add_command(label="Past", command="None", accelerator="Ctrl+V")
edit.add_command(label="Delete", command="None", accelerator="Del")
edit.add_separator()
edit.add_command(label="Search With Bing .. ", command="None", accelerator="Ctrl+E")
edit.add_command(label="Find .. ", command="None", accelerator="Ctrl+F")
edit.add_command(label="Find Next", command="None", accelerator="F3")
edit.add_command(label="Find Previous", command="None", accelerator="Shift+F3")
edit.add_command(label="Go To .. ", command="None", accelerator="Ctrl+G")
edit.add_separator()
edit.add_command(label="Select All", command="None", accelerator="Ctrl+A")
edit.add_command(label="Time Date", command="None", accelerator="F5")
# ========================== format format ================================================
formate = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Format", menu=formate)
# __________________________________________________________
formate.add_checkbutton(label="Word Wrap")
formate.add_command(label="Font")
# ============================= view view =============================================
view = Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=view)
# -----------------------------------------------
#
sub_view = Menu(view, tearoff=0)
sub_view.add_command(label="Zoom In", command="None")
sub_view.add_command(label="Zoom Out", command="None")

view.add_cascade(label="Zoom", menu=sub_view)
#
view.add_checkbutton(label="Status Bar", command="None")
# ==========================================================================
help = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help)
# _____________________________________________________------
help.add_command(label="View Help", command=viewhelp)
help.add_command(label="Send Feedback", command="None")
help.add_separator()
help.add_command(label="About Nodebook", command="None")

root.config(menu=menubar)

# =================================================================================================
# tk_popup()    tk_popup()    tk_popup()    tk_popup()    tk_popup()    tk_popup()    tk_popup()
# =================================================================================================

m = Menu(root, tearoff = 0)
m.add_command(label ="Cut")
m.add_command(label ="Copy")
m.add_command(label ="Paste")
m.add_command(label ="Reload")
m.add_separator()
m.add_command(label ="Rename")

def do_popup(event):
	try:
		m.tk_popup(event.x_root, event.y_root)
	finally:
		m.grab_release()

root.bind("<Button-3>", do_popup)

root.mainloop()
