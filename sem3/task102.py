#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X

n= int(input('введите натуральное число N: '))
print("введите каждое число: ")
list1 = list()
for i in range(1, n+1):
    list1.append(i)
print(list1)
found = 1000
x= float(input('введите натуральное число X: '))
for j in range(0, len(list1)):
    if abs(list1[j]- x)< abs(found-x):
        found=list1[j]


print(f'Ближайшее число к {x} в списке {list1} является {found}')