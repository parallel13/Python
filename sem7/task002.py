#программа принимает на вход вещественное число и показывавет его сумму сыфр

n= input('введите вещественное число:')
res = list(filter(lambda x: x !=',' and x!='.', n))
res=sum(list(map(lambda x: int(x),res)))
print(res)


#print(sum(map(int, filter(lambda el: el.isdigit(), input('введите вещественное число:')))))