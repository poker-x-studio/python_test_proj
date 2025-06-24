#功能：石头剪刀布游戏,网络代码
#说明: Python版本 3.13.5

import random
import os

#清除控制台
os.system("cls")

#文件路径
filepath = "game_results.txt"

#常量定义
choices = ["rock", "paper", "scissors"]

while True:
    #用户输入说明
    user_choice = input("输入 rock, paper, scissors 或 quit: ").lower()

    #校验输入有效性
    if user_choice == "quit":
        break
    if user_choice not in choices:
        print("无效输入！")
        continue
    
    #电脑随机
    computer_choice = random.choice(choices)

    print(f"电脑选择: {computer_choice}")

    #比较结果
    if user_choice == computer_choice:
        print("平局！")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("你赢了！")
    else:
        print("电脑赢了！")

    #保存结果
    with open(filepath, "a") as f:
        f.write(f"玩家: {user_choice}, 电脑: {computer_choice}\n")


#删除文件
os.remove(filepath)        