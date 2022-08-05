from Loggs import WriteLogg

def WritePhoneBook(write_for_phonebook):
    f = open('HW7v2/phonebook.txt', 'a', encoding='utf-8')
    for i in write_for_phonebook:
        f.write(i + '\n')
    WriteLogg()
    f.close()

def ReadPhoneBook():
    with open("HW7v2\phonebook.txt", "r", encoding='utf-8') as file:
        line = file.readlines()
    for i in line:
        i = line.index(i)
        print(line[i]) 
