# Задача 18: Требуется найти в массиве A[1..N]
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

num_x = int(input('Колличество элементов в массиве '))
list_a = []
for i in range(num_x):
    n = int(input())
    list_a.append(n)
print(list_a)
difference = list_a[0]
num_y = int(input('Какое число ищем : '))
n = abs(num_y-list_a[0])
for j in range(len(list_a)):
    if n > abs(list_a[j]-num_y):
        n = num_y-list_a[j]
        difference = list_a[j]
print(f'Близкое число: {difference}')
