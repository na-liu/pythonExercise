# 条件语句
a = 4
if a in (1, 2, 3):
    print("one")
elif a in (4, 5, 6):
    print("two")
else:
    print("win")

# 循环语句
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n, sum))

for i in range(5):  # range(2,9)
    print(i, end=',')

# break,continue 跳出循环
# pass 空语句
