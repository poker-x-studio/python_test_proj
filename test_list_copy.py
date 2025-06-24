#功能：测试深copy
#说明: Python版本 3.13.5

import copy
import os

#清除控制台
os.system("cls")

list0=[1,2,3,[4, 5]]

list1=list0 #赋值
list2=copy.copy(list1) #浅拷贝
list3=copy.deepcopy(list1) #深拷贝
list0[3].append(6) 

print("list0:",list0, "id:", hex(id(list0))) 
print("list1:",list1, "id:", hex(id(list1)))
print("list2:",list2, "id:", hex(id(list2)))
print("list3:",list3, "id:", hex(id(list3)))