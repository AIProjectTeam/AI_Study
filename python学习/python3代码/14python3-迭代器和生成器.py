# 1. 迭代器的两个基本的方法：iter() 和 next()
list = [1, 2, 3, 4]
it = iter(list)
print(next(it))
print(next(it))

# 2. 迭代器对象可以使用常规for语句进行遍历
list = [1, 2, 3, 4]
it = iter(list)
for item in it:
  print(item, end=" ")
print()
# 3. 也可以使用next()函数
import sys
list = [1, 2, 3, 4]
it = iter(list)
# while True:
#   try:
#     print(next(it))
#   except StopIteration:
#     sys.exit()
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    x = self.a
    self.a += 1
    return x
myClass = MyNumbers()
myIter = iter(myClass)
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
