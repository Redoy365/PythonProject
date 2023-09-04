from tkinter import *

root = Tk()
root.title("Test App")
root.geometry("1000x600")
root.iconbitmap("Image/rocket.ico")

label1 = Label(root, text="I am a software Engineer.", font=("arial", 20, "bold"))
label1.pack()

label2 = Label(root, text="I am a software Engineer.", font=("arial", 20, "bold"), fg="green", bg="white")
label2.config(width=20,height=2)
label2.pack()

label2 = Label(root, text="I am a software Engineer.", font=("arial", 20, "bold"), fg="green", bg="white")
label2.pack()


root.mainloop()