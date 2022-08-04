import re

def Arithmetic(input_str):
 
    lambds_act_arithmetic = {
    '/': lambda x, y: str(int(x) / int(y)), 
    '*': lambda x, y: str(int(x) * int(y)),
    '-': lambda x, y: str(int(x) - int(y)), 
    '+': lambda x, y: str(int(x) + int(y)),
    '^': lambda x, y: str(int(x) ** int(y))
    }
    while (corresponds := re.search(r'\((.+?)\)', input_str)):
        input_str = input_str.replace(corresponds.group(0), Arithmetic(corresponds.group(1)))
  
    for simvol, act in lambds_act_arithmetic.items():
        while (corresponds := re.search(r'(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)'.format(simvol), input_str)):
            input_str = input_str.replace(corresponds.group(0), act(*corresponds.groups()))

    return input_str



def ArithmeticFloat(input_str):

    lambds_act_arithmetic = {
    '/': lambda x, y: str(float(x) / float(y)), 
    '*': lambda x, y: str(float(x) * float(y)),
    '-': lambda x, y: str(float(x) - float(y)), 
    '+': lambda x, y: str(float(x) + float(y)),
    '^': lambda x, y: str(float(x) ** float(y))
    }
    while (corresponds := re.search(r'\((.+?)\)', input_str)):
        input_str = input_str.replace(corresponds.group(0), ArithmeticFloat(corresponds.group(1)))
  
    for simvol, act in lambds_act_arithmetic.items():
        while (corresponds := re.search(r'(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)'.format(simvol), input_str)):
            input_str = input_str.replace(corresponds.group(0), act(*corresponds.groups()))

    return input_str

