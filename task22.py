# # Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# # Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах
# # Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# # m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random
n = int(input())
m = int(input())
list1 = []
list2 = []
listfin = []
for i in range(n):
    list1.append(random.randint(0, 19))
print(list1)
for j in range(m):
    list2.append(random.randint(0, 19))
print(list2)
for k in list1:
    for q in list2:
        if k == q: 
            listfin.append(k)
print(*sorted(set(listfin)))
