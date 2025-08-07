#功能：测试
#说明: Python版本 3.13.5

import pygame
import sys
import random
import os

#倒叙输出字符串
def print_string(txt)->None :
    new_txt = ""
    for i in range(len(txt) - 1, -1, -1):
        new_txt += txt[i]

    print(new_txt)
    return      

def main():
    test_string = "Hello, World!"
    print_string(test_string)
    return 

if __name__ == "__main__":
    main()