
“”“  
beautifulsoup4 的简单使用方法
”“”

import bs4
import re
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


soup = bs4.BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')   # 三个参数分别为文档字符串，解析器，指定编码

print('获取所有链接')
links = soup.find_all('a')
for link in links:
    print(link.name,link['href'],link.get_text())


print('获取lacie的链接')
link_node = soup.find('a',href='http://example.com/lacie')                # find返回值可在次find 而find_all不行
print(link_node.name,link_node['href'],link_node.get_text())

print('正则表达式匹配')
link_node = soup.find('a',href=re.compile(r"ill"))

print('获取p段落文字')
p_node = soup.find('p',class_='title')                      # 等价 soup.find('p', attrs={'class':'title'})
print(p_node.name,p_node.get_text())


print(soup.prettify())            # 格式化soup文件
