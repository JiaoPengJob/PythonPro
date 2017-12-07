#!/usr/bin/python3

# 斐波那契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 100:
    print(b, end=";")
    a, b = b, a + b

# 条件控制
# 格式如下：
if True:
    print("\nif")
elif True:
    print("elif")
else:
    print("else")

# 在Python中没有switch-case语句！！
# if嵌套
# 即可以把if-elif-else嵌套进if-elif-else中

# 循环语句
# 　循环语句有for和while
# while循环
# 一般格式：
# while 判断条件:
#       语句
# while True:
#     print("这是while的语句")

# 在Python中没有do...while循环！！
# 可以使用CTRL + C来退出当前的无限循环
# 无限循环在服务器上客户端的实时请求非常有用

# while ... else 在条件语句为false时执行else的语句块
# while False:
#     print("这是while...else的while")
# else:
#     print("这是while...else的else")

# 简单语句组
# 如果判断体或者循环体中只有一条语句，可以将该语句与前面的写在同一行中
# if True: print("打印测试信息if")
#
# while True: print("打印测试信息while")

# for 语句
# 可以遍历任何序列的项目，如一个列表或者一个字符串
mList = ["1", "a", "2", "b", 3, 4]
for x in mList:
    print(x)
else:
    print("没有循环体")

# for 循环中可以使用break语句，跳出当前循环体
for y in mList:
    if y == "b":
        break
    print(y)
else:
    print("当前没有循环体")

# range()函数
# 可以遍历数字序列，自动生成数列
for i in range(13):
    print(i)
# range()函数参数是一个时，输出0到参数-1的值
# 也可以指定区间，即range(2,8)，输出2到8 - 1范围的值
# 也可以使用range()以指定数字开始，并指定不同的增量，甚至可以是负数，有时也叫作步长
for j in range(0, 22, 2):
    print(j)

# 可以结合range()和len()函数遍历一个序列的索引
for index in range(len(mList)):
    print(index)

# 可以使用range()创建一个列表
list(range(8))

# break,continue语句以及else语句
# break 可以跳出for和while的循环体
# 如果从for或者while循环中终止，任何对应的循环else块将不会执行
# continue语句用来告诉Python跳过当前循环块中剩余语句，继续进行下一轮循环
for letter in "这是一条测试数据":
    if letter == "一":
        continue
    print(letter)

# 循环语句可以有else子句，在穷尽列表（以for循环）或条件变为false（以while循环）导致循环终止时被执行，
# 但循环被break终止时不执行

# pass 语句
# 空语句，不做任何事情，一般用作占位语句，为了保持程序结构的完整性

# 使用内置 enumerate()函数进行遍历
# 会输出脚标和值
for i, j in enumerate(mList):
    print(i, j)

# 循环嵌套实现99乘法法则
i = 1
while i < 10:
    j = 1
    while j <= i:
        mut = j * i
        print("%d*%d=%d" % (j, i, mut), end=" ")
        j += 1
    print("")
    i += 1
