# -*- coding: utf-8 -*-

import turtle

t = turtle.Turtle()
s = t.getscreen() #s=turtle.Screen()
#--------------
#繪圖指令放這邊
dist = int(input("請輸入要移動的距離:"))
cmd = input("輸入left向左轉，輸入right向右轉，請輸入命令:")
if cmd == "left":
    t.left(90)
else:
    if cmd == "right":
        t.right(90)
t.forward(dist)

#---------------------
#s.mainloop()
