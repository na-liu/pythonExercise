import numpy as np

a = np.array([[1, 2, 3, 4],
              [2, 3, 4, 5],
              [4, 5, 6, 7],
              [3, 5, 6, 2]])
b = np.array([1, 1, 1, 1])
# a的每一行加b
for i in range(4):
    a[i, :] += b
print(a)
print(np.tile(b, (4, 1)))
# python循环效率很低，可以使用tile函数(将b矩阵复制4行1列)
print(a + np.tile(b, (4, 1)))

# numpy的广播，可以将不同维度的数组相加，自动补充缺失维度
print(a + b)

