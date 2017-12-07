#!/usr/bin/python3
# 字典
# 即键值对集合
# 格式如下
mDict = {"a": 1, "b": 2}

# 键必须是唯一的，值不用
# 键不可改变数据类型，必须统一
# 访问字典中的值
# 把相应的值放入方括弧
print(mDict["a"])

# 添加新值
mDict["c"] = 3

# 修改值
mDict["b"] = 4

# 删除字典元素
# 可以删除单一的元素，也可以清空,也可以删除字典，即del 字典
del mDict["b"]
mDict.clear()
del mDict

# 字典键的特性
# 不允许同一个键出现两次，如果同一个键被赋值两次，后一个会被记住
# 键必须不可变，所以不能使用列表

# 内置函数和方法
# str(dict) 输出字典
# type(variable) 返回输入的变量类型
# radiansdict.copy() 返回一个字典的浅复制
# radiansdict.fromkeys(seq[, value])) 创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的值
# radiansdict.get(key, default=None) 返回指定建的值，如果值不在字典中返回default值
# key in dict 如果键在字典中，返回True
# radiansdict.items() 以列表返回可遍历的元组数组
# radiansdict.keys() 以列表返回一个字典所有的键
# radiansdict.setdefault(key, default=None) 如果键不存在字典中，将会添加键并赋值为default
# radiansdict.update(dict2) 将参数字典的键值对更新到前者中
# radiansdict.values() 以列表返回字典中的所有值
# pop(key[,default]) 删除字典给定key所对应的值，返回被删除的值，key值必须给出，否则返回default值
# popitem() 随机返回并删除字典中的一对键值，一般删除末尾对
mDic = {"a": 1, "b": 2}
newDic = mDic.copy()
mDic["c"] = 3
print(newDic)



















