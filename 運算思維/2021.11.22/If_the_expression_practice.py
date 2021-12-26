# -*- coding: utf-8 -*-

len_a = len("apples")
len_b = len("orange")
len_c = len("熊熊")
len_d = len("許成功")

print(len_a, len_b, len_c, len_d)

if len_a >= len_b:
    #print("apple字串比較長 或是 相等")
    if len_a == len_b:
        print("二個字的長度相同...")
    else:
        print("apple字串比較長...")
else:
    print("orange字串比較長...")
    