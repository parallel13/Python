#задача 21
#напишите программу для печати уникальных значений в словаре.
# input: [{"V": "s001"}, {"V": "s002"}, {"VI": "s001"}, {"VI": "s005"}, {"VII": "s005"},
# {"V": "s009"}, {"VIII": "s007"}]
#output: {'s005', 's002', 's007, 's001', 's009' }
#примечание: список словарей задан изначально.
# пользователь его не вводит.
listDict = [{"V": "s001"}, {"V": "s002"}, {"VI": "s001"}, {"VI": "s005"}, {"VII": "s005"},
{"V": "s009"}, {"VIII": "s007"}]
#list=[]
#for i in listDict:
#    for j in i.values():
#        if j not in list:
#            list.append(j)
#print(list)

result = list()
for dict in listDict:
    for k in dict:
        result.append(dict[k])
print(set(result))

