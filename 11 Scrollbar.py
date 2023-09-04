from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Test App")
root.geometry("1000x600")
root.iconbitmap("Image/rocket.ico")



scroll_x = ttk.Scrollbar(root, orient=HORIZONTAL)
scroll_y = ttk.Scrollbar(root, orient=VERTICAL)
hospital_table = ttk.Treeview(root, columns=("nameoftables","ref","dose","nooftables","lot","issuedate","expdate","dailydose","storage",
                                                            "nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x = ttk.Scrollbar(command=hospital_table.xview)
scroll_y = ttk.Scrollbar(command=hospital_table.yview)

root.mainloop()