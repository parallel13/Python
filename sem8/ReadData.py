def OutputAll():

    with open('data.txt', 'r', encoding='utf-8') as file:
        for line in file:
            user_id, first_name, second_name, phone_number = line.split(':')
            print(f'{user_id} : {first_name} : {second_name} : {phone_number}')
       
#print(f'{user_id} : {firstname} : {secondname} : {number}')
def SearchData(data):
    data = data.lower()
    with open('data.txt', 'r', encoding='utf-8') as file:
        flag = False
        for line in file:
            user_id, first_name, second_name, phone_number = line.split(':')
            if data in second_name.lower():
                print(f'{user_id} : {first_name} : {second_name} : {phone_number}')
                flag = True
                
        if flag == False:
            print('\n не найдено \n')
        return flag 


def find_last_user_id():
    try:
        with open('data.txt', 'r', encoding= 'utf-8') as file:
            user_id=0
            for line in file:
                file_user_id, _, _, _ = line.split(':')
                user_id=file_user_id
    except IOError:
        with open('data.txt', 'w', encoding= 'utf-8') as file:
            user_id=0
    return int(user_id)+1