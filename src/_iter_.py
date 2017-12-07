#!/usr/bin/python3

import sys

# 迭代器
# 访问集合元素的一种方式
# 　可以记住遍历的位置的对象
# 从集合的第一个元素开始访问，知道所有的元素被访问结束
# 只能往前不能后退
# 列表和元组对象都可用于创建迭代器
mList = [1, 2, 3, 4, 5, 6]
mLt = iter(mList)  # 创建迭代器
print(next(mLt))  # 迭代器的下一个元素


# 可以通过for循环遍历
# for i in mLt:
#     print(i)

# 通过使用next()函数
# while True:
#     try:
#         print(next(mLt))
#     except StopIteration:
#         sys.exit("Sorry,GoodBye!")  # ????


# 生成器
# 使用了yield的函数被称为生成器
# 生成器是一个返回迭代器的函数，只能用于迭代操作，生成器就是一个迭代器
# 在调用生成器运行的过程中，每次遇到yield时，函数会暂停并保存当前所有运行信息，返回yield值，并在下一次next()方法时，从当前位置继续进行
# 斐波那契函数：
def fibonacci(n):
    a, b, c = 0, 1, 0
    while True:
        if (c > n):
            return
        yield a             # 去掉此行，报错????
        a, b = b, a + b
        c += 1


f = fibonacci(20)

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
