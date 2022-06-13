from tkinter import *
main_window=Tk()
main_window.title("simple GUI")
main_window.minsize(width=400,height=400)
main_window.maxsize(width=800,height=800)
l1=Label(main_window,text="employee name",fg="blue",bg="red")
l1.place(x=0,y=10)
v=StringVar()
def edtech():
    x=v.get()
    print(x) #this will print in the output
    l2.config(text=x,bg="black",fg="white")
e1=Entry(main_window,font=("corbel",18),bd=5,textvariable=v)
e1.place(x=100,y=10)
b1=Button(main_window,text="enter",fg="yellow",bg="green",command=edtech)
b1.place(x=120,y=60)
l2=Label(main_window,text="nothing",fg="black",bg="brown")
l2.place(x=120,y=100)
main_window.mainloop()