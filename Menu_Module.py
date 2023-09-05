from tkinter import *
from tkinter import ttk
import webbrowser

def Menubar_func(root):
# ================================================ MenuBar MenuBar MenuBar =============================================
# ================================================ MenuBar MenuBar MenuBar =============================================
# ================================================ MenuBar MenuBar MenuBar =============================================
# ================================================ MenuBar MenuBar MenuBar =============================================
# ================================================ MenuBar MenuBar MenuBar =============================================
        def viewhelp():
            
            webbrowser.open(
                "https://www.bing.com/search?q=get+help+with+notepad+in+windows&filters=guid:%224466414-en-dia%22%20lang:%22en%22&form=T00032&ocid=HelpPane-BingIA"
            )

        menubar = Menu(root)
        # ================= file file ============================
        file = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file)
        # __________________________________________
        file.add_command(label="New", accelerator="Ctrl+N")
        file.add_command(label="New Window", command=None, accelerator="Ctrl+Shift+N")

        sub_file_open = Menu(file, tearoff=0)
        sub_file_open.add_command(label="Open File", command="None")
        sub_file_open.add_command(label="Open Folder", command="None")
        file.add_cascade(label="Open ..", menu=sub_file_open)

        file.add_command(label="Save", command=None, accelerator="Ctrl+S")
        file.add_command(label="Save As ..", command=None, accelerator="Ctrl+Shift+S")
        file.add_separator()
        file.add_command(label="Page Setup .. ", command=None)
        file.add_command(label="Print .. ", command=None, accelerator="Ctrl+P")
        file.add_separator()
        file.add_command(label="Exit", command=exit, accelerator="Ctrl+W")

        # ==================== edit edit =============================================
        edit = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit)
        # __________________________________________________________________
        edit.add_command(label="Undo", command="None", accelerator="Ctrl+Z")
        edit.add_command(label="Redo", command="None", accelerator="Ctrl+Y")
        edit.add_separator()
        edit.add_command(label="Cut", command="None", accelerator="Ctrl+X")
        edit.add_command(label="Copy", command="None", accelerator="Ctrl+C")
        edit.add_command(label="Past", command="None", accelerator="Ctrl+V")
        edit.add_command(label="Delete", command="None", accelerator="Del")
        edit.add_separator()
        edit.add_command(label="Search With Bing .. ", command="None", accelerator="Ctrl+E")
        edit.add_command(label="Find .. ", command="None", accelerator="Ctrl+F")
        edit.add_command(label="Find Next", command="None", accelerator="F3")
        edit.add_command(label="Find Previous", command="None", accelerator="Shift+F3")
        edit.add_command(label="Go To .. ", command="None", accelerator="Ctrl+G")
        edit.add_separator()
        edit.add_command(label="Select All", command="None", accelerator="Ctrl+A")
        edit.add_command(label="Time Date", command="None", accelerator="F5")
        # ========================== format format ================================================
        formate = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Format", menu=formate)
        # __________________________________________________________
        formate.add_checkbutton(label="Word Wrap")
        formate.add_command(label="Font")
        # ============================= view view =============================================
        view = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view)
        # -----------------------------------------------
        #
        sub_view = Menu(view, tearoff=0)
        sub_view.add_command(label="Zoom In", command="None")
        sub_view.add_command(label="Zoom Out", command="None")

        view.add_cascade(label="Zoom", menu=sub_view)
        #
        view.add_checkbutton(label="Status Bar", command="None")
        # ==========================================================================
        help = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help)
        # _____________________________________________________------
        help.add_command(label="View Help", command=viewhelp)
        help.add_command(label="Send Feedback", command="None")
        help.add_separator()
        help.add_command(label="About Nodebook", command="None")

        root.config(menu=menubar)

        # =================================================================================================
        # tk_popup()    tk_popup()    tk_popup()    tk_popup()    tk_popup()    tk_popup()    tk_popup()
        # =================================================================================================

        m = Menu(root, tearoff = 0)
        m.add_command(label ="Cut")
        m.add_command(label ="Copy")
        m.add_command(label ="Paste")
        m.add_command(label ="Reload")
        m.add_separator()
        m.add_command(label ="Rename")

        def do_popup(event):
            try:
                m.tk_popup(event.x_root, event.y_root)
            finally:
                m.grab_release()

        root.bind("<Button-3>", do_popup)