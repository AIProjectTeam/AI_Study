# 单行注释

# 第一个注释
#第二个注释
'''
第三行注释
第四行注释
'''
"""
第五行注释
第六行注释
"""
import keyword
print(keyword.kwlist)
print("hello, python!")
if True:
  print("Answer")
  print("True")
else:
  print("Answer")
  print("False")
total = 1 + \
        2 + \
        3
print(total)
list = ['item1', 'item2', 'item3',
        'item4', 'item5']
print(list)
str = '''11111
11212
212121

21212212
21212'''
str1 = '1234567\n'
str2 = r'1234567\n'
str3 = "this " "is " "string"
str4 = 'abc' + '123'
str5 = 'abc' * 4
print(str)
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str2[0], str2[-1], str2[-2])
print(str2[2:7])

# import 与 from...import
import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
  print(i)
print('\n python 路径为', sys.path)

from sys import argv, path
for i in argv:
  print(i)
print('\n python 路径为', path)