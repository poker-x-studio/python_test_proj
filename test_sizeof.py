#功能：测试变量的字节数
#说明: Python版本 3.13.5

'''
在 Python 中,PyLongObject 是用于表示整数 (int) 的 C 语言结构体，定义在 Python 源代码的 Include/longobject.h 文件中。以下是 Python 3.10（及类似版本）中 PyLongObject 结构体的定义和相关解释。

typedef struct _longobject {
    PyObject_HEAD
    Py_ssize_t ob_size;   /* Number of digits (can be negative for negative numbers) */
    digit ob_digit[1];    /* Array of digits, flexible array member */
} PyLongObject;

64位系统
PyObject_HEAD 通常占用 16 字节
Py_ssize_t 是 8 字节
ob_digit[1] 占用 4 字节。
'''
import os
import sys

#清除控制台
os.system("cls")

num = 100
print(sys.getsizeof(num))

msg = "hello"
print(sys.getsizeof(msg))

set_a = (1,2,3.0)
print(sys.getsizeof(set_a))

list_a =[6,6,11,5,49]
print(sys.getsizeof(list_a))

list_b =["hello", True,5,True, 49.66]
print(sys.getsizeof(list_b))

