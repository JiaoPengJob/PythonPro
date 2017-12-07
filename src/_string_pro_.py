#!/usr/bin/python3
# 字符串

mStr = "这是一个测试用的字符串"
# Python不支持单字符类型，单字符也是作为一个字符串使用
# 使用[]来截取字符串
print(mStr[0:3])

# 可以截取字符串之后与另一个字符串拼接
# 在使用特殊字符时，用反斜杠 \ 转义字符
# \ 在行尾时，续行符
# \\ 反斜杠符号
# \' , \"   单引号和双引号
# \a 响铃 ????
# \b 退格
# \e 转义
# \000 空
# \n 换行
# \v 纵向制表符  ????
# \t 横向制表符
# \r 回车
# \f 换页
# \oyy 八进制数，yy代表的字符 ????
# \xyy 十六进制数，yy代表的字符
# \other 其他字符以普通格式输出


# 字符串格式化
# 将一个值插入到一个有字符串格式符 %s 的字符串中
# %c 格式化字符，及其ASCII码（单个字符）
# %s 格式化字符串
# %d 格式化整数，浮点类型值会向下取整，可以指定位数，例：%02d,如果数值为1，则会打印01
# %u 格式化无符号整型
# %o 格式化无符号八进制数
# %x 格式化无符号十六进制数
# %X 格式化无符号十六进制数（大写）
# %f 格式化浮点数，可指定小数点后的精度，例：%.4f
# %e 用科学计数法格式化浮点数
# %E 同上
# %g %f和%e的简写
# %G %f和%G的简写
# %p 用十六进制数格式化变量的地址
print("名字：%04d" % (1))

# '''...'''三引号，即：所见即所得，用于注释，html，或者js

r"""
# 字符串内建函数
# capitalize() 将字符串的第一个字符转换为大写
# center(width, fillchar) 返回一个指定的宽度width居中的字符串，fillchar为填充的字符，默认为空格
# count(str, beg= 0,end=len(string)) 返回str在beg和end范围中出现的次数
# bytes.decode(encoding="utf-8", errors="strict") 以指定的编码格式解码bytes，默认为utf-8
# 接上：errors：编码错误引起的一个UnicodeError，其他值'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值
# encode(encoding='UTF-8',errors='strict') 字符串编码格式
# endswith(suffix, beg=0, end=len(string)) 检查指定beg到end范围的字符串是否以suffix结束，返回True或者False
# expandtabs(tabsize=8) 将字符串中的tab符号转换为空格，tab默认空格数是8
# find(str, beg=0 end=len(string)) 检测str知否包含在字符串beg到end范围中，如果包含返回开始的索引值，否则返回-1
# index(str, beg=0, end=len(string)) 同上，如果不在字符串中会报异常
# isalnum() 如果字符串至少有一个字符，并且所有字符都是字母或者数字则返回True或False
# isalpha() ......所有字符都是字母则返回True
# isdigit() ......所有字符只包含数字则返回True
# islower() 至少包含一个区分大小写的字符，并且所有这些区分大小写的字符都是小写，返回True
# isnumeric() 只包含数字字符，返回True
# isspace() 只包含空白，放回True
# istitle() 字符串是标题化的返回True
# isupper() 至少包含一个区分大小写的字符，并且所有字符都是大写，返回True
# join(seq) 以指定字符串作为分隔符，将seq中所有元素合并为一个新的字符串
# len(string) 返回字符串长度
# ljust(width[, fillchar]) 返回一个原字符串左对齐，并使用fillchar填充至长度width的新字符串，默认填充空格
# lower() 转换字符串中所有大写字符为小写
# lstrip() 截掉字符串左边的空格或者指定字符
# ????
# maketrans() 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
# translate(table, deletechars="") table 翻译表，用过maketrans()转换得到，deletechars字符中要过滤的字符列表
# max(str) 返回字符串中最大的字母
# min(str) 返回字符串中最小的字母
# replace(old, new [, max]) 将字符串中的old替换成new，替换次数不超过max
# rfind(str, beg=0,end=len(string)) 类似于find()函数，从右边开始
# rindex( str, beg=0, end=len(string)) 类似于index(),从右边开始
# rjust(width,[, fillchar]) 返回一个原字符串右对齐，并使用fillchar填充至长度为width的新字符串
# rstrip() 删除字符串末尾的空格
# split(str="", num=string.count(str)) str为分隔符，num为分割次数
# splitlines([keepends]) 按照行分割，即\r,\r\n,\n，返回一个包含各行作为元素的列表，keepends为False，不包含换行符，True保留换行符
# startswith(str, beg=0,end=len(string)) 检查指定范围字符串是否以str开始，返回True或False，
# strip([chars]) 删除字符串开始和末尾的空格
# swapcase() 将字符串大写转换为小写，将小写转换为大写
# title() 所有单词以大写开始，其余字母均为小写
# upper() 转换小写字母为大写
# zfill (width) 返回长度为width的字符串，右对齐，前面用0填充
# isdecimal() 检查字符串是否只包含十进制字符，返回True或False

"""
print("123123123".split("3", 2))
