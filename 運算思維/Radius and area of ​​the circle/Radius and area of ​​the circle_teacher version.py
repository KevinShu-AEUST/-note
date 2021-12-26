# -*- coding: utf-8 -*-

import math

# 1.從鍵盤取得半徑
# 2.計算面積 公式--> 半徑*半徑*3.14145926
# 3.顯示結果

#r=int(input()) # 由於半徑可以有小數，所以不轉為整數，改轉為浮點數
r=float(input("請輸入圓的半徑:"))
#rea = r* r*3.1415926 #+-*/ -->operater 運算子
#area = r**2*math.pi #operator運算子
area = math.pow(r,2)*math.pi
print("圓的面積是:", area)

