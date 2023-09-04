from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Work with image')
root.iconbitmap("image/rocket.ico")
root.geometry("500x300")


frame_plat = Frame(root,  bd=20, relief=RIDGE, height=400)
frame_plat.place(relx=0, rely=0, relwidth=1,relheight=0.4)

frame_item_left = LabelFrame(frame_plat, text="Pesent info", bd=10, relief=RIDGE,padx=0, pady=2, font=("arial",12,"bold"),)
frame_item_left.place(relx=0, rely=0, relheight=1, relwidth=0.6)

frame_item_right = LabelFrame(frame_plat, text="Pesent info", bd=10, relief=RIDGE,padx=0, pady=2, font=("arial",12,"bold"),)
frame_item_right.place(relx=0.6, rely=0, relheight=1, relwidth=0.4)





root.mainloop()