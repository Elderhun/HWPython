from calc import *
from interface import *
from hello import *
from launcher import *
from writinglogg import *

def Act(action):
    if action == '1':
        print(result := Arithmetic(ar := input('Введите пример: ')))
        WritingLoggs(f'{ar} = {result}')
            
    if action == '2':
        d = ArithmeticFloat(ar2 := input('Введите пример: '))
        print(result := str(round(float(d),int(input('Введите кол-во елментов после точки: ')))))
        WritingLoggs(f'{ar2} = {result}')
          
Act(Interface(ChoiceAction(Launch(Hello()))))
