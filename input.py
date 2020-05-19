from tkinter import *
from tkinter import messagebox
def register():
    r = entry.get()
    if r=='Arif':
        success = messagebox.askyesno("quit","Do you want to quit?")
        print(success)
        if success=='yes':
            root.quit()
    else:
        unsuccess = messagebox.showerror("Sorry", "you enter in valid name")
        print(unsuccess)
root = Tk()

entry = Entry(root)
b = Button(root, text="Register", command=register)
entry.pack()
b.pack()
root.geometry("300x300+120+120")
root.mainloop()