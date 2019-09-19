# 字典 key:value
# key是唯一的
d = {'Tom': 12, 'Lisa': 10, 'Rachel': 22}
print("d['Tom']:", d['Tom'])  # 访问key对应的value

# get方法，获取指定key下的value，如果不存在当前的key,就用默认值创建一个新的键值对
print('d.get:', d.get('Bob', 23), d.get('Tom', 12))
# 修改字典
d['Rachel'] = 16  # 更新value
d['Bob'] = 24  # 添加元素
print(d)

# 删除字典元素
del d['Bob']  # 删除key'Bob'
d.clear()  # 清空
del d  # 删除字典

# fromkeys()创建新字典,不好用呀，只能一个值？
seq = ('Name', 'Age', 'Address')
# d = dict.fromkeys(seq, 'Rachel', 22, 'Shanxi')
d = dict.fromkeys(seq, 'Rachel')  # 参数2不赋值，默认是none
print('新的字典为：%s' % str(d))
