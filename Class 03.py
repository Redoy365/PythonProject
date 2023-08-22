from tkinter import *

root = Tk()
root.title("Test App")
root.geometry("1000x600")

def fun():
    for i in range():
        button = Button(root, text="Click me", fg="red", bg="wheat", font=("Fixedsys", 20, "bold"),
                        padx=10, pady=10, border=0).grid(row=i, column=i, )

button = Button(root, text="Click me",fg="red", bg="wheat", font=("Fixedsys",20,"bold"),
                padx=10, pady=10, border=0, command=fun).grid(row=0, column=0,)


root.mainloop()