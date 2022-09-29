# Задача №1
# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input('Введите день недели от 1 до 7: '))

if 6 <= day <= 7:
    print('"Это выходной день !"')
elif 0 < day < 6:
    print('Это будний день !')
else:
    print('Это вне диапазона дня недели !')


# Задача №2
# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def inputNumbers(x):
    xyz = ["X", "Y", "Z"]
    a = []
    for i in range(x):
        a.append(input(f"Введите значение {xyz[i]}: "))
    return a


def checkPredicate(x):
    left = not (x[0] or x[1] or x[2])
    right = not x[0] and not x[1] and not x[2]
    result = left == right
    return result


statement = inputNumbers(3)

if checkPredicate(statement) == True:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")




