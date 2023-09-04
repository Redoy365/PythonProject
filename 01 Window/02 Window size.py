from tkinter import *

root = Tk()
root.title("Test App")
root.geometry("1000x600")
root.iconbitmap("Image/rocket.ico")


root.minsize(300,200)
root.maxsize(800, 400)


def func1():
    root.resizable(True, True)

def func2():
    root.resizable(False, False)

button1 = Button(root, text="resizable True", font=("arial", 20, "bold"), command=func1).pack()
button2 = Button(root, text="resizable False", font=("arial", 20, "bold"), command=func2).pack()

root.mainloop()