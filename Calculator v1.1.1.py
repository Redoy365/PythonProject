import tkinter as tk
import math
from tkinter import *

# ===========================
window = Tk()
window.title("Claculator")
window.geometry("450x600")
window.minsize(450,600)
window.maxsize(450,600)
# ============================
# entry = Entry(window, width=430, bg="white", fg="darkorange", font=("Fixedsys",16,"regular"))
entry = Entry(window, width=100,  borderwidth=5, font=("LibreBaskerville-Regular", 20,"bold"), fg="#4F34E3")
entry.place(x=10,y=10,width=430)
global x

def result():
   try:
       x_ = eval(entry.get())
       entry.delete(0,END)

       if x_ == True:
           entry.insert(0, "True")
           return 0
       elif x_ == False:
           entry.insert(0, "False")
           return 0

       entry.insert(0,x_)


   except:
       entry.insert(0,"Syntext Error")

def button_clear():
    entry.delete(0,END)

def button_1():
    entry.insert(tk.END,"1")

def button_2():
    entry.insert(tk.END,"2")

def button_3():
    entry.insert(tk.END,"3")

def button_4():
    entry.insert(tk.END,"4")

def button_5():
    entry.insert(tk.END,"5")

def button_6():
    entry.insert(tk.END,"6")

def button_7():
    entry.insert(tk.END,"7")

def button_8():
    entry.insert(tk.END,"8")

def button_9():
    entry.insert(tk.END,"9")

def button_0():
    entry.insert(tk.END,"0")

def button_ADD():
    entry.insert(tk.END,"+")


def button_SUB():
    entry.insert(tk.END, "-")


def button_MUL():
    entry.insert(tk.END, "*")


def button_DIV():
    entry.insert(tk.END, "/")


def button_Modu():
    n = eval(entry.get())
    entry.delete(0,END)
    entry.insert(tk.END, abs(n))


def button_Grater():
    entry.insert(tk.END, ">")


def button_Less():
    entry.insert(tk.END, "<")


def button_Not_Equal():
    entry.insert(tk.END, "!=")


def button_Remaining():
    entry.insert(tk.END, "")

def button_Floer_Div():
    entry.insert(tk.END, "")

def button_Left_Bra():
    entry.insert(tk.END, "")

def button_Right_Bra():
    entry.insert(tk.END, "")

def button_Equal_To():
    entry.insert(tk.END, "==")

def button_x2y():
    entry.insert(tk.END, "")

def button_x2x():
    entry.insert(tk.END, "")

def button_10to2():
    entry.insert(tk.END, "")

def button_dot():
    entry.insert(tk.END, ".")

 # elif x_ == "Log":
 #           entry.insert(0, math.log(x_))
 #
 #       elif x_ == "In":
 #         entry.insert(0, math.log2(x_))
 #

def button_log():
    y = eval(entry.get())
    entry.insert(0, math.log(y))

def button_In():
    y = eval(entry.get())
    entry.insert(0, math.log2(y))



# ========== Label Create ==========
lab1 = Label(window, text="This is Super First Calculator.", font=("Fixedsys", 16,"bold"), fg="#395173")
lab1.place(x=10,y=60,width=430)

# ===============1 2 3 4================
btn1 = Button(window, text=1, font=("LibreBaskerville-Regular", 20, "bold"), bg="darkorange", fg="white", command=button_1)
btn1.place(x=10, y=100, width=60, height=40)

btn2 = Button(window, text=2, font=("LibreBaskerville-Regular", 20,"bold"), bg="darkorange", fg="white", command=button_2)
btn2.place(x=80, y=100, width=60, height=40)

btn3 = Button(window, text=3, font=("LibreBaskerville-Regular", 20,"bold"), bg="darkorange", fg="white", command=button_3)
btn3.place(x=150, y=100, width=60, height=40)

btn4 = Button(window, text=4, font=("LibreBaskerville-Regular", 20,"bold"), bg="darkorange", fg="white", command=button_4)
btn4.place(x=220, y=100, width=60, height=40)
# =============== ______________ ===============
btn4_ = Button(window, text="(", font=("LibreBaskerville-Regular", 20,"bold"), bg="#514280", fg="white", command=button_Left_Bra)
btn4_.place(x=290, y=100, width=65, height=40)

btn5_ = Button(window, text=")", font=("LibreBaskerville-Regular", 20,"bold"), bg="#514280", fg="white", command=button_Right_Bra)
btn5_.place(x=370, y=100, width=65, height=40)

btn6_ = Button(window, text="In", font=("LibreBaskerville-Regular", 20,"bold"), bg="#514280", fg="white", command=button_In)
btn6_.place(x=290, y=150, width=65, height=40)

btn7_ = Button(window, text="Log", font=("LibreBaskerville-Regular", 20,"bold"), bg="#514280", fg="white", command=button_log)
btn7_.place(x=370, y=150, width=65, height=40)

btn8_ = Button(window, text="10^2", font=("LibreBaskerville-Regular", 20,"bold"), bg="#514280", fg="white", command=button_10to2)
btn8_.place(x=290, y=200, width=65, height=40)

btn9_ = Button(window, text="x^y", font=("LibreBaskerville-Regular", 20,"bold"), bg="#514280", fg="white", command=button_x2y)
btn9_.place(x=370, y=200, width=65, height=40)

btn10_ = Button(window, text="x^x", font=("LibreBaskerville-Regular", 20,"bold"), bg="#514280", fg="white", command=button_x2x)
btn10_.place(x=290, y=250, width=65, height=40)

btn11_ = Button(window, text="|x|", font=("LibreBaskerville-Regular", 20,"bold"), bg="#514280", fg="white", command=button_Modu)
btn11_.place(x=370, y=250, width=65, height=40)

btn12_ = Button(window, text="%", font=("LibreBaskerville-Regular", 20,"bold"), bg="#514280", fg="white", command=button_Remaining)
btn12_.place(x=290, y=300, width=65, height=40)

btn12_ = Button(window, text="//", font=("LibreBaskerville-Regular", 20,"bold"), bg="#514280", fg="white", command=button_Floer_Div)
btn12_.place(x=370, y=300, width=65, height=40)

btn13_ = Button(window, text=">", font=("LibreBaskerville-Regular", 20,"bold"), bg="#514280", fg="white", command=button_Grater)
btn13_.place(x=10, y=300, width=60, height=40)

btn14_ = Button(window, text="<", font=("LibreBaskerville-Regular", 20,"bold"), bg="#514280", fg="white", command=button_Less)
btn14_.place(x=80, y=300, width=60, height=40)

btn15_ = Button(window, text="!=", font=("LibreBaskerville-Regular", 20,"bold"), bg="#514280", fg="white", command=button_Not_Equal)
btn15_.place(x=150, y=300, width=60, height=40)

btn16_ = Button(window, text="==", font=("LibreBaskerville-Regular", 20,"bold"), bg="#514280", fg="white", command=button_Equal_To)
btn16_.place(x=220, y=300, width=60, height=40)
# ============== _________________================

#
#============ 5 6 7 8 ======================
btn5 = Button(window, text=5, font=("LibreBaskerville-Regular", 20,"bold"), bg="darkorange", fg="white", command=button_5)
btn5.place(x=10, y=150, width=60, height=40)

btn6 = Button(window, text=6, font=("LibreBaskerville-Regular", 20,"bold"), bg="darkorange", fg="white", command=button_6)
btn6.place(x=80, y=150, width=60, height=40)

btn7 = Button(window, text=7, font=("LibreBaskerville-Regular", 20,"bold"), bg="darkorange", fg="white", command=button_7)
btn7.place(x=150, y=150, width=60, height=40)

btn8 = Button(window, text=8, font=("LibreBaskerville-Regular", 20,"bold"), bg="darkorange", fg="white", command=button_8)
btn8.place(x=220, y=150, width=60, height=40)
#
#=================== 9 10 AC <=
btn9 = Button(window, text=9, font=("LibreBaskerville-Regular", 20,"bold"), bg="darkorange", fg="white", command=button_9)
btn9.place(x=10, y=200, width=60, height=40)

btn10 = Button(window, text=0, font=("LibreBaskerville-Regular", 20,"bold"), bg="darkorange", fg="white", command=button_0)
btn10.place(x=80, y=200, width=60, height=40)

btn11 = Button(window, text="AC", font=("LibreBaskerville-Regular", 20,"bold"), bg="darkorange", fg="white", command=button_clear)
btn11.place(x=150, y=200, width=60, height=40)

btn12 = Button(window, text=".", font=("LibreBaskerville-Regular", 20,"bold"), bg="darkorange", fg="white", command=button_dot)
btn12.place(x=220, y=200, width=60, height=40)
#
# =============== + - X / ==============
#
#
btn13 = Button(window, text="+", font=("LibreBaskerville-Regular", 20,"bold"), bg="darkorange", fg="white", command=button_ADD)
btn13.place(x=10, y=250, width=60, height=40)

btn14 = Button(window, text="-", font=("LibreBaskerville-Regular", 20,"bold"), bg="darkorange", fg="white", command=button_SUB)
btn14.place(x=80, y=250, width=60, height=40)

btn15 = Button(window, text="x", font=("LibreBaskerville-Regular", 20,"bold"), bg="darkorange", fg="white", command=button_MUL)
btn15.place(x=150, y=250, width=60, height=40)

btn16 = Button(window, text="/", font=("LibreBaskerville-Regular", 20,"bold"), bg="darkorange", fg="white", command=button_DIV)
btn16.place(x=220, y=250, width=60, height=40)

# ============================================
btn21_ = Button(window, text="Sin", font=("LibreBaskerville-Regular", 20,"bold"), bg="#2EC866", fg="white")
btn21_.place(x=10, y=400, width=70, height=45)

btn22_ = Button(window, text="Cos", font=("LibreBaskerville-Regular", 20,"bold"), bg="#2EC866", fg="white")
btn22_.place(x=95, y=400, width=70, height=45)

btn23_ = Button(window, text="tan_", font=("LibreBaskerville-Regular", 20,"bold"), bg="#2EC866", fg="white")
btn23_.place(x=180, y=400, width=70, height=45)

btn24_ = Button(window, text="n!", font=("LibreBaskerville-Regular", 20,"bold"), bg="#2EC866", fg="white")
btn24_.place(x=270, y=400, width=70, height=45)

btn25_ = Button(window, text="e", font=("LibreBaskerville-Regular", 20,"bold"), bg="#2EC866", fg="white")
btn25_.place(x=360, y=400, width=70, height=45)

btn26_ = Button(window, text="1/Sin", font=("LibreBaskerville-Regular", 20,"bold"), bg="#2EC866", fg="white")
btn26_.place(x=10, y=450, width=70, height=45)

btn27_ = Button(window, text="1/Cos", font=("LibreBaskerville-Regular", 20,"bold"), bg="#2EC866", fg="white")
btn27_.place(x=95, y=450, width=70, height=45)

btn28_ = Button(window, text="1/tan", font=("LibreBaskerville-Regular", 20,"bold"), bg="#2EC866", fg="white")
btn28_.place(x=180, y=450, width=70, height=45)

btn29_ = Button(window, text="t", font=("LibreBaskerville-Regular", 20,"bold"), bg="#2EC866", fg="white")
btn29_.place(x=270, y=450, width=70, height=45)

btn30_ = Button(window, text="S", font=("LibreBaskerville-Regular", 20,"bold"), bg="#2EC866", fg="white")
btn30_.place(x=360, y=450, width=70, height=45)


# ============================== R E S U L T ==============
btn16 = Button(window, text="R E S U L T", font=("LibreBaskerville-Regular", 20,"bold"), bg="darkorange", fg="white", command=result)
btn16.place(x=10, y=350, width=430, height=40)
# ============================================
# ============================================


window.mainloop()