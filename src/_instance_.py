#!/usr/bin/python3

# 实例代码

# Hello World 实例
print("Hello World!")


# 数字求和
def _filter_numbers():
    str1 = input("输入第一个数字：\n")
    str2 = input("输入第二个数字：\n")
    try:
        num1 = float(str1)
        try:
            num2 = float(str2)
            sum = num1 + num2
            print("相加的结果为：%f" % sum)
        except ValueError:
            print("请输入数字!")
            _filter_numbers()
    except ValueError:
        print("请输入数字!")
        _filter_numbers()


# 判断奇偶数

# 0：偶数
# 1：奇数
def _odd_even(num):
    if num.isdigit():
        if (float(num) % 2) == 0:
            return 0
        else:
            return 1
    else:
        print("这不是一个数字！")


num = input("奇偶--请输入一个数字：\n")
print(_odd_even(num))


# 判断闰年
# 如果一年是闰年，它要么能被4整除但不能被100整除;要么就能被400整除

# True：是闰年
# False：是平年
def _leap_year(year):
    if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
        return True
    else:
        return False


year = input("闰年--请输入一个年份：\n")
print(_leap_year(int(year)))

# 判断质数
# 一个大于1的自然数，除了1和它本身外，不能被其他自然数（质数）整除（2, 3, 5, 7等），换句话说就是该数除了1和它本身以外不再有其他的因数。
import math


# 0：既不是质数，也不是合数
# 1：是质数
# 2：是合数
def _prime(num):
    if num > 1:
        square_num = math.floor(num ** 0.5)
        for i in range(2, (square_num + 1)):
            if (num % i) == 0:
                return 2
                break
            else:
                return 1
    else:
        return 0


num = int(input("质数--输入一个数字:\n"))
print(_prime(num))


# 阶乘
# 整数的阶乘（英语：factorial）是所有小于及等于该数的正整数的积，0的阶乘为1。即：n!=1×2×3×...×n。

def _factorial(num):
    if num < 0:
        # 负数是没有阶乘的
        return num
    else:
        return math.factorial(num)


num = int(input("阶乘--输入一个数字：\n"))
print(_factorial(num))


# 阿姆斯特朗数
# 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。
# 当n=3时，又称水仙花数，特指一种三位数，其各个数之立方和等于该数。

def _armstrong(num):
    sum = 0
    n = len(str(num))
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10
    if num == sum:
        return True
    else:
        return False


print(_armstrong(int(input("阿姆斯特朗--输入一个数字：\n"))))















