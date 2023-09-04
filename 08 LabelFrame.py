from tkinter import *

root = Tk()
root.title("Test App")
root.geometry("1000x600")
root.iconbitmap("Image/rocket.ico")

DataframeLeft = LabelFrame(root, bd=10, relief=RIDGE, padx=0, pady=2, font=("arial",12,"bold"), text="Patient Information")
DataframeLeft.place(relx=0, rely=0, relheight=1, relwidth=0.6)

root.mainloop()