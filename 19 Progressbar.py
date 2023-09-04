from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Test App")
root.geometry("1000x600")
root.iconbitmap("Image/rocket.ico")

progress = ttk.Progressbar(root, orient = HORIZONTAL, length = 300, mode = 'indeterminate')
  
# Function responsible for the updation
# of the progress bar value
def bar():
    for i in range(0,300):

        import time
        progress['value'] = i
        root.update_idletasks()
        time.sleep(0.01)
        i=i+5
    
    for i in range(300, 0, -1):

        import time
        progress['value'] = i
        root.update_idletasks()
        time.sleep(0.01)
        i=i-5
      
  
progress.pack(pady = 10)
  
# This button will initialize
# the progress bar
Button(root, text = 'Start', command = bar).pack(pady = 10)

root.mainloop()