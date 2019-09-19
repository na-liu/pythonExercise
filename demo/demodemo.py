# sum()函数接受一个list作为参数，并返回list所有元素之和。请计算 1*1 + 2*2 + 3*3 + ... + 100*100
L = []
for x in range(101):
    L.append(x ** 2)
print(sum(L))
# sum([i*i for i in L]) # get到一种简洁写法


# 一元二次方程求解
from math import *


def quadratic_equation(a, b, c):
    tmp = b * b - 4 * a * c
    x1 = (-b + sqrt(tmp)) / (2 * a)
    x2 = (-b - sqrt(tmp)) / (2 * a)
    return x1, x2


print(quadratic_equation(2, 3, 0))
print(quadratic_equation(1, -6, 5))


# 汉诺塔求解
# -*- coding:utf-8 -*-
# move(n, a, b, c)表示的是有n个盘子在a柱子上，将要移到b柱子上面去
def move(n, a, b, c):
    # 如果a柱子上面只有一个盘子，则直接移到c柱子上面去并输出路径，结束递归
    if n == 1:
        print(a + '-->' + c)
        return
    # 表示的是将n-1的盘子从a柱子上面移到b柱子上面去
    move(n - 1, a, c, b)
    # 输出最下面个盘子移从a移到c的路径
    print(a + '-->' + c)
    # 将b柱子上面的n-1个盘子移动到c柱子上面
    move(n - 1, b, a, c)


move(4, 'A', 'B', 'C')


# 函数默认参数
def greet(a='world'):
    print('hello,', a)


greet()
greet('Bart')


# 可变参数 变量前有*
def average(*args):
    if len(args) is not 0:
        return sum(args) * 1.0/ len(args)
    else:
        return 0.0


print(average())
print(average(1, 2))
print(average(1, 2, 2, 3, 4))
