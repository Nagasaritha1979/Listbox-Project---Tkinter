from tkinter import *

win=Tk()

def add():
    value=text.get()
    listbox1.insert(END,value)
    text.set("")
    
def delete():
    listbox1.delete(ANCHOR)
    

label1=Label(win,text="List of important cities",font=("Arial",25))
label1.place(relx=0.3,y=10)

listbox1=Listbox(win)
listbox1.place(relx=0.4,y=75)

text=StringVar()
entry1=Entry(win,textvariable=text)
entry1.place(relx=0.5,y=120)

btn1=Button(win,text="Add",command=add)
btn1.place(relx=0.5,y=150)

btn2=Button(win,text="Delete",command=delete)
btn2.place(relx=0.5,y=200)

win.mainloop()
