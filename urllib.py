import urllib.request
import http.cookiejar

"""
    urllib 的python3.7版本简单实现
"""

url = "http://www.baidu.com"
print('第一种方法')

response1 = urllib.request.urlopen(url)
print(response1.getcode())
print(len(response1.read()))


print('第二种方法')
header = {'user-agent':'Mozilla/5.0'}

request = urllib.request.Request(url,headers=header)
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))


print('第三种方法')
cj =  http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(cj)
print(len(response3.read()))
