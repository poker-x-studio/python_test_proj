#功能：简易学生信息管理系统
#说明: Python版本 3.13.5
 
'''
使用字典dict存储所有学生信息
每个字典元素 同样使用  字典dict变量存储
{
    "name":"",
    "age":0,
    "nationality":"",
    "gender":"",
    "math_score":0,
    "english_score":0,
    "create_time":"2025-5-6 12:10"
}
'''
import os
import sys
import json
from datetime import datetime
from operator import itemgetter

#清除控制台
#os.system("cls")

#全局变量,学生字典
dict_students = {}
#json文件
json_file = "test_student_manage_system.json"

#帮助
def help():
    str = "帮助文档\n"\
            "输入create,新建，输入某个学生的信息\n"\
            "输入list,打印所有学生的信息，需要界面展示不杂乱\n"\
            "输入delete,然后输入name,可以删除某个学生的信息\n"\
            "输入order,按学生的数学分数排序，升序\n"\
            "输入quit,退出学生信息管理系统\n"
    print(str)
    return 

#创建新学生
def new_student():
    student = {
        "name":"",
        "age":0,
        "nationality":"",
        "gender":"",
        "math_score":0,
        "english_score":0,
        "create_time":""      
    }
    return student

#输入create,新建，输入某个学生的信息
def create():
    #print("进入%s()函数"%(sys._getframe().f_code.co_name))

    student = new_student()
 
    student["name"] = input("请输入学生name:").lower()

    input_string = input("请输入学生age:").lower()
    if not input_string.isdigit():#正整数检测
        print("error:输入的age错误")
        return 
    student["age"] = int(input_string)

    student["nationality"] = input("请输入学生nationality:").lower()

    student["gender"] = input("请输入学生gender:").lower()
    if student["gender"] not in ('f', 'm'):#性别检测
        print("error:输入的gender错误")
        return 
    
    input_string = input("请输入学生math_score:").lower()
    if not input_string.isdigit():#正整数检测
        print("error:输入的math_score错误")
        return 
    student["math_score"] = int(input_string)

    input_string = input("请输入学生english_score:").lower()
    if not input_string.isdigit():#正整数检测
        print("error:输入的english_score错误")
        return 
    student["english_score"] = int(input_string)

    student["create_time"] = str(datetime.now())

    print(student)

    #增加到字典中
    dict_students[student["name"]] = student
    return 

#输入list,打印所有学生的信息，需要界面展示不杂乱
def list():
    #print("进入%s()函数"%(sys._getframe().f_code.co_name))
    for key in dict_students:
        print(dict_students[key])
    return 

#输入delete,然后输入name,可以删除某个学生的信息
def delete():
    #print("进入%s()函数"%(sys._getframe().f_code.co_name))

    input_name = input("请输入需要删除学生的name:").lower()
    #查找是否存在
    if input_name not in dict_students:
        print("error:删除失败,name为{}的学生不存在".format(input_name))
        return False 
    del dict_students[input_name]
    return True

#输入order,按学生的数学分数排序，升序
def order():
    #print("进入%s()函数"%(sys._getframe().f_code.co_name))

    #按math_score升序排序
    #sorted_dict为list返回
    sorted_dict = sorted(dict_students.values(), key=itemgetter("math_score"))
    #print(sorted_dict)
    for element in sorted_dict:
        print(element)

    return 

#输入quit,退出学生信息管理系统
def quit():
    #print("进入%s()函数"%(sys._getframe().f_code.co_name))
    return 

#载入学生信息
def read_file():

    #查找文件是否存在
    if not os.path.exists(json_file):
        return 
    
    # 读取文件
    with open(json_file, "r", encoding="utf-8") as f:
        global dict_students
        dict_students = json.load(f)

    return 

#写入学生信息
def write_file():
    # 写入文件
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(dict_students, f, indent=4, ensure_ascii=False)

    return 

#执行任务
def task():
    print("执行任务,当前时间:%s\n"%(datetime.now()))

    help()
    #载入学生信息
    read_file()
    #打印
    list()
    while True:
        user_input = input("请输入:").lower()
        
        #创建
        if user_input == "create":
            create()
        #打印
        elif user_input == "list":
            list()
        #删除
        elif user_input == "delete":
            if delete():
                list() 
        #排序
        elif user_input == "order":
            order()
        #退出
        elif user_input == "quit":
            quit()
            break

    #写入学生信息
    write_file()
    return 

#调用
task()