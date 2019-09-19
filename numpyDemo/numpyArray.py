# numpy简单教程
# Array（数组）rank(阶数)
import numpy as np

a = np.array([1, 2, 3])  # numpy创建一个Array
print(type(a))  # 查看一下该数组的类型  <class 'numpy.ndarray'>
print(a.shape)  # 查看数组的长度  # (3,)：一维数组，3个元素，但并未指明是行向量还是列向量

a = a.reshape((1, -1))  # 1表示1行，-1表示按照元素的多少以及明确的行数，计算出应该的列数
print(a.shape)  # (1, 3):表示1行3列

b = np.array([1, 2, 3, 4, 5, 6])
b = b.reshape((2, -1))
print(b)
print(b.shape)  # (2, 3):表示2行3列

# zeros函数、ones函数、full函数、random.random
# a = np.zeros((3, 3))
# a = np.ones((3, 3))
# a = np.full((2, 3), 5)
# a = np.random.random((2, 3))

# 修改某个值
print('修改前：', a)
a[0][0] = 3
print('修改后：', a)

# 索引
a = np.array([[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]])
print('a.shape', a.shape, 'a的行数：', a.shape[0], ' a的列数：', a.shape[1])
b = a[-2:, 1:3]  # 从倒数第二行开始至最后一行，第1行到第2行
print(b, b.shape)
# [[ 6  7]
#  [10 11]]

b = a[2:3, 1:3]  # 是一个范围，选取结果为1×2的矩阵 # (1, 2)
c = a[2, 1:3]  # 第一个参数固定，指代具体一行，所以c表示含有两个元素的向量 # (2,)
print(b.shape, '', c.shape)

# 将a数组第1列每个元素加10,3种写法
print(np.arange(3))  # array([0, 1, 2])
a[np.arange(3), 1] += 10
a[[0, 1, 2], [1, 1, 1]] += 10
a[np.arange(3), [1, 1, 1]] += 10
print(a)

# 获取array中大于10的数
result = a > 10
print(result)
# [[False  True False False]
# [False  True False False]
# [False  True  True  True]]
print(a[result])  # [32 36 40 11 12]
# 或者写成：
print(a[a > 10])

# 查看数据类型
a = np.array([1, 2])
print(a.dtype)  # dtype('int32')
a = np.array([1, 1.1])  # 整数小数同时包含，dtype为小数
print(a.dtype)  # dtype('float64')
a = np.array([2.3, 1.1], dtype=np.int64)  # 指定数据类型，取整
print(a)  # array([2, 1], dtype=int64)
b = np.array(a, dtype=np.int64)  # 用a创建b
print(b)  # array([2, 1], dtype=int64)
