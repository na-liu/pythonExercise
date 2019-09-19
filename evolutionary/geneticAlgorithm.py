from __future__ import division
import numpy as np


# 适应度函数&目标函数
def aim_function(x1, x2):
    y = 21.5 + x1 * np.sin(4 * np.pi * x1) + np.sin(20 * np.pi * x2)
    return y


# 单位向量二进制转十进制
# x = [0, 1, 1, 1, 0, 0, 1, 0]
def vector_change(x):
    y = 0
    for i in range(len(x)):
        y += x[i] * np.power(2, len(x) - i - 1)
    return y


class GeneticAlgorithm(object):
    def __init__(self, cross_rate, mutation_rate, n_population, n_iterations, DNA_size):
        self.cross_rate = cross_rate
        self.mutate_rate = mutation_rate
        self.n_population = n_population  # 种群数N
        self.n_iterations = n_iterations
        self.x1_size = 18
        self.x2_size = 15
        self.DNA_size = self.x1_size + self.x2_size  # DNA的长度
        self.x1_bounder = [-3.0, 12.1]
        self.x2_bounder = [4.1, 5.8]

    # 1.初始化种群10*33
    def init_population(self):
        population = np.random.randint(low=0, high=2, size=(self.n_population, self.DNA_size)).astype(np.int8)
        print('population:')
        print(population)
        return population

    # 解码,二维数组划分：前18位是X1,后15位是X2;将种群中的每个个体的DNA由二进制转换成十进制
    def decode(self, population):
        x1 = population[:, :18]
        x2 = population[:, 18:]
        for i in range(self.n_population):
            x1 = self.x1_bounder[0] + (self.x1_bounder[1] - self.x1_bounder[0]) * vector_change(x1[i]) / (
                    np.power(2, self.x1_size) - 1)
            x2 = self.x2_bounder[0] + (self.x2_bounder[1] - self.x2_bounder[0]) * vector_change(x2[i]) / (
                    np.power(2, self.x2_size) - 1)
        print('x!：', x1)
        print('x2：', x2)
        return x1, x2

    # 2.计算种群中个体的适应度
    def fitness(self, population):
        x1, x2 = self.decode(population)
        fitness_score = aim_function(x1, x2)
        return fitness_score - fitness_score.min()  # 在select函数中按照个体的适应度进行抽样的的时候，抽样概率值必须是非负的

    # 3.轮盘赌选择
    # 4.交叉算子：交叉概率pm
    # 5.变异算子：变异概率pc，防止陷入局部最优

    # 进化
    def evolution(self):
        population = self.init_population()
        fitness_score = self.fitness(population)
        print('fitness_score:', fitness_score)


def main():
    ga = GeneticAlgorithm(cross_rate=0.9, mutation_rate=0.1, n_population=300, n_iterations=2000, DNA_size=8)
    ga.evolution()


if __name__ == '__main__':
    main()
