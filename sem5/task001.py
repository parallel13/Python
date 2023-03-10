def Fib(num):
    if num<=1:
        return num
    else:
        return Fib(num-1)+ Fib(num-2)

n= int(input('введите длину списка: '))
print(Fib(n))