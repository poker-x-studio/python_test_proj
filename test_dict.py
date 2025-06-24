#功能：测试dict字典
#说明: Python版本 3.13.5

import os

#清除控制台
os.system("cls")

dict_a = {1:"1","1":1,"3":"hello","hello":True,1.233:"firth"}
print(dict_a,len(dict_a)) 
print(type(dict_a)) 

print("dict_a[\"1\"]:",dict_a["1"])
print("dict_a[1]:",dict_a[1])


if 12 in dict_a:
    print("存在")
else :
    print("不存在")

#遍历1
for element in dict_a:
    print(element)

dict_a.clear()
print(dict_a,len(dict_a)) 

