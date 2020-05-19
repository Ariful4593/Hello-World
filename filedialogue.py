from tkinter import *
from tkinter import filedialog
def open_file():
    result = filedialog.askopenfile(initialdir="/", title="Select file", filetypes=(("text files", ".txt"), ("all files", "*.*")))
    print(result)
    for i in result:
        print(i)

root = Tk()

btn = Button(root, text="Open FILE", command=open_file)
btn.pack()
root.geometry("300x300")
root.mainloop()