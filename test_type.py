#功能：测试type
#说明: Python版本 3.13.5

import os

#清除控制台
os.system("cls")

print(type(1)) 
print(type("hello")) 
print(type((1,2,3))) 
print(type([1,2,3])) 
print(type({1,2,3})) 
print(type({1:1,2:2,3:3})) 
print(type(True)) 
print(type(1.6)) 

print(os.__file__)
