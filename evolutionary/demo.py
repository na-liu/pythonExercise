import numpy as np


# 单位向量二进制转十进制
# x = [0, 1, 1, 1, 0, 0, 1, 0]
def vector_change(x):
    y = 0
    for i in range(len(x)):
        y += x[i] * np.power(2, len(x) - i - 1)
    return y


x1_bounder = [-3.0, 12.1]
x2_bounder = [4.1, 5.8]
n_population = 10  # 种群数N
DNA_size = 33  # 染色体长度33位
population = np.random.randint(low=0, high=2, size=(n_population, DNA_size)).astype(np.int8)
for i in range(10):
    print('个体', i, '：', population[i])

x1 = population[:, :18]
x2 = population[:, 18:]
v = []
for i in range(n_population):
    v += [vector_change(x1[i]), vector_change(x2[i])]
    print(v)
