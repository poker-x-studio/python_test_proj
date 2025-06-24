#功能：测试文件
#说明: Python版本 3.13.5
# 参看 https://www.runoob.com/python3/python3-file-methods.html

import os
import os.path

#清除控制台
os.system("cls")

#文件路径
filepath = "info.txt"

file = open(filepath,'w+')
# 获取当前文件位置
pos = file.tell()
print ("当前位置: %d" % (pos))

write_len = file.write("hello\n")
print("write_len:",write_len)
write_len = file.write("good")
print("write_len:",write_len)

# 获取当前文件位置
pos = file.tell()
print ("当前位置: %d" % (pos))

# 重新设置文件读取指针到开头
file.seek(0, 0)

str = file.read()
print("str:",str)

# 获取当前文件位置
pos = file.tell()
print ("当前位置: %d" % (pos))

#关闭文件
file.close()

#删除文件
os.remove(filepath)


path = "D:/private/no-style-please/_posts/2025-06-24-post.md"
filename = os.path.basename(path)
name, ext = os.path.splitext(filename)

print(f"文件名: {filename}")  # 2025-06-24-post.md
print(f"文件名（无扩展名）: {name}")  # 2025-06-24-post
print(f"扩展名: {ext}")  # .md