from bs4 import BeautifulSoup
import requests         # 发送请求的模块
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
    }
for start_num in range(0,2861,20):
    response = requests.get(f"https://gaokao.chsi.com.cn/sch/search--ss-on,option-qg,searchType-1,start-{start_num}.dhtml",headers=headers)
#   requests.get(url,params,arg)     arg:其他参数，比如cookies,headers
    html = response.text          # response.text返回的是Unicode格式的文本数据
    soup = BeautifulSoup(html,"html.parser")      #创建BeautifulSoup对象    html.parser是html的解析器
    all_names = soup.find_all("a",attrs={"class":"name js-yxk-yxmc text-decoration-none"})
    for name in all_names:
        content = name.string
#        print(name.string)
        with open('yangguang.json', 'a', encoding='utf-8') as fp:
            fp.write(content)