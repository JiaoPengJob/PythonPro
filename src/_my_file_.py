#!/usr/bin/python3

# 文件
# file对象使用open() 函数创建,返回一个file对象
# 第一个参数是要访问的文件名称的字符串值
# 第二个参数是打开文件的模式：只读，写入，追加等，默认文件访问模式为只读
"""
模式：
r       以只读方式打开文件，文件指针放在文件的开头，默认模式
rb      以二进制格式打开一个文件用于只读，文件指针将会放在文件的开头，默认模式？？？？
r+      打开一个文件用于读写，文件指针放在文件开头
rb+     以二进制格式打开一个文件用于读写，文件指针在文件开头
w       打开一个文件只用于写入，如果该文件存在，则将其覆盖，如果该文件不存在，创建新文件
wb      以二进制格式打开一个文件只用于写入，如果该文件存在则覆盖，不存在创建新文件
w+      打开一个文件用于读写，该文件存在则覆盖，不存在创建新文件
wb+     以二进制格式打开一个文件用于读写，存在则覆盖，不存在创建新文件
a       打开一个文件用于追加，存在：文件指针将在文件末尾，新的内容将会被写入到已有内容之后，不存在创建新的文件进行写入
ab      以二进制格式打开一个文件用于追加，文件存在指针在文件末尾，新的内容写入到已有内容之后，文件不存在创建新文件进行写入
a+      打开一个文件用于读写，文件存在，指针在文件末尾，文件打开时会是追加模式，文件不存在，创建文件用于读写
ab+     以二进制格式打开一个文件用于追加，文件存在指针在末尾，不存在创建新文件用于读写
"""
# close() 关闭文件
mFile = open("../files/testA.txt", "w")
mFileContent = "这是由File写入的内容\n"
mFile.write(mFileContent)
mFile.close()

# read(size)
# 读取一个文件的内容，size是一个可选的数字类型的参数，size被忽略或者为负，所有内容都将被读取并返回
mFile = open("../files/testA.txt", "r")
mContent = mFile.read()
print(mContent)
mFile.close()

# ？？？？
# 出现乱码问题

# 从文件读取单独一行，换行符为\n，如果返回一个空字符串，说明已经读取到最后一行
mFile = open("../files/testA.txt", "r")
mContent = mFile.readline()
print(mContent)
mFile.close()

# 返回文件中所有行
# 如果设置参数，则读取指定长度的字节，并将这些字节按行分割
mFile = open("../files/testA.txt", "r")
mContent = mFile.readlines()
print(mContent, "\n")
mFile.close()

# 可以迭代一个文件进行输出
# 同上面的处理机制不同，最好不要混用
mFile = open("../files/testA.txt", "r")
for line in mFile:
    print(line)
mFile.close()

# 返回文件当前所处的位置，从文件开头开始算起的字节数
# file.tell()

# ？？？？
# 改变文件的当前所处的位置
# seek(x, 0)    从文件首行首字符开始移动x字符
# seek(x, 1)    表示从当前位置往后移x个字符
# seek(-x, 2)   表示从文件的结尾往前移动x个字符
mFile = open("../files/testB.txt", "rb+")
newContent = b"1234567890abc"
mFile.write(newContent)
mFile.seek(5)
mFile.read()
mFile.close()


