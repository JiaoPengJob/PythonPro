#!/usr/bin/python3

import sys

# 异常
# try语句
# 首先执行try子句（在try和except之间的语句）
# 如果没有发生异常，忽略except子句，try子句执行后结束
# 如果发生异常，try子句余下的部分将被忽略，如果异常的类型和except之后的名称相符，那么对应的except子句将被执行，最后执行try语句之后的代码
# 如果一个异常没有与任何的except匹配，那么这个异常将会被传递给上层的try中

# 一个try语句可能会包含多个except子句，分别来处理不同的特定的异常，最多会有一个分支会被执行
# 一个except子句可以同时处理多个异常， 这些异常被放进一个（）中成为一个元组
try:
    print("try语句")
except (RuntimeError, TypeError):
    print("except语句")

# 最后一个except子句可以忽略异常的名称，它将被当做通配符使用
# 使用此方法打印一个错误信息，然后再次把异常抛出
try:
    print("try语句")
except RuntimeError:
    print("except语句")
except TypeError:
    pass
except:
    raise

# 还有一个可选的else子句，必须放在所有的except子句之后，这个子句将在try子句没有发生任何异常的时候执行
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

# 使用else子句比把所有的语句放在try中要好，可以避免一些意想不到的，而except没有捕获的异常
# 还能处理子句中调用的函数的异常（甚至间接调用的函数）

# 使用raise语句抛出一个指定的异常
# raise唯一的一个参数指定了要被抛出的异常，它必须是一个异常的实例或者是一个异常类，
# 如果只是想知道这是否抛出了一个异常，并不想处理它，那么一个简单的raise语句就可以再次把它抛出
# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

# 自定义异常
# 异常应该继承自Exception类，或者直接继承，或者间接继承
# class MyException(Exception):

# 当创建一个模块有可能抛出多种不同的异常时，一种通常的做法是为这个包建立一个基础异常类，然后基于这个基础类为不同的错误创建不同的子类

# 定义清理行为
# 无论在任何情况下都会执行的清理行为
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

# 不管try子句里面有没有发生异常，finally子句都会执行
# 如果一个异常在同try子句中被抛出，而又  没有任何except把它截住，那么这个异常会在finally子句执行后再次被抛出

# 预定义的清理行为
# 一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行
# 关键词with语句可以保证诸如文件之类的对象在使用完成之后一定会正确的执行他的清理方法
