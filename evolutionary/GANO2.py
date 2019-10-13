import math
import random
import heapq
import time
import matplotlib.pyplot as plt

start = time.time()

# ----------------------------初始化定义变量-------------------------
x1_left = -2.048  # x1，x2变量的范围
x1_right = 2.048
x2_left = -2.048
x2_right = 2.048
precision = 10 ** -4  # 精度要求
pc = 0.6  # 交叉概率
pm = 0.01  # 变异概率
N = 100  # 种群规模
T = 100  # 种群代数
E = int(N / 5)  # 精英保留数
ax = []
ay = []


# -----------------------------计算编码位数---------------------------
def count_code_gene():
    x1_len = math.ceil(math.log((x1_right - x1_left) / precision + 1, 2))  # 18
    x2_len = math.ceil(math.log((x2_right - x2_left) / precision + 1, 2))  # 15
    # print(x1_len, x2_len)
    gene_length = x1_len + x2_len
    return x1_len, x2_len, gene_length


# ---------生成随机个体，编码[input:编码位数，output:个体gene]--------
def create_random_individual():
    gene_str = ''
    for i in range(gene_length):
        gene_str += str(random.randint(0, 1))
    # print(isinstance(gene_str,str))
    return gene_str


# ------初始化种群;input:种群规模，gene个数，output:初始种群-----------
def init_generation(population_size):
    next_generation = []
    for i in range(population_size):
        next_generation.append(create_random_individual())
    # print('初始化种群：', next_generation)
    return next_generation


# ----个体解码,input:个体和两变量长度，output:解码后的两个变量值--------
def decode(gene_str):
    x1 = int(gene_str[:x1_len], 2)
    x2 = int(gene_str[x1_len:], 2)
    x1 = x1_left + (x1_right - x1_left) * x1 / (2 ** x1_len - 1)
    x2 = x2_left + (x2_right - x2_left) * x2 / (2 ** x2_len - 1)
    # print('解码：', x1, x2)
    return x1, x2


# --------------------------目标函数------------------------------------
def fitness(x1, x2):
    return 21.5 + x1 * math.sin(4 * math.pi * x1) + x2 * math.sin(20 * math.pi * x2)


# --------计算个体适应度值;[input:种群，output:适应度list]--------------
def adaption(generation, count):
    # x1_len, x2_len = count_code_gene()[:2]
    individual = []  # x1,x2
    fit = []  # 个体的适应度值
    proportion = []  # 个体适应度值占比
    for i in range(count):
        # print('个体： ', generation[i])
        x1, x2 = decode(generation[i])
        individual.append([x1, x2])
        fit.append(fitness(x1, x2))
    for i in range(count):
        proportion.append(fit[i] / sum(fit))
    return fit, proportion, individual


# -------轮盘赌选择m个算法[input:proportion，output:所选择的个体]-------
def roulette(proportion, count):
    q = []  # 累计适应度
    select = []  # 最终选出来的个体编号
    for i in range(len(proportion)):  # 计算概率累计值个数此处用了count所以错了
        q.append(proportion[i] + sum(proportion[:i]))

    for i in range(count):  # 选count个
        rand = random.uniform(0, 1)  # 生成1个[0,1]随机数
        for j in range(len(q)):
            if rand <= q[j]:
                select.append(j)
                break
    # print("轮盘赌选择的结果：", select)
    return select


# 一次交叉[input:父代两个gene_str，output:子代新的两个gene_str]
def crossover(father, mother):
    a = random.randint(0, gene_length - 1)  # 随机找两个交叉点
    b = random.randint(0, gene_length - 1)
    first = min(a, b)
    second = max(a, b)
    # print('交叉点：', first, second)
    ch1 = father[:first] + mother[first:second] + father[second:]
    ch2 = mother[:first] + father[first:second] + mother[second:]
    return ch1, ch2


# ----------------------------个体变异-------------------------------
# bug:individual是string类型，是一种区别于list的不可变类型，所以不能直接赋值改变某一位的值
# solve:可以直接string转为list
def mutation(individual):
    # print('变异前：', individual)
    individual = list(map(int, individual))  # string ---> list
    for i in range(len(individual)):
        rand = random.uniform(0, 1)
        if rand <= pm:
            individual[i] = 0 if individual[i] == 1 else 1
    individual = ''.join(str(i) for i in individual)  # list ---> string
    # print('变异后：', individual)
    return individual


# -------------------------------进化--------------------------------
# bug:每一代种群的数量不固定，一直在减少
# solve:轮盘赌第一个for循环个数写错了
def evolution(generation, t):
    # 选择出来的N个父代个体进行N/2次交叉产生的N个子代个体，在进行N次变异
    fit, proportion, individual = adaption(generation, len(generation))  # 这一代种群的适应度
    # --------------------------------------------------
    re = list(map(fit.index, heapq.nlargest(1, fit)))  # 选出一个适应度最大的个体
    # print('种群', generation[re[0]])
    # print('x1,x2', round(float(individual[re[0]][0]), 4), round(float(individual[re[0]][1]), 4))
    best = round(float(fit[re[0]]), 4)
    print('第', t, '代：', best)
    ay.append(best)
    # ---------------------------------------------------
    select = roulette(proportion, len(generation))  # 轮盘赌选择的个体N个

    # 交叉
    rand = []
    for i in range(int(N / 2)):
        rand.append(random.uniform(0, 1))  # N/2个随机数，判断这一对是否可以交叉生成后代
    offspring = []  # 交叉产生的后代
    j = 0
    for i in range(int(N / 2)):
        father = generation[select[j]]
        mother = generation[select[j + 1]]
        if rand[i] <= pc:
            child1, child2 = crossover(father, mother)
            offspring.append(child1)
            offspring.append(child2)
        else:
            offspring.append(father)
            offspring.append(mother)
        j += 2

    # 变异
    offspring1 = []  # 变异后代
    for i in range(len(offspring)):
        child = mutation(offspring[i])
        offspring1.append(child)
    the_generation = generation + offspring + offspring1  # 2N

    # 轮盘赌下一代
    next_generation = []
    if len(offspring1) == 0:
        next_generation = generation
    else:
        fit, prop, indi = adaption(the_generation, len(the_generation))
        # ------------
        re1 = list(map(fit.index, heapq.nlargest(E, fit)))  # 选出适应度最大的E = 1/5N个个体，放到下一代
        for i in range(len(re1)):
            next_generation.append(the_generation[re1[i]])
        select1 = roulette(prop, N - E)  # 轮盘赌选择，选出N - E个个体，放入下一代
        for i in range(len(select1)):
            next_generation.append(the_generation[select1[i]])
        # -------------
    return next_generation


# -------------------------------主函数------------------------------
if __name__ == '__main__':
    x1_len, x2_len, gene_length = count_code_gene()  # 获取长度
    generation1 = init_generation(N)  # 获取第一代种群
    for i in range(T):  # 进化T代
        ax.append(i)
        generation1 = evolution(generation1, i)

    end = time.time()
    print('运行时间：', end - start)
    plt.plot(ax, ay, '.')
    plt.show()
