# todo append remove
# 列表表示
list1 = ['Google', 'Runoob', 1997, 200, 1997]
list2 = [1, 2, 3, 4, 5, 6, 7]
# 列表截取
print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])
# 更新列表
list1[0] = 'Baidu'
print(list1)
# 删除元素
del list1[1]
print(list1)

# 脚本操作符
print(len([1, 2, 3]))  # 长度
print([1, 2, 3] + [4, 5, 6])  # 拼接
print([1, 2] * 4)  # 复制
print(3 in [1, 2, 3])  # 判断属于 in
for x in [1, 2, 3]:
    print(x, end=" ")  # 遍历

# 嵌套列表
list3 = [[1, 2, 3], [3, 4, 5]]
print(list3)
print(list3[0][2])

# 列表函数 len max min list(tuple)
# 将tuple转为list，tuple不能更改
tup = (1, 2, 3, 4)
print(tup, list(tup))

# 方法
list1.append('sjsj')  # append(obj)
print(list1)
list1.pop(0)  # pop(index)
print('pop0:',list1)
print('1997出现的次数：', list1.count(1997))  # count(obj)
print('obj的位置：', list1.index(1997))
list1.insert(1, 'Rachel')  # insert(index,obj)
list2 = list1.copy()
print('copy list1:', list2)
list2.clear()  # 清空列表

# list.sort( key=None, reverse=False)
list1 = ['aa', 'Rachel']
list1.sort()  # list中元素排序,纯数字或纯字符串可以
print('sort', list1)
list1.reverse()  # 反向list中的元素
print('reverse', list1)
list1.remove('aa')  # 移除obj的第一个匹配项
print('remove aa', list1)

