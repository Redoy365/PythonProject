from tkinter import *

def Menu_link(root, *image):
# =====================================================================
# ======      function      function       function     ===============
# =====================================================================
        def exit_command():
                root.destroy()
# =====================================================================
# ======      function      function       function     ===============
# =====================================================================
        menubar = Menu(root)
        # menubar
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
        # ========================================================
        fill.add_command(label="  New Text File",image=image[0], command=None, compound=LEFT,  accelerator="Ctrl+N")
        fill.add_command(label="  New File", image=image[1],compound=LEFT, command=None, accelerator="Ctrl+Alt+Window+N")
        fill.add_command(label="  New Window", image=image[2], compound=LEFT, command=None, accelerator="Ctrl+Shift+N")
        fill.add_separator()
        fill.add_command(label="  Open File", command=None, accelerator="Ctrl+O")
        fill.add_command(label="  Open Folder", command=None, accelerator="Ctrl+K+O")
        fill.add_separator()
        fill.add_command(label="  Save", command=None, accelerator="Ctrl+S")
        fill.add_command(label="  Save AS ...", command=None, accelerator="Ctrl+Shift+S")
        fill.add_command(label="  Save All", command=None, accelerator="Ctrl+KS")
        fill.add_separator()
        fill.add_command(label="  Close File", command=None, accelerator="Ctrl+O")
        fill.add_command(label="  Close Folder", command=None, accelerator="Ctrl+O")
        fill.add_command(label="  Open Window", command=None, accelerator="Ctrl+O")
        fill.add_separator()
        fill.add_command(label="  Full Screen", image= image[3], compound=LEFT, accelerator="Ctrl+O")
        fill.add_command(label="  Exit", image=image[4], compound=LEFT, command=exit_command, accelerator="Ctrl+W")

        root.config(menu=menubar)

        