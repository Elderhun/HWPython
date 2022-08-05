from writer import *
from Loggs import ReadLogg

def Interface():
    print('Выберите действие:\n Запись в телефонную книгу - 1 \n Просмотр телефонной книги - 2 \n Просмотр логов - 3 ')
    action = input()

    if action == '1':
        name_l = input('Введите фамилию: ')
        name = input('Введите имя: ')
        phone = input('Введите номер: ')
        comm = input('Введите коментарий: ')
        write_for_phonebook = [f'Last mame: *{name_l}*', f'First name: *{name}*', f'Phone: *{phone}*', f'Comment: *{comm}*']
        WritePhoneBook(write_for_phonebook)

    if action == '2':
        ReadPhoneBook()

    if action == '3':
        ReadLogg()

    elif action != '1' and action != '2' and action != '3':
        print('Введите действие 1 или 2: ')
        