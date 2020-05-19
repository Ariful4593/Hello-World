from tkinter import *
from tkinter import messagebox
def callme():
    messagebox.showinfo("Success", "Installation Complete")
def tellme():
    answer = messagebox.askquestion("exit", "Do you want to exit really?")
    print(answer)
    if answer=='yes':
        root.quit()
    else:
        print("Stay on Page")
root = Tk()

b = Button(root, text="message", command=callme)
b.pack()
p = Button(root, text="AskQuestion", command=tellme)


p.pack()
root.geometry("400x400+120+120")
root.mainloop()