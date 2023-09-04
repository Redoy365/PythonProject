from tkinter import *

root = Tk()
root.title("Test App")
root.geometry("1000x600")
root.iconbitmap("Image/rocket.ico")


sp = Spinbox(root, from_= 0, to = 20)
sp.pack()

root.mainloop()