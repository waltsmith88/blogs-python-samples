#_*_  coding: utf-8 _*_
# Author: waltsmith
# Date:2017-12-12


## zip()函数单个参数
print('=*'*10 + "zip()函数单个参数" + '=*'*10)
list1 = [1, 2, 3, 4]
tuple1 = zip(list1)
# 打印zip函数的返回类型
print("zip()函数的返回类型：\n", type(tuple1))
# 将zip对象转化为列表
print("zip对象转化为列表：\n", list(tuple1))


## zip()函数有2个参数
print('=*'*10 + "zip()函数有2个参数" + '=*'*10)
m = [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]]
n = [[2, 2, 2],  [3, 3, 3],  [4, 4, 4]]
p = [[2, 2, 2],  [3, 3, 3]]
# 行与列相同
print("行与列相同:\n", list(zip(m, n)))
# 行与列不同
print("行与列不同:\n", list(zip(m, p)))


## zip()应用，也可以使用for循环+列表推导式实现
# 矩阵相加减、点乘
m = [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]]
n = [[2, 2, 2],  [3, 3, 3],  [4, 4, 4]]
# 矩阵点乘
print('=*'*10 + "矩阵点乘" + '=*'*10)
print([x*y for a, b in zip(m, n) for x, y in zip(a, b)])
# 矩阵相加,相减雷同
print('=*'*10 + "矩阵相加,相减" + '=*'*10)
print([x+y for a, b in zip(m, n) for x, y in zip(a, b)])



## *zip()函数
print('=*'*10 + "*zip()函数" + '=*'*10)
m = [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]]
n = [[2, 2, 2],  [3, 3, 3],  [4, 4, 4]]
print("*zip(m, n)返回:\n", *zip(m, n))
m2, n2 = zip(*zip(m, n))
print(m == list(m2) and n == list(n2))


