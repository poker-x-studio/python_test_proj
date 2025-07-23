#功能：测试数据结构交换值
#说明: Python版本 3.13.5

#从 Python 3.7 开始，dict 的实现被修改，插入顺序被保留作为字典的一部分。
#这意味着在相同的运行环境中，使用相同的键值对创建字典，循环时的顺序将是相同的，除非字典被修改（添加、删除或更新键）。

import os

#清除控制台
os.system("cls")

#交换list两个元素的值
#index_0 有效索引
#index_1 有效索引
def swap_list(list_a, index_0, index_1)->tuple:  

    #判断参数
    if not isinstance(list_a, list):
        return (False,None) 
    if not isinstance(index_0, int) or index_0<0 or index_0>=len(list_a):
        return (False,None) 
    if not isinstance(index_1, int) or index_1<0 or index_1>=len(list_a):
        return (False,None) 
    
    #保存元素的值
    source_element = list_a[index_0]
    target_element = list_a[index_1]

    index = 0 #索引
    for element in list_a:
        if index==index_0:
            list_a[index] = target_element
        if index==index_1:
            list_a[index] = source_element
        index+=1

    return (True,list_a) 

#交换dict两个元素的值
#index_0 有效索引
#index_1 有效索引
def swap_dict(dict_a, index_0, index_1)->tuple:

    #判断参数
    if not isinstance(dict_a, dict):
        return (False,None) 
    if not isinstance(index_0, int) or index_0<0 or index_0>=len(dict_a):
        return (False,None) 
    if not isinstance(index_1, int) or index_1<0 or index_1>=len(dict_a):
        return (False,None) 
    
    #保存元素的值
    index = 0 #索引
    for key in dict_a:
        if index==index_0:
            source_element = dict_a[key]
        if index==index_1:
            target_element = dict_a[key]
        index+=1

    index = 0 #索引
    for key in dict_a:
        if index==index_0:
            dict_a[key] = target_element
        if index==index_1:
            dict_a[key] = source_element
        index+=1

    return (True, dict_a)

def  main():

    print("\n\n----list----")
    index = 0
    list_a = [1,33,24,6,10]
    #交换之前
    for element in list_a:
        print(f"list交换之前,{index}:{element}")
        index+=1

    tuple_result = swap_list(list_a, 0, 4)
    if tuple_result[0]:
        index = 0
        #交换之后
        for element in tuple_result[1]:
            print(f"list交换之后,{index}:{element}")
            index+=1
    else :
        print("list交换值失败")

    print("\n\n----dict----")
    index = 0
    dict_a = {1:"1","1":1,"3":"hello","hello":True,1.233:"firth"}
    #交换之前
    for key in dict_a:
        print(f"dict交换之前,{index},{key}:{dict_a[key]}")
        index+=1

    tuple_result = swap_dict(dict_a, 0, 3)
    if tuple_result[0]:
        index = 0
        #交换之后
        for key in tuple_result[1]:
            print(f"dict交换之后,{index},{key}:{dict_a[key]}")
            index+=1
    else :
        print("dict交换值失败")

    return 

if __name__ == "__main__":
    main()

