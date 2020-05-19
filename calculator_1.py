from tkinter import *
from tkinter import messagebox
val = ""
A = 0
operator = ""



def btn_1_selected():
    global val
    val = val + "1"
    data.set(val)
def btn_2_selected():
    global  val
    val = val + "2"
    data.set(val)
def btn_3_selected():
    global  val
    val = val + "3"
    data.set(val)
def btn_4_selected():
    global  val
    val = val + "4"
    data.set(val)
def btn_5_selected():
    global  val
    val = val + "5"
    data.set(val)
def btn_6_selected():
    global  val
    val = val + "6"
    data.set(val)
def btn_7_selected():
    global  val
    val = val + "7"
    data.set(val)
def btn_8_selected():
    global  val
    val = val + "8"
    data.set(val)
def btn_9_selected():
    global  val
    val = val + "9"
    data.set(val)
def btn_0_selected():
    global  val
    val = val + "0"
    data.set(val)
def btn_dot():
    global val
    val = val + "."
    data.set(val)
def btn_plus():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_min():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_mul():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_div():
    global A
    global operator
    global val
    A = int(val)
    operator="/"
    val = val + "/"
    data.set(val)

def c_pressed():
    global A
    global operator
    global val
    val = ""
    A = 0
    operator = ""
    data.set(val)

def result():
    global A
    global operator
    global val
    val2 = val #I have onconfused in this line
    if operator == "+":
        x = int((val2.split("+")[1]))
        c = A + x
        data.set(c)
        val = str(c)
    elif operator == "-":
        x = int((val2.split("-")[1]))
        c = A - x
        data.set(c)
        val = str(c)
    elif operator == "*":
        x = int((val2.split("*")[1]))
        c = A * x
        data.set(c)
        val = str(c)
    elif operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "Division is not Allowed")
            A =""
            val = ""
            data.set(val)
        else:
            c = getdouble(A / x)
            data.set(c)
            val = str(c)


root = Tk()
root.geometry("250x400+300+300")
root.title("Calculator")
root.resizable(False, False)

data = StringVar()

lbl = Label(root, text="Label", anchor=SE,textvariable=data, background="#ffffff")
lbl.pack(expand=True, fill="both")

btnrow1 = Frame(root, bg="black")
btnrow1.pack(expand=True, fill="both")

btnrow2 = Frame(root)
btnrow2.pack(expand=True, fill="both")

btnrow3 = Frame(root)
btnrow3.pack(expand=True, fill="both")

btnrow4 = Frame(root)
btnrow4.pack(expand=True, fill="both")

#row-1
btn1 = Button(
    btnrow1,
    text="1",
    relief=GROOVE,
    border=0,
    command=btn_1_selected
)
btn1.pack(side=LEFT,expand=True,fill="both")

btn2 = Button(
    btnrow1,
    text="2",
    relief=GROOVE,
    border=0,
    command=btn_2_selected
)
btn2.pack(side=LEFT,expand=True,fill="both")

btn3 = Button(
    btnrow1,
    text="3",
    relief=GROOVE,
    border=0,
    command=btn_3_selected
)
btn3.pack(side=LEFT,expand=True,fill="both")

btnplus = Button(
    btnrow1,
    text="+",
    relief=GROOVE,
    border=0,
    command=btn_plus
)
btnplus.pack(side=LEFT,expand=True,fill="both")



#row-2
btn4 = Button(
    btnrow2,
    text="4",
    relief=GROOVE,
    border=0,
    command=btn_4_selected
)
btn4.pack(side=LEFT,expand=True,fill="both")

btn5 = Button(
    btnrow2,
    text="5",
    relief=GROOVE,
    border=0,
    command=btn_5_selected
)
btn5.pack(side=LEFT,expand=True,fill="both")

btn6 = Button(
    btnrow2,
    text="6",
    relief=GROOVE,
    border=0,
    command=btn_6_selected
)
btn6.pack(side=LEFT,expand=True,fill="both")

btnminus = Button(
    btnrow2,
    text="-",
    relief=GROOVE,
    border=0,
    command=btn_min
)
btnminus.pack(side=LEFT,expand=True,fill="both")

#row-3
btn7 = Button(
    btnrow3,
    text="7",
    relief=GROOVE,
    border=0,
    command=btn_7_selected
)
btn7.pack(side=LEFT,expand=True,fill="both")

btn8 = Button(
    btnrow3,
    text="8",
    relief=GROOVE,
    border=0,
    command=btn_8_selected
)
btn8.pack(side=LEFT,expand=True,fill="both")

btn9 = Button(
    btnrow3,
    text="9",
    relief=GROOVE,
    border=0,
    command=btn_9_selected
)
btn9.pack(side=LEFT,expand=True,fill="both")

btnmul = Button(
    btnrow3,
    text="*",
    relief=GROOVE,
    border=0,
    command=btn_mul
)
btnmul.pack(side=LEFT,expand=True,fill="both")

#row-4
btnclear = Button(
    btnrow4,
    text="C",
    relief=GROOVE,
    border=0,
    command=c_pressed
)
btnclear.pack(side=LEFT,expand=True,fill="both")

btnzero = Button(
    btnrow4,
    text="0",
    relief=GROOVE,
    border=0,
    command=btn_0_selected
)
btnzero.pack(side=LEFT,expand=True,fill="both")

dot = Button(
    btnrow4,
    text=".",
    relief=GROOVE,
    border=0,
    command=btn_dot
)
dot.pack(side=LEFT,expand=True,fill="both")

btnequal = Button(
    btnrow4,
    text="=",
    relief=GROOVE,
    border=0,
    command=result
)
btnequal.pack(side=LEFT,expand=True, fill="both")

btndivide = Button(
    btnrow4,
    text="/",
    relief=GROOVE,
    border=0,
    command=btn_div
)
btndivide.pack(side=LEFT, expand=True, fill="both")

root.mainloop()