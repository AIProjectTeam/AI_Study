# 1. while 循环
num = 100
sum = 0
counter = 1
while counter <= num:
  sum += counter
  counter += 1
print(sum)

# 2. 无限循环
num = 1
while num != 0 :  # 表达式永远为 true
   num = int(input("输入一个数字  :"))
   print ("你输入的数字是: ", num)
print ("Good bye!")

# 3. while 循环使用 else 语句
count = 0
while count < 5:
  print(count, ' 小于5')
  count += 1
else:
  print(count, ' 大于或等于5')

# 4. for 循环
arr1 = [1, 2, 3, 4, 5, 6]
for i in range(len(arr1)):
  print('第%d个元素为: %d' % (i + 1, arr1[i]))
for index, item in enumerate(arr1):
  print('第%d个元素为: %d' % (index + 1, item))

# 5. pass 语句
for letter in 'Runoob': 
  if letter == 'o':
    pass
    print ('执行 pass 块')
  print ('当前字母 :', letter)
print ("Good bye!")