# -*- coding: utf-8 -*-

import turtle

t = turtle.Turtle()
s = t.getscreen()
s.colormode(255)

posx = [20,170,-140,-50,70]
posy = [80,-120,37,139,-68]

t.shape("cirle")
t.shapesize(1)
t.color(255,0,0),(255,0,0)
t.penup()

#以下重覆5次:
#   取得x,y的座標

t.penup()
t.goto(20,80)
t.stamp()
t.goto(170,-120)
t.stamp()
t.goto(-140,37)
t.stamp()
t.goto(70,-68)
t.stamp()

s.mainloop()