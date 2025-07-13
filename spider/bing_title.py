#功能：爬虫-下载bing
#说明: Python版本 3.13.5

from bs4 import BeautifulSoup #解析 HTML 或 XML 数据，并提供了一些方法来导航、搜索和修改解析树
import requests #获取网页内容
from bs4 import BeautifulSoup

# 指定你想要获取标题的网站
url = 'https://cn.bing.com/' # 抓取bing搜索引擎的网页内容

# 发送HTTP请求获取网页内容
response = requests.get(url)
# 中文乱码问题
response.encoding = 'utf-8'
# 确保请求成功
if response.status_code == 200:
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(response.text, 'lxml')
   
    # 查找<title>标签
    title_tag = soup.find('title')
   
    # 打印标题文本
    if title_tag:
        print(title_tag.get_text())
    else:
        print("未找到<title>标签")

    links = soup.find_all('a') 
    print("所有的链接")
    for link in links:
        print(link.name,link['href'],link.get_text())

else:
    print("请求失败，状态码：", response.status_code)