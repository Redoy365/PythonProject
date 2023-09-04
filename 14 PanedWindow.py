from tkinter import *
from tkinter import ttk

root = Tk()
root.title("PanedWindow")
root.geometry("1000x600")
root.iconbitmap("Image/rocket.ico")


style = ttk.Style()
style.theme_use('classic')

# paned window
pw = ttk.PanedWindow(orient=HORIZONTAL)

# Left Label
label1 = Label(root, text="Left Label", font=("arial", 20, "bold"),bg="maroon", fg="white")
label1.pack(side=LEFT)
pw.add(label1)

# Right Label
label2 = Label(root, text="Right Label", font=("arial", 20, "bold"),bg="darkorange", fg="White")
label2.pack(side=RIGHT)
pw.add(label2)


# place the panedwindow on the root window
pw.pack(fill= BOTH, expand=True)


root.mainloop()