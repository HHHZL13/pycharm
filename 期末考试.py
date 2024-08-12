# # 定义函数
# def extract_max_min(input_tuple, k):
#     # 对输入元组进行排序
#     sorted_tuple = sorted(input_tuple)
#     # 在此处编写你的代码
#     for i in k:
#         if i <=k:
#             a = tuple[0]
#             b = tuple[::-1]
#             c = (a+b)
#     return c
#
# # 获取整数输入并将其转换为元组
# input_tuple = tuple(map(int, input().split()))
# # 获取K的值
# k = int(input())
# # 调用函数
# print(extract_max_min(input_tuple, k))
n = int(input())
for i in range(1,n+1):
    for k in range(1,i+1):
        print("{}*{}={}\t".format(k,i,i*k),end='')
    print('')