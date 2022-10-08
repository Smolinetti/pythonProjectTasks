# <Задание 1>
# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
# [2, 3, 5, 9, 3] => на нечётных позициях элементы 3 и 9, ответ: 12
import random

print("\nЗадача №1 / Сумма элементов списка")

list = []
size_massive = int(input("Задайте размер массива: "))
for i in range(size_massive):
    list.append(random.randint(1, 10))

print("Сформирован список из случайных чисел: ", *list)
summ = 0
for i in range(0, size_massive, 2):
    summ += list[i]

print("Сумма нечетных чисел списка равна", summ)


# <Задание 2>
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

print("\nЗадача №2 / Нахождение произведения пар чисел списка")

list = []
size_massive = int(input("Задайте размер массива: "))
for i in range(size_massive):
    list.append(random.randint(1, 10))
print("Сформирован список из случайных чисел: ", *list)

new_summ = 0
listlenght = 0

if len(list) % 2 == 0:
    listlenght = len(list)
else:
    listlenght = len(list) + 1

for i in range(listlenght//2):
    new_summ = list[i] * list[-i-1]
    print(f"{i+1} пара:", new_summ)
    i += 1


# <Задание 3>
# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов. Если число целое, то его дробная часть
# не считается за 0 и оно (число) в сравнении не участвует
#
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


print("\nЗадача №3 / Нахождение разницы между Max и Min")

list = [1.1, 1.2, 3.1, 5, 10.01]
print("Список из вещественных чисел:", list)

float_list = []

for i in range(0, len(list)):
    float_list.append(round(list[i]%1, 4))

maxx = 0

minn = float_list[0]

for i in range(0, len(float_list)):
    if float_list[i] > maxx:
        maxx = float_list[i]
        i += 1

    elif float_list[i] < minn and   float_list[i] != 0:
        minn = float_list[i]
        i += 1

diff = maxx - minn
print("Максимально значение дробной части равно:", maxx)
print("Минимальное значение дробной части равно:", minn)
print("Разница между максимальным и минимальным значениями:", diff)


# <Задание 4>
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
# 45 => 101101
# 3 => 11
# 2 => 10

print("\nЗадача №4 / Преобразовывание десятичного числа в двоичное")

number = int(input("Введите число в десятичном формате: "))

num = number
binary_number = []

while number > 0:
    binary_number.insert(0, str(number%2))
    number //= 2

print(f"Число {num} в двоичной системе: {''.join(binary_number)}")


# <Задание 5>
# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
#
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] (Негафибоначчи)

print("\nЗадача №5 / Составление списка чисел Фибоначчи")

number = int(input("Введите предел последовательности Фибоначчи:"))

def Fibonachi(number):
    list = [1, 0, 1]
    for i in range(2, number+1):
        list.append(list[i-1] + list[i])

    for i in range(0, -number+1, -1):
        list.insert(0, list[1] - list[0])

    return list

print(Fibonachi(number))
