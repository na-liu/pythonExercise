# a is b 相当于 id(a) == id(b)
# a id not b
a = b = 1
if a is b:
    print("True", id(a), id(b))
else:
    print("False")
# is与==的区别
c = [1, 2, 3]
d = c
print(c == d)
print(c is d)
d = c[:]
print(d, 'is:', d is c, '==:', d == c)

print('复数', complex(1, 2))
