from tkinter import *

root = Tk()
root.title("Test App")
root.geometry("1000x600")
root.iconbitmap("Image/rocket.ico")


Dataframe = Frame(root, bd=20, relief=RIDGE,height=400)
Dataframe.place(relx=0, rely=0.15, relheight=0.5, relwidth=1)


root.mainloop()