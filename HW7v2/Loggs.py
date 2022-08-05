import datetime
data = datetime.date.today()


def WriteLogg():
    f = open('HW7v2/loggs.txt', 'a', encoding='utf-8')
    f.write('Произведена запсь в книгу.' + '\n')
    f.write(str(data) + '\n')
    f.close()


def ReadLogg():
    with open("HW7v2\loggs.txt", "r", encoding='utf-8') as file:
        line = file.readlines()
    for i in line:
        i = line.index(i)
        print(line[i])    
