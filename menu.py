from tkinter import *

def new_project():
    a = int(input("please enter first number: "))
    b = int(input("please enter second number: "))
    c = a + b
    print("Your result is: ",c)
def new():
    print("Okay! New file create now")

def new_scratch():
    print("Thank you for create new scratch")
def new_file():
    print("Thank you for create new file..")

root = Tk()
main_menu = Menu(root)
root.config(menu=main_menu)

#file menu
fileMenu = Menu(main_menu)
main_menu.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="New Project", command=new_project)
fileMenu.add_command(label="New", command=new)
fileMenu.add_separator()
fileMenu.add_command(label="New Scratch", command=new_scratch)
fileMenu.add_command(label="New file", command=new_file)

#edit menu
editMenu = Menu(main_menu)
main_menu.add_cascade(label="Edit", menu=editMenu)

#View Menu
viewMenu = Menu(main_menu)
main_menu.add_cascade(label="View", menu=viewMenu)

#Navigate Menu
navigate_Menu = Menu(main_menu)
main_menu.add_cascade(label="Navigate", menu=navigate_Menu)




save_menu = Menu(fileMenu)
save_menu.add_cascade(label="save as new", command=new)
save_menu.add_cascade(label="save now", command=new)

fileMenu.add_cascade(label="Save", menu=save_menu)

root.mainloop()