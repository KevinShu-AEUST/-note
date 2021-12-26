# -*- coding: utf-8 -*-
rate=float(input())
if rate >= 4.0 and rate < 6.0:
    print("哇，匯率不錯耶……")
    print("那你想換多少?")
    num = float(input("請輸入要換的NT金額:"))
    result = num*rate
    print("最後可以換JP=",result)
else:
    print("匯率太低，不建議換匯…")
    print("請明天再來看看…")
print("Bye bye")