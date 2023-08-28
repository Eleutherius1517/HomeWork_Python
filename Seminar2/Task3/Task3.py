# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


number_n = int(input("Введите число N: "))
count_two = 1

while(count_two <= number_n):
    print(count_two, end=" ")
    count_two *= 2


input('\nНажмите Enter для выхода\n')

