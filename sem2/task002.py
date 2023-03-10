#каким по счету числом Фибоначчи является число

n= int(input('введите число:'))

lastNum=0
currentNum=1
temp= None
count=0
while currentNum <=n:
    temp= lastNum
    lastNum=currentNum+lastNum
    currentNum=temp
    count+=1
    if n == currentNum:
        print(count)
        break
else:
    print("не является числом Фибоначчи")



