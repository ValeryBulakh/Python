# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random
import os
os.system('cls')
try:
    N = int(input("Введите количество кустов на вашей любимой грядке: "))
    # N = 9
    min = 1
    max = 10
    countTotal = 0
    harvest = max/2*N
    bushes = [] # кусты
    for bush in range(min,N):
        count = random.randint(min,max)
        bushes.append(count)
        countTotal+= count
    if countTotal>harvest:
        print(f"Кусты: {bushes} урожайный нынче год выдался :)")
    else:
        print(f"Кусты: {bushes} худовато нынче :(")
    print("Пойдем собирать...")
    index = 0
    countOnBush = 0
    maxOnBush = 0
    while index< len(bushes):
        # print(bushes[count])
        if index == 0:
            countOnBush = bushes[-1] + bushes[index] + bushes[index+1]
        elif index == len(bushes)-1:
            countOnBush = bushes[0] + bushes[index] + bushes[index-1]
        else:
            countOnBush = bushes[index-1] + bushes[index] + bushes[index+1]
        index+=1
        if countOnBush > maxOnBush:
            maxOnBush = countOnBush
    print(f"Максимум с трех кустов: {maxOnBush}")
except:
    print("Что-то пошло не так :(")