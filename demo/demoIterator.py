# 创建一个迭代器
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self): # 自行构造迭代器
        if self.a <= 20: # 增加迭代范围
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
