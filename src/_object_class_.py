#!/usr/bin/python3

# 类
# 面向对象

# 类
# 用来描述具有相同的属性和方法的对象的集合，定义了该集合中每个对象所共有的属性和方法，对象是类的实例

# 类变量
# 在整个实例化的对象中是公用的，类变量定义在类中且在函数体之外，类变量通常不作为实例变量使用

# 数据成员
# 类变量或者实例变量用于处理类及其实例对象的相关的数据

# 方法重写
# 如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖，也称为方法的重写

# 实例变量
# 定义在方法中的变量，只作用于当前实例的类

# 继承
# 即一个派生类继承基类的字段和方法，继承也允许把一个派生类的对象作为一个基类对象对待

# 实例化
# 创建一个类的实例，类的具体对象

# 方法
# 类中定义的函数

# 对象
# 通过类定义的数据结构实例，对象包括两个数据成员（类变量和实例变量）和方法

# 对象可以包含任意数量和类型的数据

# 类定义
class A:

    def showText(self):
        print("这是类里面的方法的输出")

    pass


# 类对象
# 支持两种操作：属性引用和实例化
# 属性引用使用和其他所有的属性引用一样的标准语法：obg.name
# 类对象创建后，类命名空间中所有的命名都是有效属性名

a = A()
a.showText()


# 很多类都倾向于将对象创建为有初始状态的，因此类可能会定义一个名为__init__()的特殊方法（构造方法）
# 类如果定义了init方法后，类的实例化操作会自动调用init方法
# init方法可以有参数，参数通过init传递到类的实例化操作中
# init函数中的self代表类的实例，而非类
# 类的方法与普通的函数只有一个特别的区别，他们必须有一个额外的第一个参数名称，按照惯例它的名称是self
# self 不是关键字，可以把它换成runoob也是可以正常执行的
class B:

    def __init__(self, text, index):
        self.textStr = text
        self.indexStr = index
        print(self.__class__)

    def __show_info__(runoob):
        runoob.first = "123456"
        print(runoob.first)


b = B("参数", 6666)
print(b.textStr)
print(b.indexStr)
b.__show_info__()


# 类的方法
# 在类的内部，使用def关键字来定义一个方法，与一般的函数定义不同，类方法必须包含参数self，且为第一个参数，self代表的是类的实例

# 继承
# 多继承
class C(A, B):
    pass


# 注意括号中基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，将从左往右搜索，即方法在子类中未找到时，从左往右查找基类中是否包含方法
# 基类必须与派生类定义在一个作用域中，除了类，还可以用表达式，基类定义在另一个模块中时，这点很重要
# 例如：
# class DerivedClassName(modname.BaseClassName):

# 如果你的父类方法的功能不能满足你的需求，你可以在子类中重写你父类的方法
class D:
    def my_method(self):
        print("调用父类的方法")


class E(D):
    def my_method(self):
        print("调用子类的方法")


e = E
e.my_method(D)

# 类属性与方法
# 类的私有属性
# 两个下划线开头，声明该属性为私有，不能在类的外部被使用或者直接访问，在类内部的方法中使用时，需要self.调用
# self名字不是规定死的，也可以使用this，最好使用按照约定的self

# 类的专有方法
# __init__      构造函数，在生成对象时调用
# __del__       析构函数，释放对象时使用
# __repr__      打印，转换
# __setitem__   按照索引赋值
# __getitem__   按照索引获取值
# __len__       获得长度
# __cmp__       比较运算
# __call__      函数调用
# __add__       加运算
# __sub__       减运算
# __mul__       乘运算
# __div__       除运算
# __mod__       求余运算
# __pow__       乘方














