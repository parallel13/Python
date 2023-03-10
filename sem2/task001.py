

n= int(input('введите целое число n:'))
print(n)
f = 1
while n>0:
    f*=n
    n=n-1
print(f"факториал числа {n} равен {f}")
