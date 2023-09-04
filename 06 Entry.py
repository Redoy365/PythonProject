from tkinter import *

root = Tk()
root.title("Test App")
root.geometry("1000x600")
root.iconbitmap("Image/rocket.ico")

entry1 = Entry(root, font=("arial",20,"bold"))
entry1.pack()

entry2 = Entry(root, font=("arial",20,"bold"), bd=10)
entry2.pack()

entry3 = Entry(root, font=("arial",20,"bold"), bd=10, show="*")
entry3.pack()

entry4 = Entry(root, font=("arial",20,"bold"),bd=1, justify=CENTER)
entry4.pack()

entry5 = Entry(root, font=("arial",20,"bold"), bd=1, justify=RIGHT, relief=RAISED)
entry5.pack()


root.mainloop()