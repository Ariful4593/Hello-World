from tkinter import*
root=Tk()
frame = Frame(root, width=300, height=300)
label = Label(frame, text="Ariful Islam")
button = Button(frame, text="Click ME")

label.pack()
button.pack()
frame.pack()

bottom = Frame(root)
down = Button(bottom, text="Down Button")




down.pack()
bottom.pack(side=BOTTOM)
root.mainloop()