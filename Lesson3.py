# <Задание 1>
# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
# [2, 3, 5, 9, 3] => на нечётных позициях элементы 3 и 9, ответ: 12
import random

list = []
size_massive = int(input("Задайте размер массива: "))
for i in range(size_massive):
    list.append(random.randint(1, 10))

print("Сформирован список из случайных чисел: ", *list)
summ = 0
for i in range(size_massive):
    if list[i] % 2 != 0:
        summ += list[i]

print("Сумма нечетных чисел списка равна", summ)


