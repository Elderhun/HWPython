# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

def FindNumber(spisok, number):
    for i in spisok:
        if i == str(number):
            return 'Yes, such a number exists'
    
    return 'No such number'


# 2.Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

def FindElement(spisok, element):
    it = 0
    for i in range(len(spisok)):
        if spisok[i] == element:
            it += 1
        if it == 2:
            return i
    return -1

spisok = ["qwe", "asd", "zxc", "qwe", "ertqwe", "123", "234", "567", "3256", "251"]
element = input('Write element: ')
number = input('Write Number: ')
result1 = FindElement(spisok, element)
result2 = FindNumber(spisok, number)
print(result1)
print(result2)
