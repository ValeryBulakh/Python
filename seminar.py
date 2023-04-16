list_a = [1, 1, 2, 0, -1, 3, 4, 4]
#list_b = []
#list_b.append(list_a[0])

"""for i in range(len(list_a)+1):
c=0
for j in range(i+1, len(list_a)+1):
if list_a[i] == list_a[j]:
c=1
break
if c==0:
list_b.append(list_a[i])

print(list_b)"""

list_b = []
for i in list_a: #проверяет не номер элемента, а значение элемента, т.к. нет range
if i in list_b:
pass
else:
list_b.append(i)

print(list_b)
Евгений: list_1=[1, 1, 2, 0, -1, 3, 4, 4]
print(list_1)
# c=list(set(list_1))
print(list(set(list_1)))


list_a = [1, 2, 3, 4, 5]
k = int(input("Введите число к: "))%len(list_a)
list_b = []
for i in range(k, len(list_a)):
list_b.append(list_a[i])
for i in range(k):
list_b.append(list_a[i])
print(list_b)

print(list_a[k:] + list_a[:k])

