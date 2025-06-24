#功能：测试json
#说明: Python版本 3.13.5
# 参看 https://www.runoob.com/python3/python3-set.html

import os
import json

#清除控制台
os.system("cls")

#json文件
json_file = "test_json.json"

dict_json = {"language":"Python","os":"Windows","keywords":["del","print"]}

#载入学生信息
def read_file():

    #查找文件是否存在
    if not os.path.exists(json_file):
        return 
    
    # 读取文件
    with open(json_file, "r", encoding="utf-8") as f:
        global dict_json
        dict_json = json.load(f)
        print(dict_json)

    return 

#写入学生信息
def write_file():
    # 写入文件
    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(dict_json, f, indent=4, ensure_ascii=False)

    return 

#调用
read_file()
write_file()