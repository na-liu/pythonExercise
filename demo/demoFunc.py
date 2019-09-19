from math import *
import random

# 数学函数
print(abs(-10))  # 绝对值
print(fabs(-10))  # 绝对值，浮点型
print(ceil(4.1))  # 向上取整
print(floor(4.9))  # 向下取整
print(round(3.4), round(3.5))  # 四舍五入
print(exp(1))  # e的n次幂
print(pow(2, 3))  # a的b次幂，a**b
print(log(e))  # 以e为底的对数
print(log10(100))  # 以10为底的对数
print(sqrt(9))  # 根号
print(max(1, 2, 3, 4, 5, 6, 723))  # 给定参数的最大值
a = [1, 2, 3, 4, 5]
print(min(a))  # 给定参数的最小值，参数可以是序列
print(modf(1.22))  # 返回整数部分和小数部分

# 三角函数
print("acos(1)=", acos(1))
print("acos(-1)=", acos(-1))
# 角度、弧度互换
print("pi是多少度：", degrees(pi))
print("90°转化为弧度：", radians(90))

# 随机函数
print(random.choice(a))  # 从序列中随机挑选一个元素
print(random.choice(range(10)))  # 从0-9中随机choose一个整数
print(random.random())  # [0,1),浮点数
# 从 1-100 中选取一个奇数，第三个参数为步长，缺省值为1
print("randrange(1,100, 2) : ", random.randrange(1, 100, 2))
# 从 0-99 选取一个随机数
print("randrange(100) : ", random.randrange(100))
random.seed()
print("使用默认种子生成随机数：", random.random())
random.seed(10)
print("使用整数种子生成随机数：", random.random())
random.seed("hello", 2)
print("使用字符串种子生成随机数：", random.random())
a = [1, 2, 3, 4]
random.shuffle(a)  # 洗牌
# todo there is a question that I run this program every time and get the same result,why?
# The friends say it's because of the random seed.
# so, I set a seed and the result changes.But if seed doesn't change, the result still don't change.
print(a)
print(random.uniform(2, 100))  # 在[2,100]范围内随机生成实数
