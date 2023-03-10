#напишите функцию, которая проверяет является число простым

num = int(input('введите число: '))
def Simple(num):
    for i in range(2,num//2):
        if num%i == 0:
            print('число не простое')
            break
    else:
        print('число простое')
Simple(num)