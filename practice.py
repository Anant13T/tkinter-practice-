from tkinter import *
main_window=Tk()
main_window.title("welcome to tkinter learning")#if we want to change the tilte
main_window.minsize(width=400,height=400)#changing the window minimum size
main_window.maxsize(width=800,height=800)# change the window max size
#l1=Label(main_window,text="great learning",bg="blue",fg="white",width=40) #creating the label
#l1.place(x=50,y=100)#using the geometry configuration of widgets
#i1=PhotoImage(file="C:/Users/DELL/Pictures/Screenshots/Screenshot (205).png") #we can only use the png image
#l1=Label(main_window,image=i1)
#l1.pack()
#b1=Button(main_window,text="enter",bg="green",fg="white") # creating the button 
#b1.pack()
#e1=Entry(main_window,width=20,bd=5,font=("calibri",20)) #to get the user input we use the entry here bd is the border size
#e1.pack()
#cb=Checkbutton(main_window,text="male")
#cb.pack()
#working with frame
#f1=Frame()
#f1.pack()
#f2=Frame()
#f2.pack(side=BOTTOM)
#l1=Label(f1,text="learning")
#l1.pack()
#l2=Label(f2,text="experience")
#l2.pack()
#working with list box 
lb1=Listbox(main_window,width=20)
lb1.pack()
l1=["tony","india","Anant"]
for i in l1:
    lb1.insert(END,i)
def re():
    lb1.delete(ANCHOR)
b1=Button(main_window,text="remove",bg="red",command=re)
b1.pack()
main_window.mainloop()