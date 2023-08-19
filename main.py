from tkinter import *
from PIL import ImageTk, Image
import speedtest
# &&&&|||| Logic ||||&&&&&
def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+" Mbps"
    uplod = str(round(sp.upload()/(10**6),3))+" Mbps"
    lab3_down.config(text=down)
    lab5_Up.config(text=uplod)
# &&&&|||| Logic ||||&&&&&



# ======================
root = Tk()
root.title("Internet Speed Test")
p1 = PhotoImage(file='speed.png')
root.iconphoto(False, p1)
root.geometry("1000x600")
# ===============Background Design===============================
img =Image.open('img1.jpg')
bg = ImageTk.PhotoImage(img)
label = Label(root, image=bg)
label.place(x = 0,y = 0)
# ========================@@@@@@@@ Label set @@@@@@@@@@=======================================
lab1 = Label(root, text= "Internet Speed Test", font=("Time New Roman", 20, "bold"), bg="White", padx=10, pady=10)
lab1.place(x=300,y=120,height=50,width=380)
#1
lab2 = Label(root, text= "Download Speed", font=("Time New Roman", 20, "bold"))
lab2.place(x=300,y=180,height=50,width=380)
#2
lab3_down = Label(root, text= "00", font=("Time New Roman", 20, "bold"))
lab3_down.place(x=300,y=240,height=50,width=380)
#3
lab4 = Label(root, text= "Upload Speed", font=("Time New Roman", 20, "bold"))
lab4.place(x=300,y=300,height=50,width=380)
#4
lab5_Up = Label(root, text= "00", font=("Time New Roman", 20, "bold"))
lab5_Up.place(x=300,y=360,height=50,width=380)
#5
btn1 = Button(root, text= "Check Speed", font=("Time New Roman", 20, "bold"),relief=RAISED,bg="red",fg="wheat",command=speedcheck)
btn1.place(x=300,y=420,height=50,width=380)

# ============== Set window in center screen with following way. ==============
positionRight = int(root.winfo_screenwidth() / 2 - 1000 / 2)
positionDown = int(root.winfo_screenheight() / 2 - 600 / 2)
root.geometry("{}x{}+{}+{}".format(1000, 600, positionRight, positionDown))
# =====================

root.mainloop()