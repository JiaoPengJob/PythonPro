#!/usr/bin/python3

# 数据结构

# 列表
mList = [1, 2, 3, 4, 5, 6]

# 把一个元素添加到列表的末尾，相当于mList[len(mList):] = [x]
mList.append(7)

# 通过添加指定列表的所有元素来扩充列表，相当于mList[len(mList):] = newList
mList.extend([8, 9])

# 在指定位置插入一个元素，第一个参数是准备插入到其前面的那个元素的索引,即想在指定位置添加元素
mList.insert(4, 22)

# 删除列表中值为参数的第一个元素，如果没有这个元素，会返回一个错误
mList.remove(22)

# 从列表的指定位置删除元素，并将其返回，如果没有指定索引，会返回最后一个元素，元素随机在列表中被删除
mList.pop(8)

# 移除列表所有项
mList.clear()

mList = [1, 2, 3, 4]

# 返回列表中第一个值为参数的元素的索引，如果没有匹配项就会返回一个错误
mList.index(3)

# 返回参数在列表中出现的次数
mList.count(1)

# 对列表中的元素进行排序,正序排序
mList.extend([9, 8, 6, 7, 5, 10])
mList.sort()

# 倒排列表中的元素,倒序排序
mList.reverse()

# 返回列表的浅复制
mList.copy()

# 将列表当做堆栈使用
# 列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放，后进先出
mList.append(11)
mList.pop()

# 将列表当做队列使用
# 在队列里第一加入的元素，第一个取出来，拿列表用作这样的目的效率并不高
# 在列表的最后或者弹出元素速度快，然而在列表里插入或者从头部弹出的速度并不快

# ？？？？
# 列表推导式
# 提供了从序列创建列表的简单途径，通常应用程序将一些操作作用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列
# 每个列表推导式都在for之后跟一个表达式，然后有0到多个for或者if子句，返回结果是一个根据表达从其后的for和if上下文环境中生成出来的列表
# 如果希望表达式推导出一个元组，就必须使用()
# 下面是将列表中每个值乘以4
vec = [2, 4, 6]
newVec = [4 * x for x in vec]
print(newVec)

# 还可以使用if作为过滤器
nextVec = [[x, x ** 2] for x in vec if x > 2]
print(nextVec)

# 其他使用
# 将两个列表中的每个数值相乘
print([x * y for x in newVec for y in nextVec])
# 也可以使用复杂表达式或嵌套函数
print([str(round(366 / 114, i)) for i in range(2, 6)])

# 嵌套列表解析
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

# 以上为4X3列表，转换为3X4列表
print([[row[i] for row in matrix] for i in range(3)])

# del 可以从一个列表中依索引而不是值来删除一个元素
# 这与pop() 返回一个值不同
# 可以从列表中删除一个切割，或清空整个列表
del mList[:]

mDic = {"1": 1, "2": 2}

# 字典遍历技巧,遍历key和值
for x, y in mDic.items():
    print(x, y)

# 同时遍历两个或多个序列，可以使用zip() 组合
question = [1, 2, 3, 4]
ans = [5, 6, 7, 8]
for x, y in zip(question, ans):
    print(x, y)

print(mList)


def fun():
    print("我是不是被调用了...")
