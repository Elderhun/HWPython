from templates import *

def write_base():
        name = name_cre()
        surname = surname_cre()
        phone = phone_cre()
        adress = adress_cre()   
        new_write_line().write(f"{name};{surname};{phone};{adress}")
        new_write_line().write('\n')
        new_write_line().close()
           
def print_data():
    
    for line in read_file_line(): 
        print(line)

def delete_line(stringa):
    de_numiration_line()
    data = list(read_file_line().readlines())
    # data = data[:stringa] + data[stringa + 1:]
    data.remove(data[stringa])
    overwrite_write_line().write(''.join(data))
    numiration_line()
    print_data()

def overwriting_file():
    number = int(input('Введите запись, которую хотите изменить'))-1
    name = name_cre()
    surname = surname_cre()
    phone = phone_cre()
    adress = adress_cre()
    data = list(read_file_line().readlines())
    data = data[:number] + [f'{name};{surname};{phone};{adress}\n'] + data[number + 1:] 
    overwrite_write_line().write(''.join(data))
    print_data()
