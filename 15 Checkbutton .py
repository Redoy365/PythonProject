from tkinter import *

root = Tk()
root.title("Test App")
root.geometry("1000x600")
root.iconbitmap("Image/rocket.ico")

Check_button1 = Checkbutton(root, text="Checkbutton 1")
Check_button1.pack()

Check_button2 = Checkbutton(root, text="Checkbutton 2", activebackground="darkorange", activeforeground="white")
Check_button2.pack()

Check_button3 = Checkbutton(root, text="Checkbutton 3", bg="red", fg="maroon")
Check_button3.pack()

Check_button4 = Checkbutton(root, text="Checkbutton 4")
Check_button4.pack()


root.mainloop()