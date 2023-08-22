from tkinter import *

root = Tk()
root.title("Test App")
root.geometry("1000x600")

label1 = Label(root, text="Label 1").grid(row=0, column=0)

label2 = Label(root, text="Label 2").grid(row=0, column=1)




root.mainloop()