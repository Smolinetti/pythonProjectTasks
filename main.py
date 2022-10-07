# Нахождение максимума
list = [5, 17, 15, 3, -1]
max = 0
for i in range(5):
    if list[i] > max:
        max = list[i]
print (max)


# Нахождение минимума
x = [16, 9, 0, -1, 12]
min = x[0]
for i in x:
    if i < min:
        min = i
print(min)

# Нахождение максимума
array = []
number = 3

for i in range(number):
    array.append(int(input(f"Введите число {i+1} из {number}: ")))

print("Вы ввели следующие цифры:", *array)

max = array[0]

for i in range(len(array)):
    if array[i] > max:
        max = array[i]

print(f"Из введённых {number} чисел, максимальное значение равно: {max}")


