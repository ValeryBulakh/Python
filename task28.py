# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def sum(a,b):
    if b>0:
        a = a + 1
        return sum(a,b-1)
    else:
        return a

try:
    a = int(input("Введите первое неотрицательное слагаемое: "))
    b = int(input("Введите второе неотрицательное слагаемое: "))
    if a>=0 and b>=0:
        res = sum(a,b)
        print(res)
    else:
        print("Sorry, введите положительные числа")
except:
    print("Что-то пошло не так")