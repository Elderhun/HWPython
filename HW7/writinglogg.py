def WritingLoggs(elel):
    with open('HW7\loggs.txt', 'a') as log:
        log.write(elel + '\n')

def ReadLogg():
    with open("HW7\loggs.txt", "r") as file:
        line = file.readlines()
    for i in line:
        i = line.index(i)
        print(line[i])    
