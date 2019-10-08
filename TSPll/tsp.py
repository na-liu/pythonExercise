# -*- coding: utf-8 -*-
"""
注意：
解环

题目：
TSP旅行商问题
n个城市，用1-n的整数编码，city = [1,2 3,...,n\n = N+]

解决：
遗传算法
    1. 初始化种群。采用整数编码，一个个体描述一条可行的路线
    2. 适应度函数就是每一条路径的距离，现在的目标是该值越小越好
"""
import numpy as np
import random

# ----------------------------初始化定义变量-------------------------
population_size = 100  # 种群规模
pc = 0.6  # 交叉概率
pm = 0.01  # 变异概率
gene_length = 48  # 基因长度，城市个数
t = 0  # 进化代数


# --------------------------城市距离矩阵-----------------------------
def city_distance(file_path):
    """
    函数名：city_distance()
    函数功能：	从gr48中读取各个城市之间的距离矩阵
        输入	文件路径---gr48
        输出	distance：城市间距离矩阵
    """
    distance = np.zeros((gene_length, gene_length))
    with open(file_path) as file:
        data = np.array(file.read().split())
        count = 0
        print('文件数据个数：', len(data))
        for i in range(gene_length):
            for j in range(gene_length):
                if data[count] == '0':
                    distance[i, j] = data[count]
                    count += 1
                    break
                else:
                    distance[i, j] = data[count]
                    distance[j, i] = data[count]
                    count += 1
    print('距离矩阵:\n', distance)
    return distance


# ------初始化种群;input:种群规模，gene个数，output:初始种群-----------
def init_generation(population_size, gene_length):
    gene = []  # 0 - 47
    for i in range(gene_length):
        gene.append(i)
    next_generation = []
    for i in range(population_size):
        for j in range(gene_length):
            random.shuffle(gene)
            next_generation.append(gene)
    print('初始化种群：\n', next_generation)
    return next_generation


# -----------------适应度函数：由个体求出总路径长度------------------
def total_cost(individual):  # individual:一维数组，表示一条路径
    path_cost = 0
    for i in range(len(individual)):
        if i == len(individual) - 1:
            path_cost += dist_array[individual[0], individual[i]]
        else:
            path_cost += dist_array[individual[i], individual[i + 1]]
    print('该条路径总距离：', path_cost)
    return path_cost


# -------------------------种群的适应度矩阵--------------------------
def adaption(generation):
    fit = []  # 个体的适应度值
    proportion = []  # 个体适应度值占比
    for i in range(len(generation)):  # 当前种群的长度
        fit.append(total_cost(generation[i]))  # 计算个体的适应度值
    for i in range(len(generation)):
        proportion.append(fit[i] / sum(fit))
    return fit, proportion


# -------轮盘赌选择m个算法[input:适应度比例，要选择的个数，output:所选择的个体编号]-------
def roulette(proportion, count):
    q = []  # 累计适应度
    rand = []  # N个随机数
    select = []  # 最终选出来的个体编号
    for i in range(count):
        q.append(proportion[i] + sum(proportion[:i]))
        rand.append(random.uniform(0, 1))  # 生成N个[0,1]随机数
    for i in range(count):
        for j in range(len(q)):
            if rand[i] <= q[j]:
                select.append(j)
                break
    return select


# crossover
# mutation
# selection
# -------------------------------进化--------------------------------
def evoltution(generation):
    return 0


# -------------------------------主函数------------------------------
if __name__ == '__main__':
    dist_array = city_distance("./data/gr48.txt")  # 各个城市距离矩阵
    next_generation = init_generation(population_size, gene_length)  # 初始化种群
    evoltution(next_generation)  # 种群进化
