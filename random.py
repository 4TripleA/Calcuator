import tkinter as tk
from tkinter import *

root=Tk()
root.title("GUI")
root.geometry("570x600+100+50")
root.resizable(True,True)
root.configure(bg="#17161b")

equation = ""

def calculate(): 
    global equation
    result = ""
    if equation != "":
        try:
            result= eval(equation)
        except:
            result= "error"
            equation = ""
    my_label.config(text=result)
    

def show(value):
    global equation
    equation+=value
    my_label.config(text=equation)

def clear():
    global equation
    equation = ""
    my_label.config(text=equation)
    



my_label= Label(root,width=25,height=2,text="",font=("arial",30))
my_label.pack()

Button(root,text="C",width=5,height=1,font=("arial",30),bd=1,fg="#fff",bg="blue",command=lambda: clear()).place(x=10,y=100)
Button(root,text="/",width=5,height=1,font=("arial",30),bd=1,fg="#fff",bg="#e5771a",command=lambda: show("/")).place(x=150,y=100)
Button(root,text="%",width=5,height=1,font=("arial",30),bd=1,fg="#fff",bg="#e5771a",command=lambda: show("%")).place(x=290,y=100)
Button(root,text="*",width=5,height=1,font=("arial",30),bd=1,fg="#fff",bg="blue",command=lambda: show("*")).place(x=430,y=100)

Button(root,text="7",width=5,height=1,font=("arial",30),bd=1,fg="#fff",bg="blue",command=lambda: show("7")).place(x=10,y=200)
Button(root,text="8",width=5,height=1,font=("arial",30),bd=1,fg="#fff",bg="#e5771a",command=lambda: show("8")).place(x=150,y=200)
Button(root,text="9",width=5,height=1,font=("arial",30),bd=1,fg="#fff",bg="#e5771a",command=lambda: show("9")).place(x=290,y=200)
Button(root,text="-",width=5,height=1,font=("arial",30),bd=1,fg="#fff",bg="blue",command=lambda: show("-")).place(x=430,y=200)

Button(root,text="6",width=5,height=1,font=("arial",30),bd=1,fg="#fff",bg="blue",command=lambda: show("6")).place(x=10,y=300)
Button(root,text="5",width=5,height=1,font=("arial",30),bd=1,fg="#fff",bg="#e5771a",command=lambda: show("5")).place(x=150,y=300)
Button(root,text="4",width=5,height=1,font=("arial",30),bd=1,fg="#fff",bg="#e5771a",command=lambda: show("4")).place(x=290,y=300)
Button(root,text="+",width=5,height=1,font=("arial",30),bd=1,fg="#fff",bg="blue",command=lambda: show("+")).place(x=430,y=300)

Button(root,text="1",width=5,height=1,font=("arial",30),bd=1,fg="#fff",bg="blue",command=lambda: show("1")).place(x=10,y=400)
Button(root,text="2",width=5,height=1,font=("arial",30),bd=1,fg="#fff",bg="#e5771a",command=lambda: show("2")).place(x=150,y=400)
Button(root,text="3",width=5,height=1,font=("arial",30),bd=1,fg="#fff",bg="#e5771a",command=lambda: show("3")).place(x=290,y=400)
Button(root,text="=",width=5,height=3,font=("arial",30),bd=1,fg="#fff",bg="blue",command=lambda: calculate()).place(x=430,y=400)

Button(root,text="0",width=5,height=1,font=("arial",30),bd=1,fg="#fff",bg="blue",command=lambda: show("0")).place(x=10,y=500)
Button(root,text="00",width=5,height=1,font=("arial",30),bd=1,fg="#fff",bg="blue",command=lambda: show("00")).place(x=150,y=500)
Button(root,text=".",width=5,height=1,font=("arial",30),bd=1,fg="#fff",bg="gray",command=lambda: show(".")).place(x=290,y=500)


root.mainloop()

















# import re
# #print("Guess a number btw 1 and 10")

# while True:
#     n = int(input("Guess a value: "))
#     if n < 1 or n > 10:
#         print("out of range, retry")
#     elif n != 3:k
#         print("incorrect value, retry")
#     else:
#         break

# if n == 3:
#     print("correct value")

#name =input("What is your name? ")
#if name == "Abdurrahman" "abdurrahman" "ABDURRAHMAN":
 #   print(f"hello, {name}")
#else:
 #   print(f"welcome, {name}")



#my_score = int(input("put a score: "))
#message = ("I scored %s points")
#print(message % my_score)

#print("we are going to get the larger value between two value")
#A = input("Put a value for A: ")
#B = input("Put a value for B: ")

#if A > B:
 #   print("A is greater than B")
#else:
 #   print("B is greater than A")









import sys

# if len(sys.argv) < 2:
#    sys.exit("Too few arguments")

# for arg in sys.argv:
#    print("hello, my name is", arg)


# import statistics

# print(statistics.mean([100, 90]))


# from random import choice

# coin = choice(["heads", "tails"])
# print(coin)