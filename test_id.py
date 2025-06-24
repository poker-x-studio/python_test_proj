#功能：测试变量地址
#说明: Python版本 3.13.5

import os

#清除控制台
os.system("cls")

a=100
print(hex(id(a)))

print("\nlist 变量相关的地址输出:")
list_a = [1,2,3]
print(hex(id(list_a)))

for element in list_a:
    print(hex(id(element)))

print("\ndict 变量相关的地址输出:")
dict_a = {1:1,2:2,3:3}
print(hex(id(dict_a)))

for element in dict_a:
    print(hex(id(element)))