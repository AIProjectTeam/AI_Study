# 1. Python算数运算符 (+, -, *, /, %, **, //)
print(3+5) # +: 加
print(3-5) # -: 减
print(3*5) # *: 乘
print(3/5) # /: 除
print(3%5) # %: 取余
print(3**5)# **: 幂运算
print(3//5)# //: 取整除

# 2. Python比较运算符 (==, !=, >, <, >=, <=)
print(2 == 3)
print(2 != 3)
print(2 > 3)
print(2 < 3)
print(2 >= 3)
print(2 <= 3)

# 3. Python赋值运算符 (=, +=, -=, *=, /=, %=, **=, //=)
a = 2 + 3
print(a)
a += 3
print(a)
a -= 3
print(a)
a *= 3
print(a)
a /= 3
print(a)
a %= 3
print(a)
a **= 3
print(a)
a //= 3
print(a)

# 4. Python位运算符 (&, |, ~, ^, <<, >>)
a = 60     # 60 = 0011 1100
b = 13     # 13 = 0000 1101
c = 0

c = a & b
print(c)
c = a | b
print(c)
c = ~a
print(c)
c = a ^ b
print(c)
c = a << 2
print(c)
c = a >> 2
print(c)

# 5. Python逻辑运算符 (and, or, not)
a = True
b = False
print(a and b)
print(a or b)
print(not b)
print(not a and b)
print(not b and a)

#6. Python成员云算符 (in, not in)
c = 1
d = 6
list1 = [1, 2, 3, 4, 5]
print(c in list1)
print(c not in list1)
print(d in list1)
print(d not in list1)

#7. Python身份云算符 (is, is not)
a = 20
b = 20
print(a is b)
print(id(a) == id(b))
print(a is not b)
print(id(a) != id(b))
'''
is 与 == 区别：
is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
'''
a = [1, 2, 3, 4, 5, 6, 7]
b = a
print(b is a)
print(b == a)
b = a[:]
print(b is a)
print(b == a)