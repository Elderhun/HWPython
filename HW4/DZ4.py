# 1 Вычислить результат деления двух чисел c заданной точностью d?

n1 = float(input('Введите делимое: '))
n2 = float(input('Введите делитель: '))
d = int(input('Введите точность: '))

def Sep(lam, a, b):
    res = (lam(a, b))
    print(round(res, d))

Sep(lambda a, b: a / b, n1, n2)


# 1 Высчитать число пи с заданной точностью.

def NumberPi(a):
    i = 1
    x = 3
    g = 1
    p = 12**0.5
    s = ''
    while i < 10000:
        if i % 2:
            g = g - (1/(x*(3**i)))
        else:
            g = g + (1/(x*(3**i)))
        x += 2
        i += 1
    p *= g
    p = str(p)
    for i in range(a+2):
        s += str(p[i])
    return float(s)

d = int(input("Enter the number of characters after the comma: "))
print(NumberPi(d))


# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import math

def primefactors(n):
    while n % 2 == 0:
        print(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n))+1, 2):
        while (n % i == 0):
            print(i)
            n = n / i
        
    if n > 2:
        print(n)


n = int(input('Write number '))
primefactors(n)


# 2 Это упрощенный вариант)

from listmulti import dict

n = input('Write numper from 1 to 700 ')

print(dict[n])









