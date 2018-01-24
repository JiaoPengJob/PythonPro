#!usr/bin/python3

# 线程

import _thread


def show(name, index):
    num = 100
    while num > 0:
        print(name, index, num)
        num -= 1


try:
    _thread.start_new_thread(show, ('123', 100,))
    _thread.start_new_thread(show, ('321', 100,))
except:
    print('无法启动')

while 1:
    pass
