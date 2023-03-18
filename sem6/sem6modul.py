def FillArray():
    from random import randint
    return [ randint(0,100) for i in range (int(input('введите длину массива: ')))]