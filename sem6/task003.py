# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 10^5.
# Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной встроке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

def Sum(x):
    sum=0
    for i in range(1,x//2+1):
        if x%i==0:
            sum +=i
    return sum


k= int(input('введите длинну массива:'))

for n in range(k):
    j=Sum(n)
    if n<j and n<k and n==Sum(j):
        print(n,j)



# for i in range(k):
#     for j in range(i+1,k):
#         if sum(i)==j and i==sum(j):
#             print(i,j)

n=int(input())
list1=list()
for i in range(n):
    summa=0
    for j in range(1, i//2+1):
        if i%j==0:
            summa +=j
    list1.append(tuple([i,summa]))
for i in range(len(list1)):
    for j in range(i,len(list1)):
        if i !=j and list1[i][0]==list1[j][1] and list1[i][1]== list1[j][0]:
            print(*list1[i])
