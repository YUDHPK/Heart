#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox  # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
top = Tk()
# Code to add widgets will go here...

def goRight():
	msg = messagebox.showinfo( "goRight", "Right")

def goLeft():
	msg=messagebox.showinfo("goLeft","Left")

def checkMale():
	c2.deselect()

def checkFemale():
	print(CheckVar2)
	if CheckVar2==1:
		c1.deselect()

top.title("Heart Disease prediction")
top.geometry("500x500")


CheckVar1=0
CheckVar2=0

c1=Checkbutton(top,text="Male",variable=CheckVar1,onvalue=1,offvalue=0,height=5,width=20,command=checkMale)
c2=Checkbutton(top,text="Female",variable=CheckVar2,onvalue=1,offvalue=0,height=5,width=20,command=checkFemale)

c1.place(x=50,y=50)
c2.place(x=200,y=50)

glbl=Label(top,text="Gender")
glbl.pack()
br=Button(top,text="->",command=goRight,padx=20,bd=1)
br.place(x=400,y=450)
bl=Button(top,text="<-",command=goLeft,padx=20,bd=1)
bl.place(x=50,y=450)




top.mainloop()