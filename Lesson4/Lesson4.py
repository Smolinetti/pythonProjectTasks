import math

# Задача №1
# Вычислить число ПИ c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

print('-' * 60)
print("Задача №1 / Вычисление числа ПИ c заданной точностью *d*")
print('-' * 10)

bit = float(input("Введите точность для ПИ: "))
bit_list = str(bit)

final_bit = bit_list[::-1].find('.')

pi = float(math.pi)

print(round(pi, final_bit))
print('-' * 60)


# Задача №2
# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

print("Задача №2 / Составление списка простых множителей числа N")
print('-' * 10)
def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans

print(*Factor(int(input("Введите число: "))))
print('-' * 60)


# Задача №3
# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

print("Задача №3 / Выведение списка неповторяющихся элементов")
print('-' * 10)

x = list('1113384455229')

number = list(map(int, x))
print('Последовательность цифр: ', *number)

dict = {a: 0 for a in range(10)}

for k in dict:
    for i in number:
        if k == i:
            dict[k] += 1
            i += 1
    k += 1

final_list = []

for k in dict:
    if dict[k] == 1:
        final_list.append(k)

print('Список неповторяющихся элементов:', final_list)
print('-' * 60)


# Задача №4
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от -100 до 100) многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную
# итерацию степени
#
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

print("Задача №4 / Сформировать случайным образом список коэффициентов")
print('-' * 10)

import random


def createDict():
    equation = {}
    degree = int(input('Введите максимальную степень многочлена: '))
    for i in range(degree, -1, -1):
        equation[i] = random.randint(-10, 10)
    return equation


def createEquation(equation: dict):
    strEquation = ''
    first = True

    for k, v in equation.items():
        if first:
            first = False
            if v > 0:
                strEquation += f'{v}*x^{k}'
            elif v < 0:
                strEquation += f'- {abs(v)}*x^{k}'
        else:
            if v > 0:
                strEquation += f' + {v}*x^{k}'
            elif v < 0:
                strEquation += f' - {abs(v)}*x^{k}'

    return strEquation


def printEquation(equation: str):
    print(equation.replace('*x^1', 'x').replace('*x^0', '') + ' = 0')

print(createEquation(createDict()))
print('-' * 60)


# Задача №5
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
#
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0
#
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

print("Задача №5 / Формирование файла, содержащий сумму многочленов")
print('-' * 10)

from random import randint as rI

def createCoef():
    coef = {}
    degree = int(input("Введите максимальную степень: "))
    for i in range(degree, -1, -1):
        coef[i] = rI(-20,20)
    return coef


def createEquation(coefEquation: dict):
    equation = ''
    first = True

    for i in coefEquation.items():
        if first:
            first = False
            if i[1] < 0:
                equation += ' -' + str(abs(i[1])) + 'x^' + str(i[0])
            elif i[1] > 0:
                equation += str(abs(i[1])) + 'x^' + str(i[0])
        else:
            if i[1] < 0:
                equation += ' - ' + str(abs(i[1])) + 'x^' + str(i[0])
            elif i[1] > 0:
                equation += ' + ' + str(abs(i[1])) + 'x^' + str(i[0])

    return equation + ' = 0'

def parseEquation(equation: str):
    equation = equation.replace(' + ', ' +').replace(' - ', ' -')
    equation = equation.split()
    equation = equation[:-2]

    dictEquation = {}
    for i in range(len(equation)):
        equation[i] = equation[i].replace('+', '').split('x^')
        dictEquation[int(equation[i][1])] = int(equation[i][0])
    return dictEquation

equation1 = createEquation(createCoef())
equation2 = createEquation(createCoef())

parEq1 = parseEquation(equation1)
parEq2 = parseEquation(equation2)

resultEquation ={}
for i in range(max(len(parEq1), len(parEq2)), -1, -1):
    first = parEq1.get(i)
    second = parEq2.get(i)
    if first != None or second != None:
        resultEquation[i] = (first if first != None else 0) + (second if second != None else 0)

def printEquation(equation: str):
    print(equation.replace(" 1x", "x").replace("x^1", 'x').replace("x^0", ''))

printEquation(createEquation(parEq1))
printEquation(createEquation(parEq2))
printEquation(createEquation(resultEquation))

print('-' * 60)





