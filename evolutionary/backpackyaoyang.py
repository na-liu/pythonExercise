import random
import matplotlib.pyplot as plt
import heapq
import time

# 3103 1000

start = time.time()

N = 50  # 种群数量
n = 50  # 编码长度
v = 1000  # 背包总容量
N_C = int(N / 5)
# 价值
C = [220, 208, 198, 192, 180, 180, 165, 162, 160, 158, 155, 130, 125, 122, 120, 118, 115, 110, 105, 101, 100, 100, 98,
     96, 95, 90, 88, 82, 80, 77, 75, 73, 72, 70, 69, 66, 65, 63, 60, 58, 56, 50, 30, 20, 15, 10, 8, 5, 3, 1]

# 容积
W = [80, 82, 85, 70, 72, 70, 66, 50, 55, 25, 50, 55, 40, 48, 50, 32, 22, 60, 30, 32, 40, 38, 35, 32, 25, 28, 30, 22, 50,
     30, 45, 30, 60, 50, 20, 65, 20, 25, 30, 10, 20, 25, 15, 10, 10, 10, 4, 4, 2, 1]

x = []
p_c = 0.6  # 交叉概率
p_m = 0.01  # 变异概率


def takeFirst(elem):
    return elem[0]


# 目标函数 参数为价值、容积、是否选择、物体总量、背包总容量 计算个体适应度值
def objectiveFunction(c, w, the_generation, n, v):
    fx = []
    gx = []
    p = []
    temp1 = 0
    temp2 = 0
    for i in range(len(the_generation)):
        # print(the_generation[i])
        the_gene = list(the_generation[i])
        for j in range(len(the_gene)):
            temp1 += c[j] * int(the_gene[j])
            temp2 += w[j] * int(the_gene[j])
        fx.append(temp1)
        gx.append(temp2)
        temp1 = 0
        temp2 = 0
        # the_generation[i] = "".join(the_generation[i])
    print('fx', fx)
    print('gx', gx)
    for i in range(len(the_generation)):
        p.append(fx[i] / sum(fx))
    print('实用度函数：', p)
    return fx, gx, p  # ,the_generation


# 交叉 输入为两个待交叉的数组、交叉概率 输出为交叉完的两个数组
def cross(c_1, c_2):
    # print(c_1,c_2)
    first = random.randint(0, 32)
    second = random.randint(0, 32)
    min1 = min(first, second)
    max1 = max(first, second)
    # print(min1,max1)
    part_1 = c_1[:min1]
    part_2 = c_1[min1:max1]
    part_3 = c_1[max1:]
    part_one = c_2[:min1]
    part_two = c_2[min1:max1]
    part_three = c_2[max1:]
    c_1 = part_1 + part_two + part_3
    c_2 = part_one + part_2 + part_three
    # print(c_1, c_2)
    # print('\n')
    return c_1, c_2


# 变异 输入为待变异数组、变异概率 输出为变异完的数组
def variation(c, p_m):
    # print(c)
    c = list(c)
    for i in range(len(c)):
        qw = random.uniform(0, 1)
        # print(qw)
        if qw <= p_m:
            # print(i)
            if c[i] == '1':
                c[i] = '0'
            elif c[i] == '0':
                c[i] = '1'
    c = "".join(c)
    # print(c)
    # print('\n')
    return c


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


# 生成N个初始种群 输入种群数量、编码长度 输出随机生成的种群
def generateGeneration(count, CodeLength):
    next_generation = []
    for i in range(count):
        data = generateRandomNumbers(0, 1, 0, 2 ** CodeLength - 1)
        data = bin(data[0])
        data = list(data)
        data = data[2:]
        while len(data) < n:
            data.insert(0, '0')
        data = "".join(data)
        next_generation.append(data)
    return next_generation


# 轮盘赌 输入适应度比值 输出选择出的个体索引
def Roulette(p, count):
    # print('轮盘赌的p', len(p))
    q = []
    tem0 = 0
    for i in range(len(p)):
        tem0 = tem0 + p[i]
        q.append(tem0)

    test_v = generateRandomNumbers(1, count, 0, 1)

    select = []
    for i in range(count):
        for j in range(len(q)):
            if test_v[i] <= q[j]:
                select.append(j)
                break
    return select


########################################进化过程#########################
def evolution(the_generation):
    fx, gx, p = objectiveFunction(C, W, the_generation, n, v)

    re = list(map(fx.index, heapq.nlargest(1, fx)))
    print(the_generation[re[0]])
    print(round(float(fx[re[0]]), 4), '     ', round(float(gx[re[0]]), 4))
    ay.append(fx[re[0]])

    select = Roulette(p, len(the_generation))  # 轮盘赌选择
    print('轮盘赌选择的结果', select)
    test_c = generateRandomNumbers(1, int(N / 2), 0, 1)

    O1 = []  # 交叉产生的后代

    j = 0
    for i in range(int(N / 2)):
        if test_c[i] <= p_c:
            child1, child2 = cross(the_generation[select[j]], the_generation[select[j + 1]])
            O1.append(child1)
            O1.append(child2)
        else:
            O1.append(the_generation[select[j]])
            O1.append(the_generation[select[j + 1]])
        j = j + 2

    O2 = []  # 变异产生的后代

    for i in range(len(O1)):
        child = variation(O1[i], p_m)
        O2.append(child)

    children = O2
    the_generation = the_generation + children

    if len(children) == 0:
        next_generation = the_generation
    else:
        fx1, gx1, p1 = objectiveFunction(C, W, the_generation, n, v)  # 解码结果、适应度、个体适应度比值
        re1 = list(map(fx1.index, heapq.nlargest(N_C, fx1)))
        next_generation = []
        for i in range(len(re1)):
            next_generation.append(the_generation[re1[i]])
        select1 = Roulette(p1, N - N_C)  # 轮盘赌选择
        for i in range(len(select1)):
            next_generation.append(the_generation[select1[i]])
    ################3#######################################################33
    for i in range(len(next_generation)):
        b = []
        next_generation[i] = list(next_generation[i])
        for j in range(len(next_generation[i])):
            if next_generation[i][j] == '1':
                value_density = C[j] / W[j]
                b.append([value_density, j])
        b.sort(key=takeFirst, reverse=True)
        weight = 0
        for k in range(len(b)):
            weight += W[b[k][1]]
            if weight > v:
                next_generation[i][b[k][1]] = '0'
        next_generation[i] = "".join(next_generation[i])
    ###############################################################################
    return next_generation


##########################主函数##########################################
ax = []  # 定义一个 x 轴的空列表用来接收动态的数据
ay = []  # 定义一个 y 轴的空列表用来接收动态的数据

next_generation = generateGeneration(N, n)
# print(next_generation)

for i in range(200):
    ax.append(i)  # 添加 i 到 x 轴的数据中
    next_generation = evolution(next_generation)

end = time.time()
print(end - start)
plt.plot(ax, ay, '.')
plt.show()
