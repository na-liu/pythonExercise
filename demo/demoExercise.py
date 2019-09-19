L = range(1, 101)
print(L)
print(list(L[0:10]))  # 前10个数
print(list(L[2::3]))  # 3的倍数
print(list(L[4:51:5]))  # 50以内5的倍数
del L

# 倒序切片,从前到倒数含头不含尾，从倒数到后全部
L = ['Adam', 'Lisa', 'Bart', 'Paul']
print(L[-2:])  # ['Bart', 'Paul']
print(L[:-2])  # ['Adam', 'Lisa']
print(L[-3:-1])  # ['Lisa', 'Bart']
del L

L = range(1, 101)
print(list(L[-10:]))  # 倒数10个
print(L[4::5][-10:])  # 最后10个5的倍数

# 字符串切片
print('ABCDEFG'[-3:])


# 用切片和upper(),仅首字母大写
def firstCharUpper(s):
    return s[0:1].upper() + s[1:]


print(firstCharUpper('hello'))
print(firstCharUpper('sunday'))
print(firstCharUpper('september'))

# 请用for循环迭代数列 1-100 并打印出7的倍数。
for i in range(1, 101):
    if i % 7 == 0:
        print(i)

# 索引迭代，enumerate（L）,需要得到索引值
# enumerate函数将list中的每一个元素看作一个tuple:(1,'Rachel')
# index = t[0]、name = t[1]
# zip(L1,L2)可以将两个list变成一个
print(list(zip([1, 2, 3], ['a', 'b', 'c'])))  # [(1, 'a'), (2, 'b'), (3, 'c')]
for index, name in enumerate(['a', 'b', 'c']):
    print(str(index) + '-' + name, end="  ")

# 迭代dict中的value
# values():将dict转化为含有values的list
# itervalues():比values()省内存，直接取出values----->python3已删除
d = {'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74}
# print(d.values()) # dict_values([95, 85, 59, 74])
print(1.0 * sum(list(d.values())) / len(d))  # 计算平均值

# items(),字典中的每一个元素
print(d.items())  # dict_items([('Adam', 95), ('Lisa', 85), ('Bart', 59), ('Paul', 74)])
for k, v in d.items():
    print(k, ':', v)  # name:value
print(sum(list(d.values())) / len(d))  # 平均值

# 列表生成式生成列表 [1x2, 3x4, 5x6, 7x8, ..., 99x100]
print([x * (x + 1) for x in range(1, 100, 2)])
d = {'Adam': 95, 'Lisa': 85, 'Bart': 59}


# 列表生成式后可以加条件过滤
def toUppers(L):
    return [u.upper() for u in L if isinstance(u, str)]


print(toUppers(['Hello', 'world', 101]))  # 如果列表中的元素是str，那么将字母大写

# 多层表达式嵌套，找出所有的3位对称数，如121，232
print([100 * x + 10 * y + z for x in range(1, 10) for y in range(10) for z in range(10) if x == z])


# 复杂表达式


def generate_tr(name, score):
    if score < 60:
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)


tds = [generate_tr(name, score) for name, score in d.items()]
print('<table border="1">')
print('<tr><th>Name</th><th>Score</th><tr>')
print('\n'.join(tds))
print('</table>')
