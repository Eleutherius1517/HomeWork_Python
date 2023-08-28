# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
import random

amount_coin = int(input("Введите количество монеток: "))
coins_list = [random.randint(0,1) for item in range(amount_coin)] # написал для проверки эту строчку
print(*coins_list)

i_zero = 0
i_one = 0
for i in coins_list:
    if i == 0:
        i_zero += 1
    if i == 1:
        i_one +=1
if i_zero < i_one:
    print(i_zero)
else:
    print(i_one)
    
input('Нажмите Enter для выхода\n')