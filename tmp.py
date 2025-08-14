#功能：临时文件
#说明: Python版本 3.13.5

import os

#清除控制台
os.system("cls")

'''
#功能：客户端
#导入socket
import socket

#创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 810))

#发送数据
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

#接受数据
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)   

#关闭连接：
s.close()

header,html = data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
print(html.decode('utf-8'))

#写入文件
with open('sina.html', 'wb') as f:
    f.write(html) 


'''

print(list(range(6)))
print(list(range(1,6)))
print(list(range(1,6,2)))
print(list(range(1,6,-2)))


