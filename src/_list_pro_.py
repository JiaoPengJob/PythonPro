#!/usr/bin/python3
# 列表 （序列）

mList = [1, 2, 3, 4, 5, 6, 7, 8]
# 可以通过下标索引访问列表中的值，或使用[:]截取字符
# 更新列表
mList[2] = 8

# 可以通过del语句删除列表的元素
del mList[2]

# + 用于组合列表 * 重复列表
# 可以使用嵌套列表
print([[1, 2], ["a", "b"]])

# 函数
# len(list) 列表元素数量
# max(list) 返回列表元素最大值
# min(list) 返回列表元素最小值
# list(seq) 将元祖转换为列表

# 方法
# list.append(obj) 在列表末尾添加新的对象
# list.count(obj) 统计某个元素在列表中出现的次数
# list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值
# list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
# list.insert(index, obj) 将对象插入列表 index，需要插入的索引位置
# list.pop(obj=list[-1]) 移除列表中的一个元素，默认为最后一个元素，并且返回该元素的值
# list.remove(obj) 移除列表中某个值的第一个匹配项
# list.reverse() 反向列表中的元素
# list.sort([func]) 对原列表进行排序
# list.clear() 清空列表
# list.copy() 复制列表
