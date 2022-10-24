import tkinter as tk

def InputData(string: str):
    number=int(input(f'Введите {string} число: '))
    return number

def OutputResult(a, b, oper, number):
    print(f'Результат операции {a} {oper} {b} = {number}')

def InputOperator():
    oper = input(f'Введите оператор: ')
    return oper

def division_by_zero():
    print('Деление на ноль!!')

def print_window(result):
    win = tk.Tk()
    win.geometry('300x300+600+600')
    my_label = tk.Label(win, text=result)
    my_label.pack()
    win.mainloop()