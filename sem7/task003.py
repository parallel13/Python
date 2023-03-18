# [12,' sadf, 543] ---> [sadf], [12, 543]
print('введите строку')
list1 = [x for x in input().split()]

res1= list(filter(lambda x: x.isdigit(), list1))
res2= list(filter(lambda x: x.isdigit()== False, list1))
print(res1,res2)