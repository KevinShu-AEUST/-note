# -*- coding: utf-8 -*-

import turtle
t=turtle.Turtle()
s=t.getscreen()
s.colormode(255)

t.pencolor((255,0,0))
# t.pensize(5)
# t.foward(100)
# t.pensize(10)
# t.forward(100)



n = int(input("幾邊形:"))
deg = 360/n

for i in range(n):
    t.pensize(i+1)
    t.forward(100)
    t.left(deg)

s.mainloop()