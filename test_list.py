#功能：测试list列表
#说明: Python版本 3.13.5

import os

#清除控制台
os.system("cls")

#输出当前文件
print("current file: " + os.path.abspath(__file__))

#输出list
list_a = [4,6,11,5,49]
print(list_a,len(list_a), max(list_a), min(list_a))

list_a.append(1000)
print("追加1000后:",list_a,len(list_a), max(list_a), min(list_a))

del(list_a[0])
print("删除4后:",list_a,len(list_a), max(list_a), min(list_a))

list_b = list_a.copy()
print(list_a)
print(list_b)

list_b.remove(11)
print(list_a)
print(list_b)


list =[6,6,11,5,49]
print ( list )
length = len(list)
print( length )
max_value = max(list)
print( max_value )
min_value = min(list)
print( min_value )
list =[6,6,11,5,49]
list.append(1000)
print( list )
length = len(list)
print( length )
max_value = max(list)
print( max_value )  
min_value = min(list)
print( min_value )
del(list[0])
print( list )
length = len(list)
print( length )
max_value = max(list)
print( max_value )
min_value = min(list)
print( min_value )


list_c =["hello", True,5,True, 49.66]
print("list_c:",list_c)
length_c = len(list_c)
print("length_c:", length_c) 

#浅copy
list_d = list_c.copy()
print("list_d:",list_d)
length_d = len(list_d)
print("length_d:", length_d) 

#移除列表中某个值的第一个匹配项
list_c.remove(True)
print("删除之后:") 

print("list_c:",list_c)
length_c = len(list_c)
print("length_c:", len(list_c)) 

print("list_d:",list_d)
length_d = len(list_d)
print("length_d:", length_d) 

'''
#遍历1
for element in list_a:
    print(element)

#遍历2
for index in range(len(list_a)):
    print("序号：%s,值：%s" % (index, list_a[index]))

list_a[0] = "b2"
for element in list_a:
    print(element)
'''