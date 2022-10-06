# Задача №1
# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# НЕОБЯЗАТЕЛЬНО Попробовать решить не переводя числа в строку.
#
# Пример:
# 6782 -> 23
# 0,56 -> 11
import random


def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum


num = InputNumbers("Введите число: ")

print(f"Сумма цифр = {sumNums(num)}")



# Задача №2
# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.

# Пример:
# пусть N = 4, тогда (1, 1*2, 1*2*3, 1*2*3*4)

def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть integer ")
    return number


def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


num = InputNumbers("Введите число: ")

list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до {num}:  {list}")


# Задача №3
# Задайте список из n чисел последовательности (1+1/n)^n
# Выведитте на экран саму последовательность и сумму элементов этой последовательности
# (для проверки сумма для 4 элементов = 9,06 (примерно))

number = int(input("Введите число N:"))
f = 1
fact = []
for i in range(1, number+1):
    f *= i
    fact.append(f)
print(*fact)


# Задача №4
# Реализуйте алгоритм перемешивания списка,
# без использования встроеных методов
# (особенно SHUFFLE, без него)
# можно (нужно) использовать библиотеку Random

num = int(input("Введите размер массива: "))

myList = []

for i in range(num):
    myList.append(i)

print("Изначальный список: ", *myList)

newlist = []

for i in range(len(myList)):
    index = random.randint(0,len(myList))
    newlist.append(myList.pop(index-1))

print("Финальный   список: ", *newlist)


# НЕОБЯЗАТЕЛЬНО:
# Задайте список из N элементов,
# заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.


num = int(input("Введите размер массива: "))

myList = []

for i in range(num):
    myList.append(random.randint(-num, num))

print(myList)

with open("file.txt", "r") as data:
    coef1 = data.readline()[:-1]
    coef2 = data.readline()

print("Значение 1-ой строки: ", coef1)
print("Значение 2-ой строки: ", coef2, end="")

print("Произведение элементов на указанных позициях =", myList[int(coef1)] * myList[int(coef2)])
