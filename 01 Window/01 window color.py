from tkinter import *

root = Tk()
root.title("Test App")
root.geometry("1000x600")
root.iconbitmap("Image/rocket.ico")

icon = PhotoImage(file = "png/018-return-to-the-past.png")

root.iconphoto(True, icon)
root.config(background="darkorange")


root.mainloop()