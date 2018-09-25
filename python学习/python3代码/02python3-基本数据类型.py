
a = b = c = 1
d, e, f = 1, 2, "runob"
print(isinstance(a, int))

# isinstance 和 type 的区别在于：
# ype()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
class A:
  pass
class B(A):
  pass
print(isinstance(A(), A))
print(type(A()) == A)
print(isinstance(B(), A))
print(type(B()) == A)

# 数值运算
print(5 + 4)
print(4.3 - 2)
print(2 * 3)
print(2/3)
print(1002 % 5) # 除法，得到一个整数
print(2 ** 10)  # 乘方

print(-0x2f)
print(3e+3)
print(3e3)
print(3e-3)
print(3 + 4j)
print(3 + 4J)

str1 = 'hello world'
print(str1[0 : -1])
counter = 100 # 整型变量
mules = 1000.0 # 浮点型变量
# 1.Number (数字)
print(counter)
print(mules)
# 2.String (字符串)
name = "runoob" #字符串
print(name)
# 3.list1 (列表)
list1 = [ 'abcd', 786, 2, 23, 'runoob', 70.2 ]
tinylist1 = [1234, 'runoob']
list1.append('hello')
print(list1.pop())
print(list1)
print(list1[0])
print(list1[1:3])
print(list1[2:])
print(list1[:4])
print(tinylist1 * 2)
print(list1 + tinylist1)
for i in list1:
  print(i)
# 4.Tuple (元组)
tup = (1, 2, 2, 3, 3, 4, 5)
tup1 = () # 空元组
tup2 = (20,) # 一个元素需要在元素后添加都好
print(tup1)
print(tup2)
print(tup + tup2)
print(tup2 * 3)
print(tup[2 : 4])

# 5.Set (集合)
# 可以使用大括号 { } 或者 set() 函数创建集合
# 建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
set1 = {1, 2, 3, 4, 5}
set2 = set({1, 2, 3, 4, 5})
x = set("abracadabra")
y = set("abacazam")
print(set())
print(set({}))
print(set1)
print(set2)
print(x)
print(y)
print(x - y) # 差集(或称补集)
print(x & y) # 交集
print(x | y) # 并集
print(x ^ y) # 对称差(a和b中不同时存在的元素)

# 6.dict1ionary (字典))
dict1 = {}
dict1['one'] = '1 - 入门'
dict1[2] = '2 - 基础'
tinydict1 = {
  'name': 'runoob',
  'code': 1,
  'site': 'www.runoob.com'
}
print(dict1)
print(dict1['one'])
print(dict1[2])
print(tinydict1)
print(tinydict1.keys())
print(tinydict1.values())
for k in tinydict1:
  print(k, ':', tinydict1[k])
dict1.clear()
print(dict1)

# Python数据类型转换
print(int("1221213123"))
print(float("2.11"))
print(complex(122, 44))
print(str(A()))
eval("print(list1)")
print(tuple("ababeddeecdg"))
print(list("ababeddeecdg"))
print(set("ababeddeecdg"))
print(frozenset("ababeddeecdg"))
print(dict([('first', 1), ('second', 2), ('third', 3)]))
print(chr(97))
print(ord('a'))
print(hex(97))
print(oct(97))
