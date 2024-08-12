
# get请求
# 获取豆瓣电影的第一页数据  并保存起来

import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}

# （1） 请求对象的定制
request = urllib.request.Request(url=url,headers=headers)

# （2）获取相应的数据
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

# （3）数据下载到本地
# open方法发默认情况下使用的是gbk的编码    如果想要保存汉字   那么需要在open方法中指定编码的格式为utf-8
# encoding = 'utf-8'
# 方法1
# fp = open('douban.json','w',encoding='utf-8')
# fp.write(content)
# 方法2
# with open('douban1.json','w',encoding = 'utf-8') as fp:
#     fp.write(content)
