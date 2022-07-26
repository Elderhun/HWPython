# 1. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов. Это не просто сумма всех коэффициентов.

def polynomial_to_dict(polynomial):
  terms = polynomial.replace(" ", "").replace("-", " -").replace("+", " +").split()
  pairs = {}

  free_term = ""
  for term in terms:
    if "x" not in term:
      free_term = term

  if (free_term!=""):
    terms.remove(free_term)
    pairs['0'] = free_term.replace('+', '')

  x1_term = ""
  for term in terms:
    if "^" not in term:
     x1_term = term  

  if (x1_term!=""):
    terms.remove(x1_term)
    x1_term = x1_term.replace('x', '').replace('*', '')
    if x1_term == '' or x1_term == '+':
      x1_term = '1'
    elif x1_term == '-':
      x1_term = '-1'
    pairs['1'] = x1_term.replace('+', '')

  for term in terms:
    splited_term = term.split("x^")
    if splited_term[0] == '' or splited_term[0] == '+':
      splited_term[0] = '1'
    elif splited_term[0] == '-':
      splited_term[0] = '-1'
    pairs[splited_term[1]] = splited_term[0].replace("*", "").replace('+', '')
    
  return pairs

with open('C:/Users/Igor/Desktop/HomeWorkePythone/HW5/file1.txt') as f1, open('C:/Users/Igor/Desktop/HomeWorkePythone/HW5/file2.txt') as f2:
  
  polynom1 = f1.read()
  polynom2 = f2.read()
  

  pairs1 = polynomial_to_dict(polynom1)
  print(pairs1)
  pairs2 = polynomial_to_dict(polynom2)
  print(pairs2)

  f1.close()
  f2.close()

def sum_of_polynomials(polynomial1 , polynomial2):

  pairs1 = polynomial_to_dict(polynomial1)
  pairs2 = polynomial_to_dict(polynomial2)

  for item in pairs2:
    if item in pairs1:
      pairs1[item] = str(int(pairs1[item]) + int(pairs2[item]))
    else:
      pairs1[item] = pairs2[item]
    
  return pairs1

summa = sum_of_polynomials(polynom1 , polynom2)

def dict_to_polynomial_string(pairs):
  result = ""
  for item in sorted(pairs)[::-1]:
    if result == "":
      result = result + pairs[item] + "*x^" + item
    elif int( pairs[item]) > 0 :
      result = result + "+" + pairs[item] + "*x^" + item
    elif int( pairs[item]) < 0:
      result = result + pairs[item] + "*x^" + item
  return (result.replace('*x^0', '').replace('^1', ''))
  
r = ((dict_to_polynomial_string(summa)))
print(r)

with open('C:/Users/Igor/Desktop/HomeWorkePythone/HW5/fileres.txt', 'w' ) as wrf:
  wrf.write(r)


# 2. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.


mass = [1, 5, 2, 3, 6, 1, 7, 4]

start = min(mass)
length  = 0
max_length  = 0
max_start = start

for i in range(start,max(mass)+1):
  if i in mass:
    length +=1
    if length>max_length:
      max_length = length
      max_start = start
  else:
    length = 0
    start = i+1


result = [max_start, max_start + max_length -1]
print(result)
