from tkinter import *

def button1(root):
    Button(root, text="Click me", font=("arial",20,"bold"), 
           bg="darkorange", fg="white", activebackground="violet", activeforeground="aqua").pack(anchor=E, expand=True)