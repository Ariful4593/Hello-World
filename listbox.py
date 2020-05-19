from tkinter import *

def listcall():
    clicked_items = l.curselection()
    print(clicked_items)
    for item in clicked_items:
        print(item)

def delete_me():
    delete_items = l.curselection()
    for delete_data in delete_items:
        print(l.delete(delete_data))
root = Tk()
l = Listbox(root,width=30, height=15, selectmode=MULTIPLE)#selectmode = BROWSE,SINGLE,MULTIPLE,EXTENDED
l.insert(1, "Python")
l.insert(2, "C")
l.insert(3, "C++")
l.insert(4, "C#")
l.insert(5, "Nodejs")

button = Button(root, text="Click ME", command=listcall)
button1 = Button(root, text="Delete", command=delete_me)
l.pack()
button.pack()
button1.pack()
root.geometry("400x400+120+120")
root.mainloop()