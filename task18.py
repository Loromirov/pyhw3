# # Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине 
# # элемент к заданному числу X. Пользователь в первой строке вводит натуральное 
# # число N – количество элементов в массиве. В последующих  строках записаны 
# # N целых чисел Ai. Последняя строка содержит число X

# # *Пример:*

# # 5
# #     1 2 3 4 5
# #     6
# #     -> 5

import random
import math
list1 = []
n = int(input("Введите длинну массива: "))
x = int(input("Введите число X: "))
for i in range(n):
    list1.append(random.randint(1, 10))
print(list1)

minNum = 0
minDiff = math.inf
for i in list1:
    if abs(x - i) < minDiff:
        minDiff = abs(x - i)
        minNum = i
print(minDiff, minNum)


