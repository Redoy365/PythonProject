from tkinter import *
from Menu_Module import *
from Button_Module import *

root = Tk()
root.title("My App")
root.geometry("1000x600")

icon_file1 = PhotoImage(file='png/002-add-folder.png')
icon_file2 = PhotoImage(file='png/018-return-to-the-past.png')
icon_file3 = PhotoImage(file='png/008-new-window.png')
icon_file4 = PhotoImage(file='png/Fullscreen -font.png')
icon_file5 = PhotoImage(file='png/013-cut.png')

Menu_link(root, icon_file1, icon_file2, icon_file3, icon_file4, icon_file5)

button1(root)

root.mainloop()