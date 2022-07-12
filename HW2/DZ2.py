# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
'''
def SumDigit(rNum):
    rNum = rNum.replace(',', '')
    rNum = rNum.replace('.', '')
    rNum = int(rNum)
    sum = 0
    while rNum > 0:
        sum += rNum % 10
        rNum //= 10
    return sum


number = SumDigit(input('Enter Your number: '))
print(f"Sum diggit number {number}")
'''


# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


def KitProdNum(n):

    i = 1
    prod = 1
    while i < n + 1:
        print(f"{prod} * {i}")
        prod *= i
        i += 1
    return prod

n = input('Write number: ')
try:
    n = int(n)
    result = KitProdNum(n)
    print(f"product of numbers {result}")
except:
    print('Write correct number')
