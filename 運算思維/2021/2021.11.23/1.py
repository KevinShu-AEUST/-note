# -*- coding: utf-8 -*-

import turtle

t = turtle.Turtle()
s= t.getscreen()  # s=turtle.Screen()
#------------------------
#繪圖指令放這邊
dist = int(input("請輸入要移動的距離:"))
t.forward(dist)

#---------------------
s.mainloop()


