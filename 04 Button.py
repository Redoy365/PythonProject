from tkinter import *

root = Tk()
root.title("Test App")
root.geometry("1000x600")
root.iconbitmap("Image/rocket.ico")

button1 = Button(root, text="Click Now 1", font=("arial",20,"bold"))
button1.pack()

button2 = Button(root, text="Click Now 2", font=("arial",20,"bold"), fg="green", bg="white", command=None)
button2.pack()

button3 = Button(root, text="Click Now 3", font=("arial",20,"bold"), fg="green", bg="white",activebackground="darkorange",activeforeground="white", command=None)
button3.pack()

button4 = Button(root, text="Click Now 4", font=("arial",20,"bold"), bd=0, fg="green", bg="white",activebackground="darkorange",
          activeforeground="white", command=None, anchor=NE)
button4.pack()
# ==========================================================================
button5 = Button(root, text="Click Now 5", font=("arial",20,"bold"), bd=15, fg="green", bg="white", anchor=NE)
button5.config(width=20, height=2)
button5.pack()
# ==========================================================================
button6 = Button(root, text="Click Now 6", font=("arial",20,"bold"), highlightcolor="red", padx=20, pady=10)
button6.pack()

button7 = Button(root, text="Click Now 7", font=("arial",20,"bold"), highlightcolor="red", justify=LEFT)
button7.config(width=20, height=2)
button7.pack()




root.mainloop()