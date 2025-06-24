#功能：测试set集合
#说明: Python版本 3.13.5
# 参看 https://www.runoob.com/python3/python3-set.html

import os

#清除控制台
os.system("cls")

set_a = {0,1,2,"hello",True}
print(set_a,len(set_a)) 
print(type(set_a)) 

if 2 in set_a:
    print("存在")
else :
    print("不存在")

#遍历1
for element in set_a:
    print(element)


set_a.clear()    
print("清除之后,",set_a,len(set_a)) 
