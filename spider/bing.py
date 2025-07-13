#功能：爬虫-下载bing
#说明: Python版本 3.13.5

from bs4 import BeautifulSoup #解析 HTML 或 XML 数据，并提供了一些方法来导航、搜索和修改解析树
import requests #获取网页内容
import chardet  #使用 chardet 自动检测编码

try:
    # 使用 requests 获取网页内容
    url = 'https://cn.bing.com/' # 抓取bing搜索引擎的网页内容
    response = requests.get(url)

    # 使用 BeautifulSoup 解析网页
    soup = BeautifulSoup(response.text, 'lxml')  # 使用 lxml 解析器
    # 解析网页内容 html.parser 解析器
    # soup = BeautifulSoup(response.text, 'html.parser')

    encoding = chardet.detect(response.content)['encoding']
    print(encoding)
    response.encoding = encoding
    
    # 写入文件
    with open("file\\bing.html", "w", encoding="utf-8") as f:
        f.write(soup.prettify())  # 使用 prettify() 格式化 HTML 后写入

except requests.exceptions.RequestException as e:
    print(f"请求失败: {e}")

