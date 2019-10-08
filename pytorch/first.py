import torch
import numpy as np

# 定义一个Tensor矩阵
a = torch.Tensor([[1, 2], [3, 4], [5, 6], [7, 8]])
print(a)

np_data = np.arange(6).reshape((2, 3))
torch_data = torch.from_numpy(np_data)
print('\nnumpy data:', np_data, '\ntorch data:', np_data)

# abs:absolute value
data = [[1, 2], [3, 4]]
tensor = torch.FloatTensor(data)  # 32bit

print(np.matmul(data))
print(torch.mm(tensor))
