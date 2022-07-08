# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

dayNumber = int(input('Write number day '))

def Day(day):
    
    if day > 7 or day < 1:
        print("Wrong day of the week")

    else:

        if day > 5:
            print("Today is a day off")

        else:
            print("Working day")

Day(dayNumber)


# 2. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input('Write x coordinat '))
y = int(input('Write y coordinat '))

def NumberQwart(x, y):
    
    if x != 0 and y != 0:
        
        if x > 0 and y > 0:
            return 1
        if x < 0 and y > 0:
            return 2
        if x < 0 and y < 0:
            return 3
        if x > 0 and y < 0:
            return 4
    
    else:
        print('Write correct x and y')

qwart = NumberQwart(x, y)
print(qwart)