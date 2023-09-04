from tkinter import *

root = Tk()
root.title('Work with image')
root.iconbitmap("image/rocket.ico")
root.geometry("500x300")

  
photo1 = PhotoImage(file = "png/018-return-to-the-past.png")

Button(root, text = 'Click Me !', image = photo1).pack(side = TOP)

Button(root, text = 'Click Me !', image = photo1, compound=LEFT).pack(side = TOP)



root.mainloop()