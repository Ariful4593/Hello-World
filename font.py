from tkinter import *
from tkinter.font import Font

root = Tk()
my_font = Font(size=20,family="SutonnyMJ",weight="bold",underline=1, slant="italic")
label = Label(root,text="This is our new page",font=my_font)
label.pack()

root.geometry("400x400+120+120")
root.mainloop() 