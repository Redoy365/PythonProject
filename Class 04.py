from tkinter import *

root = Tk()
root.title("Redoy")
root.geometry("1000x600")
# ========== Entry Design ===========
myenter = Entry(root, width=100, borderwidth=5, font=("Fixedsys", 20,"bold"))
myenter.pack()
myenter.focus_set()
myenter.insert(0,"Enter your name : ")


def Myfun():
    getentry = myenter.get()
    lab1 = Label(root, text=getentry, font=("Fixedsys", 20,"bold"))
    lab1.pack()

mybtn = Button(root, text="Click Me",font=("Fixedsys",20,"bold"), padx=10, pady=10, command=Myfun)

mybtn.pack()



root.mainloop()





i = 4
d = 4.0
s = 'HackerRank '

x = int(input())
y = float(input())
z = input()

print(i+x)
print(d+y)
print(s+z)



