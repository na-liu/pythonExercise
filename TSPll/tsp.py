# -*- coding: utf-8 -*-
"""
注意：
解环
print(list(set(father).difference(set(m)))) # 求差集，set自动顺序
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
import heapq

# ----------------------------初始化定义变量-------------------------
population_size = 100  # 种群规模
gene_length = 48  # 基因长度，城市个数
pc = 0.6  # 交叉概率
pm = 0.01  # 变异概率
# t = 0  # 进化代数
T = 100  # 迭代次数


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
        # print('文件数据个数：', len(data))
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
    # print('距离矩阵:\n', distance)
    return distance


# ------初始化种群;input:种群规模，gene个数，output:初始种群-----------
# population_size, gene_length
def init_generation():
    gene = []  # 0 - 47
    for i in range(gene_length):
        gene.append(i)
    next_generation = []
    print(gene)
    for i in range(population_size):
        np.random.shuffle(gene)
        # print(i, gene)
        next_generation.append(gene.copy())
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
    # print('该条路径总距离：', path_cost)
    return path_cost


# -------------------------种群的适应度矩阵--------------------------
def adaption(generation):
    dist = []  # 每一个个体的距离矩阵
    fit = []  # 个体的适应度值
    proportion = []  # 个体适应度值占比
    for i in range(len(generation)):  # 当前种群的长度
        fit.append(1 / total_cost(generation[i]))  # 计算个体的适应度值，距离的倒数
        dist.append(total_cost(generation[i]))
    for i in range(len(generation)):
        proportion.append(fit[i] / sum(fit))
    print('\nfit:\n', fit, '\npro:\n', proportion)
    return fit, proportion, dist


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


# -----------------------------交叉处理->返回子代个体-----------------------------------
def deal(gene_array, cut_array, first):
    ret_list = []  # 父代除去cut的gene位
    for item in gene_array:
        if item not in cut_array:
            ret_list.append(item)
    # print('父代删除cut之后：', ret_list)
    return ret_list[:first] + cut_array + ret_list[first:]


# ------------------------------------顺序交叉-------------------------------------------
def crossover(father, mother):
    a = random.randint(0, gene_length - 1)  # 随机找两个交叉点
    b = random.randint(0, gene_length - 1)
    first = min(a, b)
    second = max(a, b)
    # print(first, second)
    f_cut = father[first:second]
    m_cut = mother[first:second]
    ch1 = deal(father, m_cut, first)
    ch2 = deal(mother, f_cut, first)
    return ch1, ch2


# -----------------------------------对换变异-------------------------------------------
def mutation(individual):
    a = random.randint(0, len(individual) - 1)  # 随机找两个位置
    b = random.randint(0, len(individual) - 1)
    tmp = individual[a]
    individual[a] = individual[b]
    individual[b] = tmp
    return individual


# -------------------------------进化，精英保留--------------------------------
def evoltution(generation):
    # 1. 交叉
    offspring1 = []  # 交叉产生的后代
    j = 0
    for i in range(int(population_size / 2)):
        rand = random.uniform(0, 1)
        father = generation[j]
        mother = generation[j + 1]
        if rand <= pc:
            child1, child2 = crossover(father, mother)
            offspring1.append(child1)
            offspring1.append(child2)
        else:
            offspring1.append(father)
            offspring1.append(mother)
        j += 2
    offspring2 = []

    # 2. 变异
    for item in range(population_size):
        rand = random.uniform(0, 1)  # 生成[0,1]随机数
        if rand <= pm:
            offspring2.append(mutation(offspring1[i]))

    # 3. 选择
    next_generation = []
    the_generation = generation + offspring2  # 当前的父代和子代
    fit, proportion, dist = adaption(the_generation)
    re = list(map(fit.index, heapq.nlargest(1, fit)))  # 选出最大的一个
    print('re:', re[0])
    print('最好的：', dist[re[0]])
    # next_generation.append()

    select_no = roulette(proportion, population_size - 1)
    for i in range(len(select_no)):
        next_generation.append(the_generation[select_no[i]])
    return next_generation


# -------------------------------主函数------------------------------
if __name__ == '__main__':
    dist_array = city_distance("./data/gr48.txt")  # 各个城市距离矩阵
    generation = init_generation()  # 初始化种群
    for i in range(T):
        evoltution(generation)  # 种群进化
    print(generation)

# crossover([2, 1, 3, 4, 5, 6, 7], [4, 3, 1, 2, 5, 7, 6])
# print(mutation([1, 2, 3, 4, 5, 6, 7]))
# 测试 adaption
# adaption([[0, 1, 2], [0, 1, 3], [0, 3, 2], [3, 1, 2]])
