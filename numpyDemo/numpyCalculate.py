import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[6, 7], [8, 3]])
print(a + b)
print(np.add(a, b))
# array([[ 7,  9],
#        [11,  7]])
print(a - b)
print(np.subtract(a, b))
# array([[-5, -5],
#        [-5, 1]])
print(a * b)  # 对应元素相乘
print(np.multiply(a, b))
# array([[6, 14],
#        [24, 12]])
print(np.sqrt(a))  # 每一个元素开根号
# array([[1., 1.41421356],
#        [1.73205081, 2.]])
b = np.array([[1, 2, 3], [4, 5, 6]])
print(a.dot(b))  # 矩阵乘积
print(np.dot(a, b))
# array([[9, 12, 15],
#        [19, 26, 33]])
print(np.sum(a))  # a所有元素之和
# 10
print(np.sum(a, axis=0))  # axis=0表示列向量
print(np.sum(a, axis=1))  # axis=1表示行向量
print(np.mean(a))  # a中所有元素的均值 2.5
print(np.mean(a, axis=0))  # array([2., 3.])
print(np.mean(a, axis=1))  # array([1.5, 3.5])
# 随机数
print(np.random.uniform(3, 4))  # 3.9125705162966047
print(np.random.uniform(1, 100))  # 20.034232701119244
# 重复，参数1表示初始矩阵，参数2表示重复的次数，第一个表示行，第二个表示列
print(np.tile(a, (1, 2)))
# array([[1, 2, 1, 2],
#        [3, 4, 3, 4]])
print(np.tile(a, (2, 2)))
# [[1 2 1 2]
#  [3 4 3 4]
#  [1 2 1 2]
#  [3 4 3 4]]
# 排序，结果表示排序之后的元素索引值
a = np.array([[3, 6, 4, 11], [5, 10, 1, 2]])
print(a.argsort())
# array([[0, 2, 1, 3],
#        [2, 3, 0, 1]], dtype=int64)
a.argsort(axis=0)  # 按列排序
# array([[0, 0, 1, 1],
# [1, 1, 0, 0]], dtype=int64)
# 转置
print(a.T)
# array([[3, 5],
#        [6, 10],
#        [4, 1],
#        [11, 2]])
print(np.transpose(a))  # 同上
# array([[3, 5],
#        [6, 10],
#        [4, 1],
#        [11, 2]])
