

from RecordData import *
from ReadData import *



user_id= find_last_user_id()

while True:
    choise = int(input('Введите нужное действие: \n 1 - Добавить в справочник \
        \n 2 - Вывести всех \n 3 - Поиск по фамилии \n 4 - Выход \n'))
    match choise: 
        case 1: 
            Record_Data(user_id, input('Введите имя: '), input('Введите фамилию: '), input('Введите номер: '))
            user_id +=1

        case 2: 
            OutputAll()
            
        case 3:
            found=SearchData (input('Введите искомую фамилию: '))
            if found == True:           
                user_id=int(input('Введите id пользователя, которого хотите отредактировать. 0 если редактировать не требуется '))
                if user_id !=0:
                    Record_Data(user_id, input('Введите имя: '), input('Введите фамилию: '), input('Введите номер: '))
            
        case 4: break
