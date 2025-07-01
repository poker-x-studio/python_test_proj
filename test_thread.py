#功能：测试线程
#说明: Python版本 3.13.5
# 参看 https://www.runoob.com/python3/python3-set.html

import os
import threading

#清除控制台
os.system("cls")

#线程函数
def thread_func(thread_index):

    #获取当前线程对象
    current_thread = threading.current_thread()
    #获取线程 ID
    thread_id = current_thread.ident
    
    #获取线程名称（可选）
    thread_name = current_thread.name 
    print(f"线程 ID: {thread_id}, 线程名称: {thread_name}")

    num = 0
    while num<10:
        print("thread_index:%d,num:%d"%(thread_index, num))
        num+=1
    return 

index = 0

# 创建新线程
while index<=4 :
    t = threading.Thread(target=thread_func, args=(index,))
    t.start()
    index+=1
