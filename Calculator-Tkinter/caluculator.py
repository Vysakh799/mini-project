import tkinter
win=tkinter.Tk()
def num(num):
    e1.insert('end',num)
def eql():
    e2.delete(0,'end')
    ans=str(eval(e1.get()))
    e2.insert('end',ans)
def clear():
    e1.delete(0,'end')
    e2.delete(0,'end')
def back():
    us=e1.get()
    length=len(us)
    print(length)
    e1.delete(length-1,'end')
    e2.delete(0,'end')
win.title("Calculator")
win.geometry("400x400")
win.configure(background="whitesmoke")

e1=tkinter.Entry(win,background="white",width=20)
e1.grid(row=0,column=0,columnspan=2)

e2=tkinter.Entry(win,background="white",width=20)
e2.grid(row=0,column=2 ,columnspan=2)

b7=tkinter.Button(text="7",background='white',foreground="black",activebackground="green",pady=20,padx=30,command=lambda:num(7))
b7.grid(row=1,column=0)

b8=tkinter.Button(text="8",background='white',pady=20,padx=30,command=lambda:num(8))
b8.grid(row=1,column=1)

b9=tkinter.Button(text="9",background='white',pady=20,padx=30,command=lambda:num(9))
b9.grid(row=1,column=2)

add=tkinter.Button(text="+",background='white',pady=20,padx=30,command=lambda:num("+"))
add.grid(row=1,column=3)

b4=tkinter.Button(text="4",background='white',pady=20,padx=30,command=lambda:num(4))
b4.grid(row=2,column=0)

b5=tkinter.Button(text="5",background='white',pady=20,padx=30,command=lambda:num(5))
b5.grid(row=2,column=1)

b6=tkinter.Button(text="6",background='white',pady=20,padx=30,command=lambda:num(6))
b6.grid(row=2,column=2)

sub=tkinter.Button(text="-",background='white',pady=20,padx=30,command=lambda:num("-"))
sub.grid(row=2,column=3)

b1=tkinter.Button(text="1",background='white',pady=20,padx=30,command=lambda:num(1))
b1.grid(row=3,column=0)

b2=tkinter.Button(text="2",background='white',pady=20,padx=30,command=lambda:num(2))
b2.grid(row=3,column=1)

b3=tkinter.Button(text="3",background='white',pady=20,padx=30,command=lambda:num(3))
b3.grid(row=3,column=2)

mul=tkinter.Button(text="*",background='white',pady=20,padx=30,command=lambda:num("*"))
mul.grid(row=3,column=3)

b0=tkinter.Button(text="0",background='white',pady=20,padx=30,command=lambda:num(0))
b0.grid(row=4,column=0)

clear=tkinter.Button(text="C",background='white',pady=20,padx=30,command=clear)
clear.grid(row=4,column=1)

equal=tkinter.Button(text="=",background='white',pady=20,padx=30,command=eql)
equal.grid(row=4,column=2)

div=tkinter.Button(text="/",background='white',pady=20,padx=30,command=lambda:num("/"))
div.grid(row=4,column=3)

back=tkinter.Button(text="<-",background='white',pady=20,padx=30,command=back)
back.grid(row=5,column=3)

win.mainloop()
