#Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве),
#которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива.
#Затем число M - количество элементов во втором массиве. Затем элементы второго массива.

# from random import randint # выводим библиотеку
# array=[]
# n= int(input('введите длинну массива:'))
# for i in range(0,n):
#     array.append(randint(0,10))
# print(array)
# array2=[]
# for i in range(0,n):
#     array2.append(randint(0,10))
# print(array2)
# for i in array:
#     for j in array2:
#         if i==j:
#             break
#     else:
#           print(i, end =' ')

# for i in array:
#     if i not in array2:
#         print(i, end =' ')

def input_array(size):
    array=[]
    for i in range(size):
        array.append(int(input()))
    return array

n= int(input('введите длинну первого массива:'))
array1 = input_array(n)
m= int(input('введите длинну второго массива:'))
array2 = input_array(m)


print(array1)
print(array2)
print([i for i in array1 if i not in array2])


