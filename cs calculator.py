from tkinter import *
root=Tk()
root.title("CALCULATOR")
root.geometry("750x500+100+200")
root.resizable(False,False)

root.configure(bg="grey")

result = ""
def show(value):
    global result
    result+=value
    Screen.config(text=result)

def clear():
    global result
    result = ""
    Screen.config(text=result)   
def calculate():
    global result
    solve = ""
    if result !="":
        try:
            solve = eval(result)
        except:
            solve="error"
            result = ""
    Screen.config(text=solve)           

Screen = Label(root,width=27,height=2,text="",bd=6,bg="powder blue",font=("arial 25 bold"),relief=SUNKEN )
Screen.pack() 

Button(root,text="7",width=5,height=1, font=("arial 30 bold") ,bd=7,fg="#fff",bg="#2a2d36",command=lambda:show("7")).place(x=10,y=100)
Button(root,text="8",width=5,height=1, font=("arial 30 bold") ,bd=7,fg="#fff",bg="#2a2d36",command=lambda:show("8")).place(x=150,y=100)
Button(root,text="9",width=5,height=1, font=("arial 30 bold") ,bd=7,fg="#fff",bg="#2a2d36",command=lambda:show("9")).place(x=300,y=100)
Button(root,text="%",width=5,height=1, font=("arial 30 bold") ,bd=7,fg="#fff",bg="#2a2d36",command=lambda:show("%")).place(x=450,y=100)
Button(root,text="C",width=5,height=1, font=("arial 30 bold") ,bd=7,fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=600,y=100)

Button(root,text="4",width=5,height=1, font=("arial 30 bold") ,bd=7,fg="#fff",bg="#2a2d36",command=lambda:show("4")).place(x=10,y=200)
Button(root,text="5",width=5,height=1, font=("arial 30 bold") ,bd=7,fg="#fff",bg="#2a2d36",command=lambda:show("5")).place(x=150,y=200)
Button(root,text="6",width=5,height=1, font=("arial 30 bold") ,bd=7,fg="#fff",bg="#2a2d36",command=lambda:show("6")).place(x=300,y=200)
Button(root,text="*",width=5,height=1, font=("arial 30 bold") ,bd=7,fg="#fff",bg="#2a2d36",command=lambda:show("*")).place(x=450,y=200)
Button(root,text="/",width=5,height=1, font=("arial 30 bold") ,bd=7,fg="#fff",bg="#2a2d36",command=lambda:show("/")).place(x=600,y=200)

Button(root,text="1",width=5,height=1, font=("arial 30 bold") ,bd=7,fg="#fff",bg="#2a2d36",command=lambda:show("1")).place(x=10,y=300)
Button(root,text="2",width=5,height=1, font=("arial 30 bold") ,bd=7,fg="#fff",bg="#2a2d36",command=lambda:show("2")).place(x=150,y=300)
Button(root,text="3",width=5,height=1, font=("arial 30 bold") ,bd=7,fg="#fff",bg="#2a2d36",command=lambda:show("3")).place(x=300,y=300)
Button(root,text="+",width=5,height=3, font=("arial 30 bold") ,bd=7,fg="#fff",bg="#2a2d36",command=lambda:show("+")).place(x=450,y=300)
Button(root,text="-",width=5,height=1, font=("arial 30 bold") ,bd=7,fg="#fff",bg="#2a2d36",command=lambda:show("-")).place(x=600,y=300)

Button(root,text="0",width=5,height=1, font=("arial 30 bold") ,bd=7,fg="#fff",bg="#2a2d36",command=lambda:show("0")).place(x=10,y=400)
Button(root,text="00",width=5,height=1, font=("arial 30 bold") ,bd=7,fg="#fff",bg="#2a2d36",command=lambda:show("00")).place(x=150,y=400)
Button(root,text=".",width=5,height=1, font=("arial 30 bold") ,bd=7,fg="#fff",bg="#2a2d36",command=lambda:show(".")).place(x=300,y=400)
Button(root,text="=",width=5,height=1, font=("arial 30 bold") ,bd=7,fg="#fff",bg="#2a2d36",command=lambda:calculate()).place(x=600,y=400)


root.mainloop()

