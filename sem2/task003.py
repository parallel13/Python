#статистика по среднесуточной температуры

n= int(input('введите число дней:'))
count=0
maxDay=0
while n>0:
    t=int(input('введите температуру: '))
    if t>0:
        count+=1
    else:
        count=0
    if maxDay<count:
        maxDay=count
    n-=1

print(f"максимальное число дней с положительной температурой: {maxDay}")