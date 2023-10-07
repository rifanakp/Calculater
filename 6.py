from tkinter import *
import tkinter as tk
root = tk.Tk()
def clicked(num):
    first_num=txt.get()
    txt.delete(0,(END))
    txt.insert(0,str(first_num)+str(num))
def add():
    first_number=txt.get()
    global old_value
    old_value=int(first_number)
    global math
    math="add"
    txt.delete(0,END)
def sub():
    first_number=txt.get()
    global old_value
    old_value=int(first_number)
    global math
    math="sub"
    txt.delete(0,END)
def div():
    first_number=txt.get()
    global old_value
    old_value=int(first_number)
    global math
    math="div"
    txt.delete(0,END)
def mult():
    first_number=txt.get()
    global old_value
    old_value=int(first_number)
    global math
    math="mult"
    txt.delete(0,END)
def clear():
    txt.delete(0,END)
def equal():
    if math=="add":
        new_value=txt.get()
        txt.delete(0,END)
        txt.insert(0,int(old_value)+int(new_value))
    if math=="sub":
        new_value=txt.get()
        txt.delete(0,END)
        txt.insert(0,int(old_value)-int(new_value))
    if math=="div":
        new_value=txt.get()
        txt.delete(0,END)
        txt.insert(0,int(old_value)/int(new_value))
    if math=="mult":
        new_value=txt.get()
        txt.delete(0,END)
        txt.insert(0,int(old_value)*int(new_value))
root.title("Calculator")
root.geometry('200x400')
txt=Entry()
txt.place(x=10,y=10)
btn=Button(text="C").place(x=25,y=100)
btn1=Button(text="%").place(x=65,y=100)
btn2=Button(text="Clr",command=clear).place(x=105,y=100)
btn3=Button(text="/",command=div).place(x=145,y=100)
btn4=Button(text="7",command=lambda:clicked(7)).place(x=25,y=150)
btn5=Button(text="8",command=lambda:clicked(8)).place(x=65,y=150)
btn6=Button(text="9",command=lambda:clicked(9)).place(x=105,y=150)
btn7=Button(text="*",command=mult).place(x=145,y=150)
btn8=Button(text="4",command=lambda:clicked(4)).place(x=25,y=200)
btn9=Button(text="5",command=lambda:clicked(5)).place(x=65,y=200)
btn10=Button(text="6",command=lambda:clicked(6)).place(x=105,y=200)
btn11=Button(text="-",command=sub).place(x=145,y=200)
btn12=Button(text="1",command=lambda:clicked(1)).place(x=25,y=250)
btn13=Button(text="2",command=lambda:clicked(2)).place(x=65,y=250)
btn14=Button(text="3",command=lambda:clicked(3)).place(x=105,y=250)
btn15=Button(text="+",command=add).place(x=145,y=250)
btn16=Button(text="00",command=lambda:clicked(00)).place(x=25,y=300)
btn17=Button(text="0",command=lambda:clicked(0)).place(x=65,y=300)
btn18=Button(text=".").place(x=105,y=300)
btn19=Button(text="=", command=equal).place(x=145,y=300)
root.mainloop()