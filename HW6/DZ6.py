# 1. Создайте программу для игры в "Крестики-нолики".
'''
def ListG(b):
    for i in range(0, len(b)):
        for j in range(0, len(b[i])):
            print(b[i][j], end=' ')
        print()


def Winner(b):
    if (
        b[0][0] == 'X' and b[0][1] == 'X' and b[0][2] == 'X' or b[0][0] == '0' and b[0][1] == '0' and b[0][2] == '0' or
        b[1][0] == 'X' and b[1][1] == 'X' and b[1][2] == 'X' or b[1][0] == '0' and b[1][1] == '0' and b[1][2] == '0' or
        b[2][0] == 'X' and b[2][1] == 'X' and b[2][2] == 'X' or b[2][0] == '0' and b[2][1] == '0' and b[2][2] == '0' or
        b[0][0] == 'X' and b[1][0] == 'X' and b[2][0] == 'X' or b[0][0] == '0' and b[1][0] == '0' and b[2][0] == '0' or
        b[0][1] == 'X' and b[1][1] == 'X' and b[2][1] == 'X' or b[0][1] == '0' and b[1][1] == '0' and b[2][1] == '0' or
        b[0][2] == 'X' and b[1][2] == 'X' and b[2][2] == 'X' or b[0][2] == '0' and b[1][2] == '0' and b[2][2] == '0' or
        b[0][0] == 'X' and b[1][1] == 'X' and b[2][2] == 'X' or b[0][0] == '0' and b[1][1] == '0' and b[2][2] == '0' or
        b[0][2] == 'X' and b[1][1] == 'X' and b[2][0] == 'X' or b[0][2] == '0' and b[1][1] == '0' and b[2][0] == '0'
        ):
        return True
    else:
        return False


a = 3
lst = ['*'] * 3
p = 0
i = 0
j = 0
step = ''
for i in range(a):
    lst[i] = ['*'] * a
ListG(lst)
for g in range(9):
    if g % 2 == 0:
        step = "X"
    else:
        step = "0"
    i = int(input()) - 1
    j = int(input()) - 1
    while int(i) < 0 or int(i) > 2 or int(j) < 0 or int(j) > 2 or lst[i][j] != '*':
        print('Error! Specify other coordinates')
        i = int(input()) - 1
        j = int(input()) - 1
    lst[i][j] = step
    ListG(lst)
    Winner(lst)
    if Winner(lst) == True:
        p = step
        break
if p == 'X':
    print("Wins X")
elif p == '0':
    print("Wins 0")
else:
    print("Friendship won")
'''

'''
# 2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,. приоритет операций стандартный.


import re
 
 
lambds_act_arithmetic = {'/': lambda x, y: str(int(x) / int(y)), '*': lambda x, y: str(int(x) * int(y)),
    '-': lambda x, y: str(int(x) - int(y)), '+': lambda x, y: str(int(x) + int(y)) }
    
def arithmetic(input_str):
 
    while (corresponds := re.search(r'\((.+?)\)', input_str)):
        input_str = input_str.replace(corresponds.group(0), arithmetic(corresponds.group(1)))
  
    for simvol, act in lambds_act_arithmetic.items():
        while (corresponds := re.search(r'(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)'.format(simvol), input_str)):
            input_str = input_str.replace(corresponds.group(0), act(*corresponds.groups()))

    return input_str
 
 
input_string = str(input())
print(arithmetic(input_string))
'''

# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#    Входные и выходные данные хранятся в отдельных текстовых файлах.


with open('C:/Users/Igor/Desktop/HomeWorkePythone/HW6/RLEone.txt', 'r') as f1:
    my_text = f1.read()

def EnRle(ss):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code

            
str_code = EnRle(my_text)
print(str_code)

f1.close()

with open('C:/Users/Igor/Desktop/HomeWorkePythone\HW6/RLEtwo.txt', 'r') as f2:
    my_text2 = f2.read()

def DeRle(ff:str):
    count = ''
    str_decode = ''
    for char in ff:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_decode = DeRle(my_text2)
print(str_decode)

f2.close()

with open('C:/Users/Igor/Desktop/HomeWorkePythone\HW6/RLEfin.txt', 'w') as res:
    
    res.write(str_code + '\n')
    res.write(str_decode)
res.close()   

    

    
    

   