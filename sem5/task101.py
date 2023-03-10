'''
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
'''

number = int(input('введите число: '))
power = int(input('введите степень числа: '))

def exponentiation(number, power):
    if(power==1):
        return (number)
    if(power !=1):
        return (number* exponentiation(number, power-1))
    

result= exponentiation(number, power)

print(f"число {number} в степени {power} равно: {result}")
