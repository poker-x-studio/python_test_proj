#功能：测试class
#说明: Python版本 3.13.5
# 参看 https://www.runoob.com/python3/python3-class.html

import os
import inspect

#清除控制台
os.system("cls")

##学生类
class Student:
    ##属性
    name = ""
    age = 0
    __id = 0 #私有属性

    ##方法
    def __init__(self) -> None:
        #获取当前函数名
        current_function = inspect.currentframe().f_code.co_name
        print("function:", current_function)
        pass

    def __del__(self) -> None:
        #获取当前函数名
        current_function = inspect.currentframe().f_code.co_name
        print("function:", current_function)
        pass

    def create(self, name, age) -> None:
        #获取当前函数名
        current_function = inspect.currentframe().f_code.co_name
        print("function:", current_function)

        self.name = name
        self.age = age 
        return
    
    def list(self) -> None:
        #获取当前函数名
        current_function = inspect.currentframe().f_code.co_name
        print("function:", current_function)

        print(f"name:{self.name},age:{self.age}")
        return

    def __test(self) ->None: #私有方法
        #获取当前函数名
        current_function = inspect.currentframe().f_code.co_name
        print("function:", current_function)
        return 

def main():
    student = Student()
    student.create("Tom", 18)
    student.list()
    return 

if __name__ == "__main__":
    main()