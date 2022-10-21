import random

# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter,
# map, zip, enumerate, list comprehension.


# list comprehension
list_random = [random.randint(1, 50) for _ in range(15)]
print(*list_random)


# <Задание 1>
# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
# [2, 3, 5, 9, 3] => на нечётных позициях элементы 3 и 9, ответ: 12

size_massive = int(input("Задайте размер массива: "))
list1 = [random.randint(1, 10) for _ in range(size_massive)]

print("Сформирован список из случайных чисел: ", *list1)
summ = 0
for i in range(0, size_massive, 2):
    summ += list1[i]

print("Сумма нечетных чисел списка равна", summ)


# map

oldlist = [random.randint(-10, 10) for _ in range(7)]

def sq(x):
    return x, x**2

b = map(sq, oldlist)
a = list(b)
print(a)


# filter, lambda

a = [random.randint(1, 10) for _ in range(10)]
print(a)

b = list(filter(lambda x: x%2, a))
print(b)

# zip

a = [1,2,3,4]
b = [5,6,7,8]

it = zip(a, b)
print(it)

print(list(it))
