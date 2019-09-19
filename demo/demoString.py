# str拆分成list又逆向重组
str = "i LIKE APPLE"
str = str.split(" ")[-1::-1]
output = ' '.join(str)
print(output)

a = "a cat\a"  # 响铃
print(a)
a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])

if "H" in a:
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

if "M" not in a:
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print(r'\n')
print(R'\n')

# 字符串格式化
print("我是%s.今年%d岁，考入%s大学" % ('Rachel', 22, '西安电子科技'))

# 字符串内建函数
# 首字母大写
str = "this is a string example!!!"
print("str.capitalize() : ", str.capitalize())
print('是否都是大写：', 'THIS A SUPPER'.isupper())
print("abcd中是否都是小写：", "abcd".islower())
print("aBcd中是都都是小写：", "aBcd".islower())
print('字符串中所有大写转换成小写：', 'THIS IS A change'.lower())
print('字符串中所有小写转换成大写：', 'THIS IS A change'.upper())
print('字符串中大小写互相转换：', 'THIS IS A change'.swapcase())

# 指定宽度居中字符串，第二个参数为填充字符
# 字符串填充，居中/左对齐/右对齐
str1 = "a cat"
print(str1.center(40, '*'))
print(str1.ljust(40, '*'))
print(str1.rjust(40, '*'))
# 指定字符串的长度。原字符串右对齐，前面填充0。
print('abcd'.zfill(20))

# 截取左边或右边的指定字符 lstrip/rstrip
str = "     a cat     ";
print(str.lstrip());
str = "88888a cat88888";
print(str.lstrip('8').rstrip('8'));

# 字串出现的次数 str.count(sub, start= 0,end=len(string))
str = "www.runoob.com"
sub = 'o'
print("str.count('o') : ", str.count(sub))
sub = 'run'
print("str.count('run', 0, 10) : ", str.count(sub, 0, 10))

'''
bytes.decode(encoding="utf-8", errors="strict")
errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 
其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。
'''
str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
print(str)
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
print("GBK 解码：", str_gbk.decode('GBK', 'strict'))

# endswith:判断指定字符串中是否以suffix结尾
# 其后两个参数表示需要判断的字串部分，前闭后开原则
# 单个参数的，表示起始位置
Str = '01234567!!'
suffix = '!!'
print(Str.endswith(suffix))
print(Str.endswith(suffix, 9))
suffix = 'run'
print(Str.endswith(suffix))
print(Str.endswith(suffix, 0, 19))

# 替换\t制表符
str = "this is\tstring"
print("原始字符串: " + str)
print("替换 \\t 符号: " + str.expandtabs())
print("使用16个空格替换 \\t 符号: " + str.expandtabs(16))

# 查找字符串中子串首次出现的索引值
# str.find(str, beg=0, end=len(string))
# index与find用法一致，当字串找不到时，index会报错
info = "abcdabcd"
print("首次出现的索引值：", info.find("a"))
print(info.find("a", 4))
print(info.rfind("a"))  # 从右开始找
print(info.find("a", 5, 7))
print(info.find("e"))
# print(info.index("e"))
'''
Traceback (most recent call last):
  File "D:/pythonCode/python3exercise/demodemo.py", line 9, in <module>
    print(info.index("e"))
ValueError: substring not found
'''

# 检查str中是否只包含字母&数字
print("ab1c3d1中只有数字字母：", "ab1c3d1".isalnum())
print("a cat中只有数字字母：", "a cat".isalnum())
print("abcd中只含字母：", "abcd".isalpha())
print("abcd123中只含字母：", "abcd123".isalpha())
print("abcd中只含字母：", "abcd".isalpha())
print("abc.d中只含字母：", "abc.d".isalpha())
# 数字判断的区别：
a = "1"  # 英文
b = "1"  # 中文
c = "IV"  # 英文的罗马数字
d = "三四五"  # 汉字数字
e = b"12"  # byte
print('全角数字：', a.isdigit(), a.isdecimal(), a.isnumeric())
print('半角数字：', b.isdigit(), b.isdecimal(), b.isnumeric())
print('罗马数字：', c.isdigit(), c.isdecimal(), c.isnumeric())
print('汉字数字：', d.isdigit(), d.isdecimal(), d.isnumeric())
print('byte:', e.isdigit())
# AttributeError: 'bytes' object has no attribute 'isnumeric' 'isdecimal'

print('是否有空格：', '              '.isspace())
print('是否是标题：', 'This Is A Title'.istitle())
print('标题化：', 'this is a title'.title())
print('字符串长度：', len('superviser'))
print('最大的字母：', max('abcdefg'))
print('最小的字母：', min('abcdefg'))

# tuple字符串连接
tuple = ('a', 'b', 'c', 'd', 'e')
print('用-连接tuple:', '-'.join(tuple))
print('直接拼接tuple:', ''.join(tuple))

# 将字符串中特定字符转换成另外的字符
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)  # 转换表,将in映射为out
str = "This a cat and you are a beautiful girl!!!"
print(str.translate(trantab))  # 加密
# 参数分别表示，旧字符，新字符，替换最大次数
replace = 'a cat is a cat'
print(replace.replace('cat', 'dog', 1))
print(replace.replace('cat', 'dog', 2))
