# print("Hello,World!!!")
"""money=50
print("当前钱包余额： ",money)
money=money-10-5
print("购买了冰激凌，花费： ",10)
print("购买了可乐，花费： ",5)
print("最终，钱包剩余： ",money)"""
# print("2**3= ",2**3)
# print("请告诉我你是谁？")
# print("欢迎来到黑马儿游乐园，儿童免费，成人收费")
"""age =int(input("请输入你的年龄: "))
if age >= 18 :
    print("您已成年,请补票10元")
else:
    print('你未成年,免费游玩')52
print("祝你玩的愉快")"""
"""
#随机生成一个数字
import random
num = random.randint(1,100)
#定义一个变量，记录猜测的次数
count = 0
flag = True
while flag:#flag为True时执行循环
    guess_num = int(input("请输入你猜测的数字 "))
    count += 1
    if guess_num == num:
        print("猜中了")
        flag = False
    else:
        if guess_num > num:
            print("你猜大了")
        else:
            print("你猜小了")
print(f"你一共猜了{count}次")"""
"""i = 1
while i <= 100:
    print(f"今天是{i}天，准备表白....")
    j = 1
    while j<= 10:
        print(f"送给小美第{j}支玫瑰花")
        j += 1
    print("小美我喜欢你")
    i += 1
print(f"坚持到第{i - 1}天，表白成功")"""
#print("Hello ",end='')
#print("World",end='')
#print("Hello\tWorld")
#print("HD\tbest")
#定义外层循环变量
"""i = 1
while i <= 9:
    #定义内层循环变量
    j = 1
    while j <= i:
        #内层循环的print语句，不需要换行，通过\t制表符进行对齐
        print(f"{i}*{j}={i*j}\t",end='')
        j += 1

    i += 1
# print空内容，就是输出一个换行
    print()"""
# name = "itheima"
# for x in name:
#     print(x)
# name = "itheima is a brand of itcast"
# count = 0
# for x in name:
#     if x == 'a':
#         count += 1
# print(f"itheima is a brand of itcast中共有：{count}个字母a")
#range 语法1
# for x in range(10):
#     print(x)
#range 语法2
# for x in range(5,10):
#     print(x)
#range 语法3
# for x in range(5,10,2):
 #从5开始，到10结束（不包含10）的一个数字序列，数字之间的间隔是2
#     print(x)
# for x in range(1,10):
#     for y in range(1,x+1):
#         print(f"{x}*{y}={x*y}\t",end='')
#     print()
# money = 10000
# for i in range(1,21):
#     import random
#     score = random.randint(1,10)
#     if score < 5:
#         print(f'员工{i}绩效分{score},不满足，不发工资，下一位')
#         continue
#     if money >= 1000:
#         money-=1000
#         print(f"员工{i}，满足条件发放工资1000，公司账户余额：{money}")
#     else:
#         print(f"余额不足，当前余额：{money}元，不足以发工资，不发了，下个月发")
#         break
# def tem(x):
#     if x<=37.5:
#         print(f"欢迎来到黑马程序员！请出示你的健康码，并配合测量体温！\n体温测量中，你的体温是：{x},体温正常请进入")
#     else:
#         print(f"欢迎来到黑马程序员！请出示你的健康码，并配合测量体温！\n体温测量中，你的体温是：{x},需要隔离")
#  x = input("请输入你的体温 ")
# tem(40)
# def add (x,y):
#     result = x + y
#     return result
# r = add(5,6)
# print(r)
# ATM机
# 定义全局变量money,name
# money = 500000
# name = None
# # 要求客户输入姓名
# name = input("请输入您的姓名：")
# # 定义查询函数
# def query(show_header):
#     if show_header:
#         print("------------查询余额------------")
#     print(f"{name},您好，您的余额剩余：{money}元")
#
# # 定义存款函数
# def saving(num):
#     global money
#     money += num
#     print("--------------存款--------------")
#     print(f"{name}，您好，您存款{num}元成功。")
#
#     # 调用query函数查询余额
#     query(False)
#
# # 定义取款函数
# def get_money(num):
#     global money
#     money -= num
#     print("--------------取款--------------")
#     print(f"{name}，您好，您取款{num}元成功。")
#     #调用query函数查询余额
#     if money>=0:
#         query(False)
#     else:
#         print(f"您当前余额不足,余额为{money}元")
# # 定义主菜单函数
# def main():
#     print("-------------主菜单--------------")
#     print(f"{name},您好，欢迎来到python银行ATM。请选择操作：")
#     print("查询余额\t[输入1]")
#     print("存款\t\t[输入2]")
#     print("取款\t\t[输入3]")
#     print("退出\t\t[输入4]")
#     return input("请输入您的选择：")
#
# # 设置无限续循环，确保程序不退出
# while True:
#     keyboard_input = main()
#     if keyboard_input == "1":
#         query(True)
#         continue         # 通过continue继续下一个循环，一进来就是回到主菜单
#     elif keyboard_input == "2":
#         num = int(input("您想要存多少钱？请输入："))
#         saving(num)
#         continue
#     elif keyboard_input == "3":
#         num = int(input("您想要去取少钱？请输入："))
#         get_money(num)
#         continue
#     else:
#         print("程序退出啦")
#         break          # 通过break退出循环
# 定义一个列表
# my_list = ["itheima","itcast","python"]
# print(my_list)
# print(type(my_list))
# # 定义一个嵌套的列表
# my_list = [[1,2,3],[4,5,6]]
# print(my_list)
# print(type(my_list))
# 语法：列表【下标索引】
# name_list = ["Tom","Lily","Rose"]
# print(name_list[0])   #Tom
# print(name_list[1])   #Lily
# print(name_list[2])   #Rose
# print(name_list[-1])    #Rose
# print(name_list[-2])    #Lily
# print(name_list[-3])    #Tom
# my_list = [[1,2,3],[4,5,6]]
# print(my_list[1][1])      # 5
# mylist = ["itcast","itheima","python"]
# # 1.查找某元素在列表内的下标索引
# # index = mylist.index("python")
# # print(index)
# # 2.修改特定下标索引的值
# mylist[0] = "传智教育"
# print(mylist)
# # 3.在指定下标位置插入新元素
# mylist.insert(1,"best")
# print(mylist)
# # 4.在列表的尾部追加'''单个'''新元素
# mylist.append("黑马程序员")
# print(mylist)
# # 5.在列表的尾部追加'''一批'''新元素
# mylist2 = [1,2,3]
# mylist.extend(mylist2)
# print(mylist)
# 6.删除指定下标索引的元素（2种方式）
# mylist = ["itcast","itheima","python"]
# 6.1 方式1：del 列表[下标]
# del mylist[2]
# print(mylist)
# 6.2 方式2：列表.pop(下标)
# mylist = ["itcast","itheima","python"]
# element = mylist.pop(2)
# print(mylist)
# print(element)
# 7.删除某元素在列表中的第一个匹配项
# mylist = ["itcast","itheima","itcast","itheima","python"]
# mylist.remove("itheima")
# print(mylist)
# 8.清空列表
# mylist.clear()
# print(mylist)
# 9.统计列表内某元素的数量
# mylist = ["itcast","itheima","itcast","itheima","python"]
# count = mylist.count('itheima')
# print(count)
# 10.统计列表中全部的元素个数
# mylist = ["itcast","itheima","itcast","itheima","python"]
# n = len(mylist)
# print(n)
# age = [21,25,21,23,22,20]
# age.append(31)
# print(age)
# age2 = [29,33,30]
# age.extend(age2)
# print(age)
# num1 = age[0]
# print(num1)
# num2 = age[-1]
# print(num2)
# index = age.index(31)
# print(index)
# 取出列表中的偶数
# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = []
# print(len(list1))    # 查看当前列表的元素个数
# for i in list1:
#     if i%2==0:
#         list2.append(i)
# print(list2)
# list3 = []
# i = 1
# k = len(list1)
# while i<=k :
#     if i%2 ==0:
#         list3.append(i)
#     i+=1
# print(list3)
# 定义元组
# 元组的嵌套
# t5 = ((1,2,3),(4,5,6))
# print(f"t5的类型是{type(t5)},内容是{t5}")
# 下标索引取出内容
# num = t5[1][2]
# print(f"从嵌套元组中取出的数据是:{num}")
# index查找
# t6 = ("传智教育",'黑马程序员',"python")
# index = t6.index("黑马程序员")
# print(index)
# count统计方法
# t7 = ("传智教育","黑马程序员",'黑马程序员',"黑马程序员","python")
# num = t7.count("黑马程序员")
# print(num)
# len函数统计元组元素数目
# t8 = ("传智教育","黑马程序员",'黑马程序员',"黑马程序员","python")
# num = len(t8)
# print(num)
# 元组的遍历：while
# index = 0
# while index < len(t8):
#     print(f"元组的元素有:{t8[index]}")
#     index+=1
# 元组的遍历：for
# for i in t8:
#     print(f"元组的元素有：{i}")
# 练习
# t = ("周杰伦",11,["football","music"])
# x1 = t.index(11)
# print(x1)
# print(f"学生的姓名是；{t[0]}")
# del t[2][0]
# print(t)
# 字符串
# my_str = "itheima and itcast"
# 通过下标索引取值
# value = my_str[2]
# value2 = my_str[-16]
# print(value,value2)

# index方法
# value = my_str.index("and")
# print(f"在字符串{my_str}中查找and，其起始下标是：{value}")

# replace方法
# new_my_str = my_str.replace("it","程序")
# print(new_my_str)

# split方法
# my_str = "hello python itheima itcast"
# my_str_list = my_str.split(' ')
# print(f"将字符串{my_str}进行split切分后得到：{my_str_list},类型是:{type(my_str_list)}")

# strip方法
# my_str = "   itheima and itcast   "
# new_str = my_str.strip()
# print(f"字符串{my_str}被strip后，结果是；{new_str}")      #去掉了空格
# my_str1 = "12itheima and itcast21"
# new_str1 = my_str1.strip("12")
# print(f"字符串{my_str1}被strip后，结果是；{new_str1}")

# 统计字符串中某字符串出现次数  ,count
# my_str = "itheima and itcast"
# count = my_str.count("it")
# print(f"it在字符串中出现的次数：{count}")

# 统计字符串长度
# num = len(my_str)
# print(f"字符串的长度是：{num}")

# 练习
# str = "itheima itcast boxuegu"
# count = str.count("it")
# print(f"it在字符串中出现了：{count}次")
# new_str = str.replace(" ","|")
# print(f"原字符串{str}被|替换后为：{new_str}")
# str2 = new_str.split("|")
# print(f"以|分割得到：{str2}")
# 切片
# 对list进行切片，从1开始，4结束，步长为1
# my_list = [0,1,2,3,4,5,6]
# list = my_list[1:4]        # 到4为止，不包含4
# print(list)

# 对tuple进行切片，从头开始，到最后结束，步长为1
# my_tuple = (0,1,2,3,4,5,6)
# tuple = my_list[:]
# print(tuple)

# 对str进行切片，从头开始到最后结束，步长为2
# my_str = "01234567"
# str = my_str[::2]
# print(str)

# 对str进行切片，从头开始，到最后结束，步长为-1
# my_str = "01234567"
# str = my_str[::-1]          # 等同于将序列反转
# print(str)

# 对列表进行切片，从3开始，到1结束，步长为-1
# my_list = [0,1,2,3,4,5,6]
# list = my_list[3:1:-1]
# print(list)

# 对元组进行切片，从头开始，到最后结束，步长为-2
# my_tuple = (0,1,2,3,4,5,6)
# tuple = my_tuple[::-2]
# print(tuple)

# 练习
# str = "万过薪月，员序程马黑来，nohtyp学"
# str1 = str[::-1]
# print(str1)
# str2 =str1[9:14:1]
# print(str2)

# 集合
# 定义集合
# my_set = {"传智教育","黑马程序员","itheima","传智教育","黑马程序员","itheima","传智教育","黑马程序员","itheima"}
# my_set_empty = set()
# print(f"my_set的内容是：{my_set},类型是：{type(my_set)}")       # 不允许重复，且乱序
# print(f"my_set_empty的内容是：{my_set_empty},类型是：{type(my_set_empty)}")

# 添加新元素
# my_set.add("Python")
# print(f"my_set添加一个元素后结果是:{my_set}")

# 移除元素
# my_set.remove("黑马程序员")
# print(f"my_set移除一个元素结果是:{my_set}")

# 随机取出一个元素
# my_set = {"传智教育","黑马程序员","itheima"}
# element = my_set.pop()
# print(f"集合被取出元素是：{element},取出元素后:{my_set}")

# 清空集合
# my_set.clear()
# print(my_set)

# 取两个集合的差集
# set1 = {1,2,3}
# set2 = {1,5,6}
# set3 = set1.difference(set2)
# print(set3)
# print(set1)
# print(set2)

# 消除2个集合的差集
# set1.difference_update(set2)
# print(set1)
# print(set2)

# 2个集合合并为1个集合
# set1 = {1,2,3}
# set2 = {1,5,6}
# set3 = set1.union(set2)
# print(set3)
# print(set1)
# print(set2)

# 统计集合元素数量
# set = {1,2,3,4,5}
# num = len(set)
# print(num)

# 集合的遍历
# 集合不支持下标索引，所以不能用while循环
# set1 = {1,2,3,4,5}
# for element in set1:
#     print(f"集合的元素有：{element}")

# 练习
# my_list = ["黑马程序员","传智播客","黑马程序员","传智播客","itheima","itcast","itheima","itcast","best"]
# my_set = set()
# for element in my_list:
#     print(f"my_list元素有：{element}")
#     my_set.add(element)
# print(my_set)

# 定义字典
# my_dict1 = {"aaa":99,"bbb":88,"ccc":77}
# 定义空字典
# my_dict2 = {}
# my_dict3 = dict()
# print(f"字典1的内容是；{my_dict1},类型是：{type(my_dict1)}")
# print(f"字典2的内容是；{my_dict2},类型是：{type(my_dict2)}")
# print(f"字典3的内容是；{my_dict3},类型是：{type(my_dict3)}")

# 定义重复key的字典
# my_dict1 = {"aaa":99,"aaa":88,"ccc":77}
# print(f"重复key的字典的内容是：{my_dict1}")

# 从字典中基于key获取value
# my_dict1 = {"aaa":99,"bbb":88,"ccc":77}
# score = my_dict1["aaa"]
# print(f"a的考试分数是：{score}")
# 定义嵌套字典
# stu_score_dict = {
#     "aaa":{
#         "语文":77,
#         "数学":66,
#         "英语":33
#     },"bbb":{
#         "语文":88,
#         "数学":86,
#         "英语":55
#     },"ccc":{
#         "语文":99,
#         "数学":96,
#         "英语":66
#     }
# }
# print(f"学生的考试信息是：{stu_score_dict}")

# 从嵌套字典中获取数据
# score = stu_score_dict["aaa"]["语文"]
# print(f"aaa的语文成绩是：{score}")

# dict = {"aaa":99,"bbb":88,"ccc":77}
# 新增元素
# dict["ddd"]=66
# print(f"新增元素后结果是：{dict}")

# 更新元素
# dict["aaa"]=33
# print(f"更新元素后结果是：{dict}")

# 删除元素
# score = dict.pop("aaa")
# print(f"字典中被移除一个元素结果是：{dict},aaa的考试分数是：{score}")

# 清空元素
# dict.clear()
# print(f"字典被清空了结果是：{dict}")

# 获取全部的key
# dict = {"aaa":99,"bbb":88,"ccc":77}
# keys = dict.keys()
# print(keys)

# 遍历字典
# for key in keys :
#     print(f"字典的key是：{key}")
#     print(f"字典的value是：{dict[key]}")

# 统计字典内的元素个数
# num = len(dict)
# print(num)

# 练习
# dict = {"aaa":{"部门":"科技部","工资":3000,"级别":1},
#         "bbb":{"部门":"市场部","工资":5000,"级别":2},
#         "ccc":{"部门":"市场部","工资":7000,"级别":3},
#         "ddd":{"部门":"科技部","工资":4000,"级别":1},
#         "eee":{"部门":"市场部","工资":6000,"级别":2}
# }
# for key in dict:
#     if dict[key]["级别"] == 1:
#         dict[key]["工资"]+=1000
#         dict[key]["级别"]+=1
# print(dict)
#
# my_list = [1,2,3,4,5]
# my_tuple = (1,2,3,4,5)
# my_str = "abcdefg"
# my_set = {1,2,3,4,5}
# my_dict = {"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}
#
# # len元素个数
# print(f"列表元素个数有：{len(my_list)}")
# print(f"元组元素个数有：{len(my_tuple)}")
# print(f"字符串元素个数有：{len(my_str)}")
# print(f"集合元素个数有：{len(my_set)}")
# print(f"字典元素个数有：{len(my_dict)}")
#
# # max最大元素
# print(f"列表  最大的元素是：{max(my_list)}")
# print(f"元组  最大的元素是：{max(my_tuple)}")
# print(f"字符串最大的元素是：{max(my_str)}")
# print(f"集合  最大的元素是：{max(my_set)}")
# print(f"字典  最大的元素是：{max(my_dict)}")
#
# # min最小元素
# print(f"列表  最小的元素是：{min(my_list)}")
# print(f"元组  最小的元素是：{min(my_tuple)}")
# print(f"字符串最小的元素是：{min(my_str)}")
# print(f"集合  最小的元素是：{min(my_set)}")
# print(f"字典  最小的元素是：{min(my_dict)}")

# 类型转换：容器转列表
# print(f"列表转列表的结果是:{list(my_list)}")
# print(f"元组转列表的结果是:{list(my_tuple)}")
# print(f"字符串转列表的结果是:{list(my_str)}")
# print(f"集合转列表的结果是:{list(my_set)}")
# print(f"字典转列表的结果是:{list(my_dict)}")

# 类型转换：容器转元组
# print(f"列表转元组的结果是:{tuple(my_list)}")
# print(f"元组转元组的结果是:{tuple(my_tuple)}")
# print(f"字符串转元组的结果是:{tuple(my_str)}")
# print(f"集合转元组的结果是:{tuple(my_set)}")
# print(f"字典转元组的结果是:{tuple(my_dict)}")

# 类型转换：容器转字符串
# print(f"列表转字符串的结果是:{str(my_list)}")
# print(f"元组转字符串的结果是:{str(my_tuple)}")
# print(f"字符串转字符串的结果是:{str(my_str)}")
# print(f"集合转字符串的结果是:{str(my_set)}")
# print(f"字典转字符串的结果是:{str(my_dict)}")

# 类型转换：容器转集合
# print(f"列表转集合的结果是:{set(my_list)}")
# print(f"元组转集合的结果是:{set(my_tuple)}")
# print(f"字符串转集合的结果是:{set(my_str)}")
# print(f"集合转集合的结果是:{set(my_set)}")
# print(f"字典转集合的结果是:{set(my_dict)}")
#
# # 进行容器的排序
# # my_list = [3,1,2,5,4]
# my_tuple = (3,1,2,5,4)
# my_str = "abcdefg"
# my_set = {3,1,2,5,4}
# my_dict = {"key3":1,"key1":2,"key2":3,"key5":4,"key4":5}
# print(f"列表对象的排序结果：{sorted(my_list)}")
# print(f"元组对象的排序结果：{sorted(my_tuple)}")
# print(f"字符串对象的排序结果：{sorted(my_str)}")
# print(f"集合对象的排序结果：{sorted(my_set)}")
# print(f"字典对象的排序结果：{sorted(my_dict)}")
#
# print(f"列表对象的反向排序结果：{sorted(my_list,reverse=True)}")
# print(f"元组对象的反向排序结果：{sorted(my_tuple,reverse=True)}")
# print(f"字符串对象的反向排序结果：{sorted(my_str,reverse=True)}")
# print(f"集合对象的反向排序结果：{sorted(my_set,reverse=True)}")
# print(f"字典对象的反向排序结果：{sorted(my_dict,reverse=True)}")

# # 多种传参形式
# def user_info(name,age,gender):
#     print(f"姓名是:{name},年龄是:{age},性别是:{gender}")
# # 位置参数 - 默认形式
# user_info("小明",20,"男")
#
# # 关键字参数
# user_info(name="小王",age=11,gender="女")
# user_info(age=10,name="潇潇",gender="女")
# user_info("天天",gender="男",age=9)
#
# # 缺省参数(默认值)
# def user_info(name,age,gender="男"):
#     print(f"姓名是:{name},年龄是:{age},性别是:{gender}")
#
# user_info('小天',13)
# user_info('小天',13,gender="女")
#
# # 不定长 - 位置不定长, *号
# # 不定长定义的形式参数会作为元组存在，接收不定长数量的参数传入
# def user_info(*a):
#     print(f"a参数的类型是：{type(a)},内容是:{a}")
#
# user_info(1,2,3,"小明","男孩")
#
# # 不定长 - 关键字不定长, **号
# def user_info(**b):
#     print(f"b的类型是：{type(b)},b的内容是：{b}")
#
# user_info(name="小王",age=11,gender="男孩",add="北京")

# # 函数作为参数传入
# # 定义一个函数，接收另一个函数作为传入参数
# def test_func(compute):
#     result = compute(1,2)
#     print(f"compute参数的类型是：{type(compute)}")
#     print(f"计算结果是：{result}")
#
# # 定义一个函数，准备作为参数传入另一个函数
# def compute(x,y):
#     return x+y
# # 调用，并传入参数
# test_func(compute)

# def test_func(compute):
#      result = compute(1,2)
#      print(result)
# # 通过lambda匿名函数的形式，将匿名函数作为参数传入
# test_func(lambda x,y:x+y)

# Python的模块导入
# 使用import导入time模块使用sleep功能
# import time         # 导入python内置的time模块（time.py这个代码文件）
# print("你好")
# time.sleep(5)       # 通过. 就可以使用模块内部的全部功能（类、函数、变量）
# print("我好")

# 使用from导入time的sleep功能
# from time import sleep
# print("你好")
# sleep(5)
# print("我好")

# 使用 * 导入time模块的全部功能
# from time import *         # *表示全部的意思
# print("你好")
# sleep(5)
# print("我好")

# 使用as给特定功能加上别名
# import time as t
# print("你好")
# t.sleep(5)
# print("我好")

# from time import sleep as sl
# print("你好")
# sl(5)
# print("我好")

# 导入自定义模块使用
# import my_modle
# my_modle.test(1,2)
# from my_modle import test
# test(1,2)

# 导入不同模块的同名功能
# __main__变量
# from my_modle import test

# __all__变量
# from my_modle import *
# test_a(1,2)
# test_b(2,1)

# 创建一个包
# 导入自定义的包中的模块，并使用
# import my_package.my_module1
# import my_package.my_module2
#
# my_package.my_module1.info_print1()
# my_package.my_module2.info_print2()

# from my_package import my_module1
# from my_package import my_module2
# my_module1.info_print1()
# my_module2.info_print2()

# from my_package.my_module1 import info_print1
# from my_package.my_module2 import info_print2
# info_print1()
# info_print2()

# 通过__all__变量，控制import *
# from my_package import *
# my_module1.info_print1()
# my_module2.info_print2()

# JSON数据和python字典的相互转换
# import json
# 准备列表，列表内每一个元素都是字典，将其转换为JSON
# data = [{"name":"张大仙","age":11},{"name":"王大锤","age":13},{"name":"赵小虎","age":16}]
# json_str = json.dumps(data,ensure_ascii=False)
# print(type(json_str))
# print(json_str)

# 准备字典，将字典转换为JSON
# d = {"name":"周杰伦","addr":"台北"}
# json_str = json.dumps(d,ensure_ascii=False)
# print(type(json_str))
# print(json_str)

# 将JSON字符串转换为Python数据类型[{k:v,k:v},{k:v,k:v}]
# s = '[{"name": "张大仙", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小虎", "age": 16}]'
# l = json.loads(s)
# print(type(l))
# print(l)

# 将JSON字符串转换为Python数据类型{k:v,k:v}
# s = '{"name":"周杰伦","addr":"台北"}'
# d = json.loads(s)
# print(type(d))
# print(d)

# pyecharts的基础入门
# # 导包
# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts,ToolboxOpts,LegendOpts,VisualMapOpts
# # 创建一个折线图对象
# line = Line()
# # 给折线图对象添加x轴的数据
# line.add_xaxis(["中国","美国","英国"])
# # 给折线图对象添加y轴的数据
# line.add_yaxis("GDP",[30,20,10])
#
# # 设置全局配置项set_global_opts来设置
# line.set_global_opts(
#     title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="1%"),
#     legend_opts=LegendOpts(is_show=True),
#     toolbox_opts=ToolboxOpts(is_show=True),
#     visualmap_opts=VisualMapOpts(is_show=True)
# )
#
# # 通过render方法，将代码生成图像
# line.render()





