#功能：测试变量域
#说明: Python版本 3.13.5

import os
import time
import math
import random
import test_raise

#清除控制台
os.system("cls")

#num =1000

def test():
    # global test_raise.num 
    print(test_raise.num)
    test_raise.num =2000

test()
