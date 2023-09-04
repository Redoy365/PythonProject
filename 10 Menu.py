from tkinter import *

root = Tk()
root.title("Test App")
root.geometry("1000x600")
root.iconbitmap("Image/rocket.ico")


# ======================================================
# ======================================================
# ======================================================
# =========   Function    Function    Function    ======
# ======================================================
# ======================================================
# ======================================================
def full_screen():
    root.attributes('-fullscreen', True)
# ======================================================
# ======================================================
# ======================================================
# =========   Function    Function    Function    ======
# ======================================================
# ======================================================
# ======================================================
menubar = Menu(root)
# =====================================================
fill = Menu(menubar, tearoff=0)
edit = Menu(menubar, tearoff=0)
section = Menu(menubar, tearoff=0)
view = Menu(menubar, tearoff=0)
go = Menu(menubar, tearoff=0)
run = Menu(menubar, tearoff=0)
terminal = Menu(menubar, tearoff=0)
help = Menu(menubar, tearoff=0)
# ======================================================
menubar.add_cascade(label="File", menu=fill)
menubar.add_cascade(label="Edit", menu=edit)
menubar.add_cascade(label="Section", menu=section)
menubar.add_cascade(label="View", menu=view)
menubar.add_cascade(label="Go", menu=go)
menubar.add_cascade(label="Run", menu=run)
menubar.add_cascade(label="Terminal", menu=terminal)
menubar.add_cascade(label="Help", menu=help)
# =======================================================
icon_file1 = PhotoImage(file='png/002-add-folder.png')
icon_file2 = PhotoImage(file='png/018-return-to-the-past.png')
icon_file3 = PhotoImage(file='png/008-new-window.png')
icon_file4 = PhotoImage(file='png/Fullscreen -font.png')
icon_file5 = PhotoImage(file='png/008-new-window.png')
# icon_file1 = PhotoImage(file='menu_icon/new.png')
# icon_file1 = PhotoImage(file='menu_icon/new.png')
# icon_file1 = PhotoImage(file='menu_icon/new.png')
# icon_file1 = PhotoImage(file='menu_icon/new.png')
# icon_file1 = PhotoImage(file='menu_icon/new.png')
# icon_file1 = PhotoImage(file='menu_icon/new.png')
# icon_file1 = PhotoImage(file='menu_icon/new.png')
# ========================================================
fill.add_command(label="  New Text File",image=icon_file1, command=None, compound=LEFT,  accelerator="Ctrl+N")
fill.add_command(label="  New File", image=icon_file2,compound=LEFT, command=None, accelerator="Ctrl+Alt+Window+N")
fill.add_command(label="  New Window",  image=icon_file3, compound=LEFT, command=None, accelerator="Ctrl+Shift+N")
fill.add_separator()
fill.add_command(label="Open File", command=None, accelerator="Ctrl+O")
fill.add_command(label="Open Folder", command=None, accelerator="Ctrl+K+O")
fill.add_separator()
fill.add_command(label="Save", command=None, accelerator="Ctrl+S")
fill.add_command(label="Save AS ...", command=None, accelerator="Ctrl+Shift+S")
fill.add_command(label="Save All", command=None, accelerator="Ctrl+KS")
fill.add_separator()
fill.add_command(label="Close File", command=None, accelerator="Ctrl+O")
fill.add_command(label="Close Folder", command=None, accelerator="Ctrl+O")
fill.add_command(label="Open Window", command=None, accelerator="Ctrl+O")
fill.add_separator()
fill.add_command(label="Full Screen", image= icon_file4, compound=LEFT, command=full_screen, accelerator="Ctrl+O")
fill.add_command(label="Exit", command=None, accelerator="Ctrl+O")



root.config(menu=menubar)

root.mainloop()