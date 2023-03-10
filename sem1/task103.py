#Задача 3: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
#Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.


"""
number = int(input('введите шестизначный номер билета:'))

number1 = int(number//100000)
number2 = number%100000//10000
number3 = number%100000%10000//1000
number4 = number%100000%10000%1000//100
number5 = number%100000%10000%1000%100//10
number6 = number%100000%10000%1000%100%10

print(f" {number1} {number2} {number3} {number4} {number5} {number6}")

if (number1+number2+number3)==(number4+number5+number6):
    print ('Счастливый')
else:
    print ('Обычный')
"""
number = (input('введите шестизначный номер билета:'))
b = int(number[0])+int(number[1])+int(number[2])
c = int(number[3])+int(number[4])+int(number[5])
print(f" {number[0]} {number[1]} {number[2]} {number[3]} {number[4]} {number[5]}")
if c == b:
  print('Счастливый')
else:
  print('Обычный')

