var1 = 1
var2 =  10
print(var1, var2)
del var1, var2
from math import ceil, exp, fabs, floor, log, log10, modf, sqrt, e, pi
# 1. 数学函数
print(abs(-100))
print(ceil(12.4))
print(exp(1))
print(fabs(-1.12))
print(floor(12.12))
print(log(exp(3)))
print(log10(100))
print(max(1,2,3,4,5))
print(min(1,2,3,4,5))
print(modf(-55.55))
print(round(5.555, 2))
print(sqrt(16))
print(e)
print(pi)
from random import choice, randrange, random, shuffle, uniform
# 2. 随机函数
print(choice([1, 2, 3, 4]))
print(choice(range(10)))
print(randrange(2, 4))
print(random())
list1 = [1, 2, 3, 4]
shuffle(list1)
print(list1)
print(uniform(6, 100))

#3. 三角函数
from math import acos, asin, atan, atan2, cos, sin, tan, degrees, radians, hypot
print(acos(1))
print(asin(1))
print(atan(2))
print(atan2(2, 1))
print(cos(pi/3))
print(sin(pi/6))
print(tan(pi/4))
print(degrees(pi/2))
print(radians(45))
print(hypot(3, 4))