from tkinter import *

root = Tk()
root.title("Test App")
root.geometry("1600x800+0+0")
root.iconbitmap("Image/rocket.ico")

photo1 = PhotoImage(file = "gif/butterfly-1.gif")
C = Canvas(root, bg="yellow",height=800, width=1500)

line = C.create_line(50,320,300,50,fill="green", width=3)
rectangle = C.create_rectangle(100,250,400,400,fill="orange", outline="purple",width=4)
create_arc = C.create_arc(400, 450, 700, 200, start=0, extent=130, fill="red")
create_oval = C.create_oval(100, 700, 350, 450,fill="orange", outline="purple",width=4)
image = C.create_image((650,100), image=photo1)
polygon = C.create_polygon((700,200), (900,100), (1100,200), (1000,350), (800,400))
# line = C.create_window((650,100), image=photo1)
canvas = C.create_text((350, 150), text="Canvas Demo", fill="maroon", font='tkDefaeultFont 24 bold')




C.pack()
root.mainloop()