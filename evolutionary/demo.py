import numpy as np

gene = []
for i in range(10):
    gene.append(i)
next_generation = []
for i in range(10):
    np.random.shuffle(gene)
    print(i, gene)
    next_generation.append(gene)
    print(next_generation)
print('初始化种群：\n', next_generation)

