#!/usr/bin/python3

# Pickle 模块
# 实现了基本的序列化和反序列化
# 序列化操作可以保存运行的对象信息到文件中去，永久存储
# 反序列化操作能从文件中创建上一次程序保存的对象
# 基本接口
# pickle.dump(obj, file, [,protocol])

# 对file以读取的形式打开
# 即，从file中读取一个字符串，并将它重构成原来的Python对象
import pickle

mData = {'a': [1, 2.0, 3, 4 + 6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open("../files/testC.txt", 'wb')
pickle.dump(mData, output)
pickle.dump(selfref_list, output, -1)

output.close()

# pickle的load() 使用
loadFile = open("../files/testC.txt", 'rb')
mDatas = pickle.load(loadFile)
print(mDatas)
loadFile.close()

# 测试代码，爬虫
from urllib import request

response = request.urlopen("http://www.runoob.com/python3/python3-inputoutput.html")
fi = open("../files/testWorm.txt", "w")
fi.write(str(response.read()))
fi.close()

fi = open("../files/testWorm.txt", "r")
page = fi.read()
print(page)
fi.close()
