import re

def name_cre():
    name = input('Name: ')
    return name

def surname_cre():
    surname = input('Surname: ')
    return surname

def phone_cre():
    phone = input('Phone: ')
    return phone

def adress_cre():
    adress = input('Adress: ')
    return adress

def read_file_line():
    read_file = open('HW8/b1.csv', 'r', encoding='utf-8')
    return read_file

def overwrite_write_line():
    delete_file = open('HW8/b1.csv', 'w', encoding='utf-8')
    return delete_file

def new_write_line():
    write_file = open('HW8/b1.csv', 'a', encoding='utf-8')
    return write_file


def numiration_line():
    data = []
    for idx, line in enumerate(read_file_line()):
        data += re.sub(r"^",f"{idx + 1};", line)     
    overwrite_write_line().write(''.join(data))


def de_numiration_line():
    data = []
    for line in read_file_line():
        data += re.sub(r'^\d\D', '', line)
    overwrite_write_line().write(''.join(data))


