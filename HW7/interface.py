def Interface(ex3):
    print('Выбор режима\n 1 - Пример с целыми числами.\n 2 - Пример с рациональными числами.')
    ex3 = input()
    if ex3 == '1':
        return '1'
    if ex3 == '2':
        return '2'
    if ex3 != '1' and ex3 != '2':
        print('Выбери 1 или 2')
        return Interface(ex3)
   



