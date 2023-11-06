from tkinter import *
from math import *

window=Tk()

window.title('Python Gui Calculator')
window.geometry('142x190')
window.resizable(False,False)

label1=Label(text='',bg='light grey')
label1.place(x=85,y=10)

entry=''
def clear():
    global entry
    label1.configure(text='')
    entry=''

btn1=Button(text='C',command=clear)
btn1.place(x=10,y=30)
btn1.config( height = 1, width = 3)

def sqrts():
    global entry
    entry+='sqrt('
    label1.configure(text=entry)

btn2=Button(text='√',command=sqrts)
btn2.place(x=40,y=30)
btn2.config( height = 1, width = 3)

def power():
    global entry
    entry+='^'
    label1.configure(text=entry)

btn3=Button(text='x^y',command=power)
btn3.place(x=70,y=30)
btn3.config( height = 1, width = 3)

def percent():
    global entry
    entry+='%'
    label1.configure(text=entry)

btn4=Button(text='%',command=percent)
btn4.place(x=100,y=30)
btn4.config( height = 1, width = 3)

def one():
    global entry
    entry+='1'
    label1.configure(text=entry)

btn5=Button(text='1',command=one)
btn5.place(x=10,y=55)
btn5.config( height = 1, width = 3)

def two():
    global entry
    entry+='2'
    label1.configure(text=entry)

btn6=Button(text='2',command=two)
btn6.place(x=40,y=55)
btn6.config( height = 1, width = 3)

def three():
    global entry
    entry+='3'
    label1.configure(text=entry)

btn7=Button(text='3',command=three)
btn7.place(x=70,y=55)
btn7.config( height = 1, width = 3)

def add():
    global entry
    entry+='+'
    label1.configure(text=entry)

btn8=Button(text='+',command=add)
btn8.place(x=100,y=55)
btn8.config( height = 1, width = 3)

def four():
    global entry
    entry+='4'
    label1.configure(text=entry)

btn9=Button(text='4',command=four)
btn9.place(x=10,y=80)
btn9.config( height = 1, width = 3)

def five():
    global entry
    entry+='5'
    label1.configure(text=entry)

btn10=Button(text='5',command=five)
btn10.place(x=40,y=80)
btn10.config( height = 1, width = 3)

def six():
    global entry
    entry+='6'
    label1.configure(text=entry)

btn11=Button(text='6',command=six)
btn11.place(x=70,y=80)
btn11.config( height = 1, width = 3)

def minus():
    global entry
    entry+='-'
    label1.configure(text=entry)

btn12=Button(text='-',command=minus)
btn12.place(x=100,y=80)
btn12.config( height = 1, width = 3)

def seven():
    global entry
    entry+='7'
    label1.configure(text=entry)

btn13=Button(text='7',command=seven)
btn13.place(x=10,y=105)
btn13.config( height = 1, width = 3)

def eight():
    global entry
    entry+='8'
    label1.configure(text=entry)

btn14=Button(text='8',command=eight)
btn14.place(x=40,y=105)
btn14.config( height = 1, width = 3)

def nine():
    global entry
    entry+='9'
    label1.configure(text=entry)

btn15=Button(text='9',command=nine)
btn15.place(x=70,y=105)
btn15.config( height = 1, width = 3)

def star():
    global entry
    entry+='*'
    label1.configure(text=entry)

btn16=Button(text='*',command=star)
btn16.place(x=100,y=105)
btn16.config( height = 1, width = 3)

def zero():
    global entry
    entry+='0'
    label1.configure(text=entry)

btn17=Button(text='0',command=zero)
btn17.place(x=10,y=130)
btn17.config( height = 1, width = 3)

def decimal():
    global entry
    entry+='.'
    label1.configure(text=entry)

btn18=Button(text='.',command=decimal)
btn18.place(x=40,y=130)
btn18.config( height = 1, width = 3)

def log():
    global entry
    entry+='log'
    label1.configure(text=entry)

btn19=Button(text='LOG',command=log)
btn19.place(x=70,y=130)
btn19.config( height = 1, width = 3)

def divide():
    global entry
    entry+='/'
    label1.configure(text=entry)

btn20=Button(text='/',command=divide)
btn20.place(x=100,y=130)
btn20.config( height = 1, width = 3)

def open():
    global entry
    entry+='('
    label1.configure(text=entry)

btn21=Button(text='(',command=open)
btn21.place(x=10,y=155)
btn21.config( height = 1, width = 3)

def closed():
    global entry
    entry+=')'
    label1.configure(text=entry)

btn22=Button(text=')',command=closed)
btn22.place(x=40,y=155)
btn22.config( height = 1, width = 3)

def pi():
    global entry
    entry+='3.14159'
    label1.configure(text=entry)

btn23=Button(text=u"\u03C0",command=pi)
btn23.place(x=70,y=155)
btn23.config( height = 1, width = 3)

def test():
    global entry
    entry=str(eval(entry))
    label1.configure(text=entry)
    

btn24=Button(text='=',bg='RED',command=test)
btn24.place(x=100,y=155)
btn24.config( height = 1, width = 3)



window.mainloop()