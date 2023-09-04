from tkinter import *

root = Tk()
root.title("Test App")
root.geometry("1700x900+0+0")
root.iconbitmap("Image/rocket.ico")

photo1 = PhotoImage(file = "png/018-return-to-the-past.png")    #===================

#=============================================================
#====================== Radiobutton ==========================
#=============================================================
"""
activebackground
activeforeground
anchor
bg
fg
bd
bitmap
borderwidth
command
cursor
font
height
highlightbackground
highlightcolor
image
justify
padx
pady
relief
selectcolor
selectimage
state
text
textvariable
underline
value
variable
width
wraplength

"""

# ============================================================
radio_button1 = Radiobutton(root, text="Mail 1")
radio_button1.pack()

radio_button2 = Radiobutton(root, text="Mail 2", font=("arial", 14, "bold"), width=50, state=ACTIVE)
radio_button2.pack()

radio_button3 = Radiobutton(root, text="Mail 3",font=("arial", 14, "bold"), selectcolor="red", relief=RAISED)
radio_button3.pack()

radio_button4 = Radiobutton(root, text="Mail 4", font=("arial", 14, "bold"), padx=10, pady=8, bg="white", fg="green", bd=10)
radio_button4.pack()

radio_button5 = Radiobutton(root, text="Mail 5", font=("arial", 14, "bold"), padx=10, pady=8, bg="white", fg="green", bd=10)
radio_button5.config(image=photo1)
radio_button5.pack()

radio_button6 = Radiobutton(root, text="Mail 6", font=("arial", 14, "bold"),  padx=10, pady=8, bg="white", fg="green", bd=10, compound=RIGHT)
radio_button6.config(image=photo1)
radio_button6.pack()

radio_button7 = Radiobutton(root, text="Mail 7", font=("arial", 14, "bold"), padx=10, pady=8, bg="white", fg="green", bd=10, state=DISABLED)
radio_button7.pack()

radio_button8 = Radiobutton(root, text="Mail 8", font=("arial", 14, "bold"), padx=10, pady=8, bg="white", fg="green", bd=10, wraplength=5)
radio_button8.pack()

radio_button9 = Radiobutton(root, text="Mail 9", font=("arial", 14, "bold"), padx=10, pady=8, bg="white", fg="green", bd=10, width=50, justify="right")
radio_button9.pack()

radio_button10 = Radiobutton(root, text="Mail 10", font=("arial", 14, "bold"), padx=10, pady=8, bg="white", fg="green", bd=10,
                             activebackground="orange", activeforeground="maroon")
radio_button10.pack()

radio_button11 = Radiobutton(root, text="Mail 11", font=("arial", 14, "bold"), padx=10, pady=8, bg="white", fg="green", bd=10, width=40, height=3, anchor=NW)
radio_button11.pack()

radio_button12 = Radiobutton(root, text="Mail 12", font=("arial", 14, "bold"), padx=10, pady=8, bg="white", fg="green", bd=10, bitmap="hourglass")
radio_button12.pack()

radio_button13 = Radiobutton(root, text="Mail 13", font=("arial", 14, "bold"), padx=10, pady=8, bg="white", fg="green", bd=10, borderwidth=10)
radio_button13.pack()

radio_button14 = Radiobutton(root, text="Mail 14", font=("arial", 14, "bold"), padx=10, pady=8, bg="white", fg="green", bd=10, cursor="heart")
radio_button14.pack()

root.mainloop()