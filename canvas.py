from tkinter import *
root = Tk()
canvas = Canvas(root, width=200, height=200, bg="green")
canvas.pack()
line = canvas.create_line(100,150,100,100)

root.geometry("400x400+120+120")
root.mainloop()