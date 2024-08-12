
# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%91%A8%E6%9D%B0%E4%BC%A6

# 需求 获取 https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=周杰伦  的网页源码

import urllib.request
import urllib.parse

url = 'https://www.baidu.com/s?wb='

# 请求对象的定制为了解决反爬的第一种手段UA
headers = {
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}

# 将周杰伦三个字变为unicode编码的格式
# 需要依赖于urllib.parse
name = urllib.parse.quote('周杰伦')
# print(name)

url = url+name

# 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的内容
content = response.read().decode('utf-8')

# 打印数据
print(content)
