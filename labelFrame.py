from tkinter import *
root = Tk()
frame = LabelFrame(root,text="Input", padx=5, pady=5)

entry = Entry(frame)
entry.pack()

frame.pack()
root.geometry("300x300")
root.mainloop()