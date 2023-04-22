# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


import random
import os
# import function as f
os.system('cls')

def FindIntersect(set1, set2):
    nums = []
    for num in set1:
        if num in set2:
            nums.append(num)
    return nums
try:
    n = int(input("Введите кол-во элементов первого набора: "))
    m = int(input("Введите кол-во элементов второго набора: "))
    # n = 6
    # m = 7

    min = 1
    max = 6
    nums1 = []
    nums2 = []
    for num in range(0,n):
        nums1.append(random.randint(min,max))
    print(nums1)
    for num in range(0,m):
        nums2.append(random.randint(min,max))
    print(nums2)
    setNum1 = set(nums1)
    # print(setNum1)
    setNum2 = set(nums2)
    # print(setNum2)
    # setNew = setNum1 & setNum2
    setNew = FindIntersect(setNum1, setNum2)
    print(f"Пересечение: {setNew}")
except:
    print("Что-то пошло не так :(")