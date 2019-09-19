# 集合创建：set() 或{1，2，3}
# 无序不重复
a = set("abcd1eee2")  # 无序的，每次run都不一样
print(a)  # {'1', 'b', 'd', 'c', 'e', '2', 'a'}
b = {1, 2, 3, 's', 4, 'sd'}
print(b)  # {1, 2, 3, 4, 'sd', 's'}
del a, b

# 集合的交并补
a = {1, 2, 3, 4}
b = {1, 2, 5}
print('a,b差集1：', a - b)
print('a,b差集2：', a.difference(b))

print('a,b并集1：', a | b)
print('a,b并集2：', a.union(b))

print('a,b交集1：', a & b)
print('a,b交集2：', a.intersection(b))

print('并集-交集：', a ^ b)
a.difference_update(b)  # 去除与b交集部分之后的a集合,b不变

print('去除与b交集部分之后的a集合：', a)
# 添加元素
a.add(10)
print(a)
a.update({11: 11, 12: 14})  # 参数可以是tuple、list、dict
print(a)

# 删除元素
a.remove(12)  # 移除set中的元素
a.discard(11)  # 移除指定元素，同上
a.pop()  # 随机移除
print(a)
# len(a),a.clear(),x in a,copy(),

# 判断是都有交集
print('是否有交集？', a.isdisjoint(b))

c = {4, 5, 6}
d = {4}
print('a是否是b的子集？', c.issubset(d), 'a是否是b的父集', c.issuperset(d))
