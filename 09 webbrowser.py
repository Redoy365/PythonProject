from tkinter import *
import webbrowser

root = Tk()
root.title("Test App")
root.geometry("1000x600")
root.iconbitmap("Image/rocket.ico")


webbrows = webbrowser.open(
    "https://www.w3schools.com/python/python_mysql_getstarted.asp"
)

root.destroy()

root.mainloop()