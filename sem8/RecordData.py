

#print(f'id: {user_id} имя: {firstname} Фамилия: {secondname} Номер телефона: {number}')
def Record_Data(user_id, first_name, second_name, phone_number):
    with open('data.txt', 'r+', encoding='utf-8') as file:
        position = 0
        while (line := file.readline()):
            file_user_id, _, _, _ = line.split(':')
            if int(file_user_id) == int(user_id):
                end_of_file = file.read()
                file.seek(position)
                file.write(f'{user_id} : {first_name} : {second_name} : {phone_number}\n' + end_of_file)
                file.truncate()
                print('откорректировано')
                return
            else:
                position = file.tell()
        if position != 0:
            file.write('\n')
        file.writelines(
            [f'{user_id} : {first_name} : {second_name} : {phone_number}']
        )
        print('Добавлено')
    

