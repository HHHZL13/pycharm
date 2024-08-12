# from bs4 import BeautifulSoup
# import requests
# https://gaokao.chsi.com.cn/sch/schoolInfo--schId-1,categoryId-26177,mindex-2.dhtml
# https://gaokao.chsi.com.cn/sch/schoolInfo--schId-2,categoryId-41700,mindex-2.dhtml
# https://gaokao.chsi.com.cn/sch/schoolInfo--schId-3,categoryId-36655,mindex-2.dhtml
# https://gaokao.chsi.com.cn/sch/schoolInfo--schId-4,categoryId-18283,mindex-2.dhtml
# https://gaokao.chsi.com.cn/sch/schoolInfo--schId-5,categoryId-29706,mindex-2.dhtml
#                                   ........
# https://gaokao.chsi.com.cn/sch/schoolInfo--schId-1677831015,categoryId-1677831033,mindex-2.dhtml
# https://gaokao.chsi.com.cn/sch/schoolInfo--schId-222,categoryId-65790617,mindex-2.dhtml
# https://gaokao.chsi.com.cn/sch/schoolInfo--schId-57290100,categoryId-57290109,mindex-2.dhtml
import requests
from bs4 import BeautifulSoup
def fetch_departments(url):
    # 发送HTTP请求
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
    }
    response = requests.get(url, headers=headers)

    # 检查请求是否成功
    if response.status_code != 200:
        print("Failed to retrieve data from", url)
        return []

    # 解析网页
    soup = BeautifulSoup(response.text, 'html.parser')

    # 这里需要根据实际的HTML结构来编写选择器
    # 假设所有院系信息都在一个<div>标签中，class为"departments"
    departments = soup.find_all(name="div",attrs={"class":"yxk-detail-con"}) # 需要替换为实际的class或标签

    # 提取院系名称
    department_names = []
    for department in departments:
        # 假设每个院系的名称都在一个<h3>标签中
        name = department.find('p').get_text(strip=True)  # 同样需要替换为实际的结构
        department_names.append(name)

    return department_names


# 示例URL，请替换为实际的院系信息页面URL
url = 'https://gaokao.chsi.com.cn/sch/schoolInfo--schId-1,categoryId-26177,mindex-2.dhtml'
departments = fetch_departments(url)
print(departments)
