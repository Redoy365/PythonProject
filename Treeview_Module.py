from tkinter import *
from tkinter import ttk
import mysql.connector

def Treeview_func(self):
                # ===========================   DataBase  Layout  =====================
        Dataframe_base = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe_base.place(relx=0, rely=0.75, relheight=0.25, relwidth=1)
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

        mydatabase_ = mysql.connector.connect(
        host = "localhost",
        username = "Redoy365",
        password = "a4t23zaRedoy",
        database = "mydata"
        )

        mycursor = mydatabase_.cursor()

        mycursor.execute("SELECT * FROM hospital")

        myresult = mycursor.fetchall()

        i=1
        for x in myresult:

            self.hospital_table.insert('',i,text="",values=(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12]))
            i=i+1

        self.hospital_table.pack()

