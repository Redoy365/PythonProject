from tkinter import *
from tkinter import messagebox
import mysql.connector

def Button_func(self):
        def Prescription_add():
             
             if self.Nameoftablets.get() == "" or self.Ref.get() == "":
                messagebox.showerror("Error","All fiels are required")
                
             else:
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
        # ===========================   Button Layout =========================
        # ===========================   Button Layout =========================
        # ===========================   Button Layout =========================
        # ===========================   Button Layout =========================
        Dataframe_btn = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe_btn.place(relx=0, rely=0.65, relheight=0.1, relwidth=1)
        #   Button  1   ==============
        button1 = Button(Dataframe_btn, font=("arial",13,"bold"),padx=10,pady=10,bg="green", fg= "white", text="Prescription")
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
        button6 = Button(Dataframe_btn, font=("arial",13,"bold"),padx=10,pady=10,bg="green", fg= "white", text="Exit")
        button6.place(relx=0.805, rely=0.01, relheight=1, relwidth=0.16)
        #   Button  7   ==============
        button7 = Button(Dataframe_btn, font=("arial",13,"bold"),padx=10,pady=10,bg="green", fg= "red", text="+ H")
        button7.place(relx=0.967, rely=0.01, relheight=1, relwidth=0.03)
