#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n= int(input('введите целое число n:'))

sqd=1
while sqd<=n:
    print(f'{sqd}')
    sqd=sqd*2
