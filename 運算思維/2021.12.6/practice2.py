# -*- coding: utf-8 -*-


import turtle
t = turtle.Turtle()
for i in range(3):
    n=int(input("幾邊形"))
    deg=360/n
    
    for i in range(n):
        t.pensize(i+1)
        t.forward(100)
        t.left(deg)
