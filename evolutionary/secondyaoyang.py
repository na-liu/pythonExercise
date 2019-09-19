import numpy as np
import math
import random
import heapq
import matplotlib.pyplot as plt
import time

# -2.048 -2.048 3905.9262268
start = time.time()

# 初始化变量
N = 300            #种群数量
N_C = int(N/5)
e = 10 ** -4        #
p_c = 0.6           #交叉概率
p_m = 0.01          #变异概率
x1_left = -2.048
x1_right = 2.048
x2_left = -2.048
x2_right = 2.048

# 计算编码长度 参数为x1、x2左右界限 返回x1、x2、总体编码长度
def computeCodeLenght(x1_left,x1_right,x2_left,x2_right,e):
    x1CodeLength = math.floor(math.log((x1_right-x1_left)/e+1,2)+1)
    x2CodeLength = math.floor(math.log((x2_right -x2_left)/e+1,2)+1)
    CodeLength = x1CodeLength + x2CodeLength
    return x1CodeLength,x2CodeLength,CodeLength

# 目标函数 参数为x1、x2 计算个体适应度值
def objectiveFunction(x1,x2):
    return 100 * (x2 - x1 * x1) * (x2 - x1 * x1) + (1 - x1) * (1 - x1)

# 对个体解码 参数一行待解码数及x1、x2编码长度 返回两个解码后的x1和x2的十进制数值数组
def decode(x,x1CodeLength,x2CodeLength):
    x1 = x[:x1CodeLength]
    x2 = x[x1CodeLength:]
    x1 = int(x1,2)
    x2 = int(x2,2)
    x1 = x1_left + (x1_right - x1_left) * x1 / (2 ** x1CodeLength - 1)
    x2 = x2_left + (x2_right - x2_left) * x2 / (2 ** x2CodeLength - 1)
    x = [x1,x2]
    # print(x)
    return x

# 交叉 输入为两个待交叉的数组、交叉概率 输出为交叉完的两个数组
def cross(c_1,c_2):
    # print(c_1,c_2)
    first = random.randint(0, 32)
    second = random.randint(0, 32)
    min1 = min(first,second)
    max1 = max(first, second)
    # print(min1,max1)
    part_1 = c_1[:min1]
    part_2 = c_1[min1:max1]
    part_3 = c_1[max1:]
    part_one = c_2[:min1]
    part_two = c_2[min1:max1]
    part_three = c_2[max1:]
    c_1 = part_1+part_two+part_3
    c_2 = part_one + part_2 + part_three
    # print(c_1, c_2)
    # print('\n')
    return  c_1,c_2



# 变异 输入为待变异数组、变异概率 输出为变异完的数组
def variation(c,p_m):
    # print(c)
    c = list(c)
    for i in range(len(c)):
        qw = random.uniform(0,1)
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

# 计算适应度值 输入为种群 输出为解码后的x1、x2数组和种群适应度值
def adaptability(v,count):
    vv = []  # 解码结果
    sy = []  # 适应度的值
    p = []   #个体的适应度占总适应度的比值
    for i in range(count):
        tem = decode(v[i], x1CodeLength, x2CodeLength)
        vv.append(tem)
        sy.append(objectiveFunction(tem[0], tem[1]))

    for i in range(count):
        p.append(sy[i] / sum(sy))
    return vv,sy,p

# 生成随机数组 输入为选择浮点型还是整形、数组长度、区间
def generateRandomNumbers(floatOrInt,count,down,up):
    randomArray = []
    for i in range(count):
        if(floatOrInt==1):
            randomArray.append(random.uniform(down,up))
        elif(floatOrInt==0):
            randomArray.append(random.randint(down,up))
    return randomArray

# 生成N个初始种群 输入种群数量、编码长度 输出随机生成的种群
def generateGeneration(count,CodeLength):
    next_generation = []
    for i in range(count):
        data = generateRandomNumbers(0, 1, 0, 2 ** CodeLength - 1)
        data = bin(data[0])
        data = list(data)
        data = data[2:]
        while len(data) < CodeLength:
            data.insert(0,'0')
        data = "".join(data)
        next_generation.append(data)
    return next_generation

# 轮盘赌 输入适应度比值 输出选择出的个体索引
def Roulette(p,count):
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
def evolution(v):

    vv,sy,p = adaptability(v,len(v))     # 解码结果、适应度、个体适应度比值
    re = list(map(sy.index, heapq.nlargest(1, sy)))
    print(v[re[0]])
    print(round(float(vv[re[0]][0]),4),round(float(vv[re[0]][1]),4))
    print(round(float(sy[re[0]]),4))
    ay.append(sy[re[0]])
    select = Roulette(p,len(v))          # 轮盘赌选择

    test_c = generateRandomNumbers(1,int(N/2),0,1)

    O1 = []#交叉产生的后代
    j=0
    for i in range(int(N/2)):
        if test_c[i] <= p_c:
            child1,child2 = cross(v[select[j]],v[select[j+1]])
            O1.append(child1)
            O1.append(child2)
        else:
            O1.append(v[select[j]])
            O1.append(v[select[j+1]])
        j=j+2

    O2 = []#变异产生的后代

    for i in range(len(O1)):
        child = variation(O1[i] , p_m)
        O2.append(child)

    children = O2
    the_generation = v + children
    if len(children) == 0:
        next_generation = v
    else:
        vv1, sy1, p1 = adaptability(the_generation,len(the_generation))  # 解码结果、适应度、个体适应度比值
        re1 = list(map(sy1.index, heapq.nlargest(N_C, sy1)))
        # print("re1的长度",len(re1))
        next_generation = []
        for i in range(len(re1)):
            next_generation.append(the_generation[re1[i]])

        select1 = Roulette(p1,N-N_C)  # 轮盘赌选择
        for i in range(len(select1)):
            next_generation.append(the_generation[select1[i]])
    return next_generation
##########################主函数##########################################
ax = []                    # 定义一个 x 轴的空列表用来接收动态的数据
ay = []                    # 定义一个 y 轴的空列表用来接收动态的数据
x1CodeLength,x2CodeLength,CodeLength = computeCodeLenght(x1_left,x1_right,x2_left,x2_right,e)
next_generation = generateGeneration(N,CodeLength)

for i in range(100):
    ax.append(i)               # 添加 i 到 x 轴的数据中
    next_generation = evolution(next_generation)

end = time.time()
print('运行时间：',end-start)
plt.plot(ax,ay,'.')
plt.show()