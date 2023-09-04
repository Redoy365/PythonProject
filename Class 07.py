from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Work with image')
root.iconbitmap("image/rocket.ico")
root.geometry("500x300")


myimage = ImageTk.PhotoImage(Image.open('image/hello.png'))

label = Label(root, image=myimage)
label.pack()

root.mainloop()