# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


def power(A,B):
    if B>0:
        return A*power(A,B-1)
    else:
        if B<0:
            print("Введите положительную степень")
            return 0
        else:
            return 1

try:
    A = int(input("Введите число А: "))
    B = int(input("Введите число B: "))3
    res = power(A,B)
    print(res)
except:
    print("Что-то пошло не так")