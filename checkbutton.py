from tkinter import *
from tkinter import messagebox
def checker():
    if (i.get()==1):
        c = messagebox.showinfo("Congrate", "Come in boss")
        print(c)
    else:
        f = messagebox.showerror("You are Fail", "Please try again")

root = Tk()
i = IntVar()
c = Checkbutton(root,text="Keep me Login", variable=i)
b = Button(text="Register", command=checker)
c.pack()
b.pack()
root.geometry("300x300+120+120")
root.mainloop()