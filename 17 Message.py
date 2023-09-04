from tkinter import *

root = Tk()
root.title("Test App")
root.geometry("1000x600")
root.iconbitmap("Image/rocket.ico")


def func1():
    Message( root, text = "A computer science is horizon in science").pack()

button1 = Button(root, text="resizable True", font=("arial", 20, "bold"), command=func1).pack()

root.mainloop()