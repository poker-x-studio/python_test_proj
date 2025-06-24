#功能：临时文件
#说明: Python版本 3.13.5

import os

#清除控制台
os.system("cls")

def chek_type(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers")
    return True
a=100
b=200
# 定义add函数
def add(a, b):
  if chek_type(a, b):
      return a + b

#调用函数
printme = add(a, "ddd")
print(printme)