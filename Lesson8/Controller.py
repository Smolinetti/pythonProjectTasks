import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox as mb

from Classes import PhoneBook
import Model
from Interface import MainWindow, TopWindow


def refresh_table():
    MainWindow.main_table.delete(*MainWindow.main_table.get_children())
    for row in Model.my_phonebook.show_all():
        MainWindow.main_table.insert('', 0, values=row)

def change_contact(ID: int):
    contact = MainWindow.main_table.item(ID).get('values')
    TopWindow.createChangeWindow(contact)

def delete_contact(ID: int):
    contact = MainWindow.main_table.item(ID).get('values')
    if mb.askyesno('Удаление', f'Вы точно хотите удалить контакт {contact[1]}?'):
        Model.my_phonebook.remove(str(contact[0]))
        refresh_table()

def new_file():
    if mb.askyesno('Создать новую книгу?', 'Вы точно хотите создать новую книгу?\nВсе несохраненные данные будут утеряны'):
        Model.my_phonebook.clear()
        refresh_table()

def open_txt_file():
    types = (("all files", "*.*"),)
    full_file_name = askopenfilename(title='Открыть базу данных', filetypes=types)
    Model.my_phonebook.clear()
    with open(full_file_name, 'r', encoding='UTF-8') as file:
        for line in file.readlines():
            contact = line.replace('\n', '').replace("'", "").replace('"', '').split(', ')
            Model.my_phonebook.add(contact[1], contact[2], contact[3], contact[0])
    refresh_table()


def save_as_file():
    global main_table
    types = (("Текстовый файл", "*.txt"), ("SQLite3 DB file", "*.db"), ("all files", "*.*"))
    full_file_name = asksaveasfilename(title='Сохранить как...', filetypes=types, initialfile='phonebook.txt')
    with open(full_file_name, 'w', encoding='UTF-8') as file:
        data = ''
        for contact in Model.my_phonebook.show_all():
            data += str(contact)[1:-1] + '\n'
        file.write(data)