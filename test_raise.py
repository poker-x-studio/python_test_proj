#功能：测试抛出异常
#说明: Python版本 3.13.5

import os

#清除控制台
os.system("cls")

num = 100

def add(a,b):
    raise Exception("抛出异常")

try :
    add(1,3)
except Exception as error:    
    print("捕获到异常:%s"%(error))
    print("异常的类型:",type(error).__name__)
except :
    print("其他异常")





    