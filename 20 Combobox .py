from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Test App")
root.geometry("1000x600")
root.iconbitmap("Image/rocket.ico")

combo = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"])
combo.pack()

root.mainloop()