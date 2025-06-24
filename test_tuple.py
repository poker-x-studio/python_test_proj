#功能：测试tuple元组
#说明: Python版本 3.13.5
# 参看 https://www.runoob.com/python3/python3-tuple.html

import os

#清除控制台
os.system("cls")

tuple = (0,1,2)
print(tuple) 
print(type(tuple)) 

#元组元素不能修改
#tuple[0] = 100

#16进制输出tuple地址
print(hex(id(tuple)))

del tuple 
print("删除tuple后输出:",tuple)