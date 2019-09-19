# python3.X 已经不支持operator了,no no no
# 我不知道需要导包
import operator

a = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
b = operator.itemgetter(1)  # 定义函数b，获取对象的第1个域的值
print(b(a))  # 2 
b = operator.itemgetter(1, 0)  # 定义函数b，获取对象的第1个域和第0个的值
print(b(a))  # (2, 1) 


# operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值。

c = {'A': 1, 'B': 4, 'C': 3}
print(sorted(c.items(), key=operator.itemgetter(1)))
# 我已经找到替换的方法：
# key=lambda x: x[1]
# lambda 匿名函数，参数为x，函数体是x[1],应该和上面相同的效果
# 第三个参数，reverse:True为倒序
