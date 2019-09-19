# tuple 表示
tup = ()  # 空元组
tup1 = (1, 2, 3, 4)
tup2 = (1)  # 括号中是单个元素时，括号会被认为是运算符号，表示整型
print('type(tup1):', type(tup1))  # type(tup1): <class 'tuple'>
print('type(tup2):', type(tup2))  # type(tup1): <class 'int'>

# 访问元组
print('tup1[0]:', tup1[0])  # tup1[0]: 1
print('tup1[-1]:', tup1[-1])  # tup1[-1]: 4
print('tup1[1:3]', tup1[1:3])  # tup1[1:3] (2, 3)

# 修改元组，非法
# tup1[0] = 8 # 会提示你将tuple转化为list

# 删除元组
del tup1
# print(tup1)  # name 'tup1' is not defined
del tup
tup = (1, 2, 3, 4, 5, 6, 7, 8)
# 运算符
print('长度：', len(tup))  # 8
print('拼接：', tup + (1, 2, 3))  # 拼接： (1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3)
print('复制：', ('hi',) * 2)
print('存在检验：', 'a' in ('a', 'b', 'c'))
# 迭代
for x in (1, 2, 3):
    print(x, end='')

# max min len tuple(list):将tuple转化为list
