#!/usr/bin/python3


# 函数
# 组织好的，可重复使用的，用来实现单一，或相关功能的代码段
# 提高应用的模块性，和代码复用率
# 自己创建的函数，叫做用户自定义函数

# 定义一个函数
# 规则：
# 函数代码块以def关键词开头，后接函数标识符名称和圆括号()
# 任何传入参数和自变量必须放在圆括号中间，圆括号之间用于定义参数
# 函数的第一行语句可以选择性的使用文档字符串用于存放函数说明
# 函数内容以冒号起始，并且缩进
# return [表达式] 结束函数，选择性返回一个值给调用方，不带表达式的return相当于返回None
# 格式如下：
# def 函数名 (参数列表):
#     函数体

# 默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配的

# 函数调用
# 直接调用

# 可更改（mutable）与不可更改（immutable）对象参数
# 不可变类型
# 值传递，传递的只是参数的值，没有影响参数本身
# 可变类型
# 引用传递，将参数真正的传过去，修改后外部的参数变量也会受到影响

# 传不可变参数，同Java
def changeInt(a):
    a = 10


b = 2
changeInt(b)
print(b)


# 传可变参数，原始参数也会改变

# 必需参数
# 以正确的顺序传入函数，调用时的数量必需和声明时一样

# 关键字参数
# 允许函数调用时参数的顺序和声明时不一致，以为Python解释器能够用参数名匹配参数值
# 参数可以指定进行赋值，不需要按顺序
def printinfo(namer, age):
    print(namer, age)
    return


printinfo(age=2, namer="小明")


# 默认参数
def testinfo(param=2):
    print("默认参数", param)


testinfo()


# 不定长参数
# 一个函数处理比当时声明时更多的参数
# 在声明时不会命名
# 加了 * 号的变量名会存放所有未命名的变量参数，如果在函数调用时没有指定参数，他就是一个空元组
# 我们也可以不向函数传递未命名的变量
# * 参数是一个元组，应该遍历获取
def printSome(stringInfo, *numbers):
    print(stringInfo, numbers)


printSome("123", 456)

# 匿名函数
# 用lambda创建匿名函数
# 意即不再使用def语句的标准形式定义一个函数
# lambda只是一个表达式，函数体比def简单很多
# 主体是一个表达式，而不是一个代码块，仅仅能在表达式中封装有限的逻辑进去
# 拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间的参数
# 也可以使用关键字参数传参
# 也可以设定默认值
# ？？？？
# 虽然看起来只能写一行，却不等同于内联函数
# 如下：
sum = lambda a, b: a + b

print(sum(10, 20))

# return 语句，同Java
# 用一个变量接收这个函数，可以得到return的值

# 变量作用域
# 变量的访问权限决定于这个变量实在哪里赋值的
# 变量的作用域决定了在哪一部分程序的可以访问哪个特定的变量
# L（Local）局部作用域 > E（Enclosing）闭包函数外的函数中 >
# G（Global）全局作用域 > B（Built）内建作用域
# Python中只有模块，类，以及函数才会引入新的作用域
# 其他代码块：if，try，while，for是不会引入新的作用域的，这些语句内定义的变量，外部也是可以访问的
if True:
    abc = "abc"

print(abc)

# global 和 nonlocal关键字
# 当内部作用域想修改外部作用作用域的变量时使用
num = 2


def changeNum():
    global num  # 指明是全局的变量
    print(num)
    num = 4
    print(num)


changeNum()
print(num)


# 修改嵌套作用域，外层非全局作用域，使用nonlocal关键字
def testNumb():
    numb = "22"
    print(numb)

    def inner():
        nonlocal numb
        numb = "44"
        print(numb)

    inner()
    print(numb)


testNumb()
