from tkinter import *
from tkinter.ttk import Combobox

def clickme():
    value=combo.get()
    print(value)
root = Tk()
list_1 = list(range(1,32))
combo = Combobox(root, values=list_1)
combo.set("Select")
combo.pack()

button = Button(root, text="Click Me", command=clickme)
button.pack()

root.geometry("400x400+120+120")
root.mainloop()