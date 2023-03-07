# # Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# # *Пример:*

# # A = 3; B = 5 -> 243 (3⁵)
# #     A = 2; B = 3 -> 8 
result = 0
a = int(input())
b = int(input())
def expon(a,b):
    result = 0
    if b <= 1:
        return a
    result = a ** b
    return result
print(expon(a, b))