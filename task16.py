# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1


import random

min = 0
min1 = 1
max = 5
try:
    # N = 20//2
    N = int(input("Введите размер массива: "))//2
    # X = random.randint(min,max)
    X = int(input("Введите число поиска: "))
    print(X)
    numbers = []
    for num in range(min,N):
        numbers.append(random.randint(min1,max))
    count = 0
    print(numbers)
    if X in numbers:
        for n in numbers:
            if n == X:
                count+=1
        print(f"Число {X} встречается {count} раз")
    else:
        print(f"Число {X} ни разу не встречается")
except:
    print("Упс, что-то пошло не так")