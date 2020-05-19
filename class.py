from tkinter import *

class myButton:
    def __init__(self, master):
        self.printButton = Button(master, text="Print", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(master, text="Quit", command = master.quit)
        self.quitButton.pack(side=RIGHT)
    def printMessage(self):
        print("Hello World")

root = Tk()
b = myButton(root)
root.mainloop()