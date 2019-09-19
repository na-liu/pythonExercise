import sys

list = [1, 2, 3]
it = iter(list)  # 创建迭代器对象
print(next(it))
print(next(it))
print(next(it))

a = [1, 2, 3, 4]
it = iter(a)
# for x in it:
#     print(x, end=' ')

while it:
    try:
        print(next(it), end=' ')
    except StopIteration:  # 需要抛异常
        sys.exit()


