import random
# x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# x = [1, 3, 5, 7, 9 ]
# y = [2, 4, 6, 8, 10]
# for x,y in zip(x, y):
#   print(x, y)
#i = [i for i in range(10)]
# print(i)

data = [n for n in range(10)]
random.shuffle(data)
print(data)
print(data[:4])