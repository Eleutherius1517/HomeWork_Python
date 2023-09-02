# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input("Введите количество элементов первого набора чисел: "))
m = int(input("Введите количество элементов второго набора чисел: "))
print("Введите сами элементы первого множества: ")
first_list = {int(input()) for i in range(n)}
print("Введите сами элементы второго множества: ")
second_list = {int(input()) for i in range(m)}

result_list = second_list.intersection(first_list) 
result = list(result_list)
result.sort()
print(*result)

input('\nНажмите Enter для выхода\n')