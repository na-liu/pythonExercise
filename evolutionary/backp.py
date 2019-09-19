import random
import numpy as np

# todo 遗传算法结合贪心算法
# 结果：总价值：3103   总重量1000
C = [220, 208, 198, 192, 180, 180, 165, 162, 160, 158, 155, 130, 125, 122, 120, 118, 115, 110, 105, 101, 100, 100, 98,
     96, 95, 90, 88, 82, 80, 77, 75, 73, 72, 70, 69, 66, 65, 63, 60, 58, 56, 50, 30, 20, 15, 10, 8, 5, 3, 1]  # 物体的价格
W = [80, 82, 85, 70, 72, 70, 66, 50, 55, 25, 50, 55, 40, 48, 50, 32, 22, 60, 30, 32, 40, 38, 35, 32, 25, 28, 30, 22, 50,
     30, 45, 30, 60, 50, 20, 65, 20, 25, 30, 10, 20, 25, 15, 10, 10, 10, 4, 4, 2, 1]  # 物体的重量
N = 50  # 物体总数50;编码长度
V = 1000  # 背包总重量
max_last = 0
diff_last = 10000
MAX_GENERATION = 5  # 收敛代数
SELECT_NUMBER = 4  # 选择次数
p_c = 0.6  # 交叉概率
p_m = 0.01  # 变异概率


# 个体编码50位
def randGene():
    seed = "01"
    rand = []
    for i in range(N):
        rand.append(random.choice(seed))
    return ''.join(rand)


# 初始化种群
def init():
    p = []  # 种群P(0)
    num = 50  # 种群中个体个数
    for i in range(num):
        p.append(randGene())
    return p


# 适应度函数fitness(p)
def fitness(population):
    # fit = []  # [价值，重量]
    fitprice = []
    fitweight = []
    fit = []
    for item in population:  # 遍历种群中的所有个体，即每次背包的不同装法
        value_sum = 0  # 物品重量
        weight_sum = 0  # 物品价值
        # 将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标
        # print('个体：', item)
        for (i, gene) in enumerate(item):
            # gene位是1表示小偷拿了该物品，所以累计其总重量&价格
            if int(gene) == 1:
                # print('该个体的第', i, '个gene位：', gene, ' 该物品重量：', W[i + 1], '该物品价值：', C[i + 1])
                weight_sum += W[i]
                value_sum += C[i]
        # fit.append([value_sum, weight_sum])
        fitprice.append(value_sum)
        fitweight.append(weight_sum)
    # print('fitness:', fit)
    for i in range(len(population)):
        fit.append(fitprice[i] / np.sum(fitprice))
    return fitprice, fitweight, fit


# 生成随机数组 输入为选择浮点型还是整形、数组长度、区间
def generateRandomNumbers(floatOrInt, count, down, up):
    randomArray = []
    for i in range(count):
        if (floatOrInt == 1):
            randomArray.append(random.uniform(down, up))
        elif (floatOrInt == 0):
            randomArray.append(random.randint(down, up))
    print("生成随机数组：", randomArray)
    return randomArray


# 轮盘赌 输入适应度比值 输出选择出的个体索引
def Roulette(p, count):
    q = []
    tem0 = 0
    for i in range(len(p)):
        tem0 += p[i]
        q.append(tem0)
    test_v = generateRandomNumbers(1, count, 0, 1)
    select = []
    for i in range(count):
        for j in range(len(q)):
            if test_v[i] <= q[j]:
                select.append(j)
                break
    return select


# 交叉
def crossover(population, selected_index):
    population_new = []
    index = len(population) - 1  # selection选择之后剩余的种群个数-1
    while index >= 0:  # 遍历完种群中所有的个体
        index -= 1
        pop_item = population.pop(index)
        print('crossover弹出后种群:', population)
        print('pop_item:', pop_item)  # 弹出的个体
        for i in range(selected_index[index]):
            pop_item_x = random.choice(population)  # 随机选择一个个体
            print('随机选择的个体:', pop_item_x)
            pos = random.choice(range(1, N - 1))  # 随机[1, 2, 3, 4]其中的一个数
            print('pos:', pos)
            population_new.append(pop_item[:pos] + pop_item_x[pos:])
            print('population_new:', population_new)
        population.insert(index, pop_item)  # 恢复原种群
        print('population_4:', population)
    return population_new  # 返回得到的新的种群


# crossover(p, selection(p, fitness(p)))
# def mutation():
#     return 1


if __name__ == '__main__':
    population = init()  # 初始种群
    n = 100  # 迭代次数
    while n > 0:
        n -= 1
        fitnesses = fitness(population)  # 适应度计算
        selected_index = selection(population, fitnesses)
        print('2:', selected_index)
        # 产生下一代
        population = crossover(population, selected_index)
        print('交叉后新种群:', population)
        print(str(n) + '.   .................................')  # 迭代次数
    fitnesses = fitness(population)
    print('fitnesses:', fitnesses)
    # print(population)


# 程序结束条件
# def is_finished(fit):
#     global max_last
#     global diff_last
#     max_current = 0
#     for v in fit:
#         if v[0] > max_current:
#             max_current = v[0]
#     print('max_current:', max_current)  # 得到当前最大的价值
#     diff = max_current - max_last  # 价值差，也就是适应度的改变的大小
#     # 这里判断连续两代的改变量如果都小于5，则停止迭代
#     if diff < MAX_GENERATION and diff_last < MAX_GENERATION:
#         return True
#     else:
#         diff_last = diff
#         max_last = max_current
#         return False

# todo selection精英保留
# 选择【重量大于1000的out】
# def selection(population, fitprice, fit):  # 弹出之后的适应度
#             fitweight.pop(index)
#             fitprice.pop(index)
#             print('pop超重个体后的种群：', population)
#     # 轮盘赌选择
#     selected_index = [0] * len(population)  # 如果[0]*3得到的是[0,0,0]
#     print('selected_index:', selected_index)
#     for i in range(SELECT_NUMBER):  # SELECT_NUMBER：选择次数
#         # 随机选择染色体，然后得到相应的索引
#         j = population.index(random.choice(population))
#         selected_index[j] += 1
#     print('最终selected_index:', selected_index)
#     return selected_index
