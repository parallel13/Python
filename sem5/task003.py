
num = int(input('введите количество элементов: '))

def Reverse(num):
    if num == 0:
        return
    n = int(input('введите число: '))
    Reverse(num-1)
    print(n)

Reverse(num)