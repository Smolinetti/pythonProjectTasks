# График f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

import numpy as np
import matplotlib.pyplot as plt

def func(x, a, b, c, d, e):
    return a*x**4*np.sin(np.cos(x)) + b*x**3 + c*x**2 + d*x + e

koef = [-12, -18, 5, 10, -30]
x_limit = [-10, 10]
x = np.arange(x_limit[0], x_limit[1], 0.1)
color = 'r'
x_change = []
func_direct = -1

def change_color():
    global color
    if color == 'r':
        color = 'b'
    else:
        color = 'r'
    return color

for i in range(len(x) - 1):
    if func_direct == -1:
        if func(x[i], *koef) < func(x[i+1], *koef):
            func_direct= 1
            x_change.append((x[i], func(x[i], *koef)))
    else:
        if func(x[i], *koef) > func(x[i+1], *koef):
            func_direct= -1
            x_change.append((x[i], func(x[i], *koef)))

x_cur = np.arange(x_limit[0], x_change[0][0], 0.1)
plt.plot(x_cur, func(x_cur, *koef), change_color())

for i in range(len(x_change) - 1):
    x_cur = np.arange(x_change[i][0], x_change[i+1][0], 0.1)
    plt.plot(x_cur, func(x_cur, *koef), change_color())

x_cur = np.arange(x_change[-1][0], x_limit[1], 0.1)
plt.plot(x_cur, func(x_cur, *koef), change_color())

plt.show()
