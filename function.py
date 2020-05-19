from tkinter import *
root = Tk()
def call_me():
    a = int(input("Enter a number: "))
    b = int(input("Enter second number: "))
    c = a + b
    print("Hey I am There..",c)
button = Button(root,text="Click me", command=call_me)

button.pack()
root.mainloop()