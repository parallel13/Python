# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from sem6modul import FillArray


list_1= FillArray()
min_number = int(input('введите минимальное число: '))
max_number = int(input('введите минимальное число: '))
print(list_1)
for i in range(len(list_1)):
    if min_number <= list_1[i] <= max_number:
        print(i)



