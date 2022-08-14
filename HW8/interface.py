from writer import *

def main():
    print('Привет. Выбери что будем делать:\n 1. Записать новые данные.\n 2. Вывести данные\n 3. Удалить данные\n 4. Перезапись\n')
    action = int(input(''))
    
    if action == 1:
        write_base()
        de_numiration_line()
        numiration_line()
    if action == 2:
        print_data()
    if action == 3:
        print_data()
        delete_line(int(input('Введите строку которую хотите удалить: '))-1)
    if action == 4:
        print_data()
        overwriting_file()
        de_numiration_line()
        numiration_line()