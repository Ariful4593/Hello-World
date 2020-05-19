from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
list = ["Arif","Akram","Arman","Imran"]
combo = Combobox(root, values=list)
combo.pack()

root.geometry("400x400+120+120")
root.mainloop()