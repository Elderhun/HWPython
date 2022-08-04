from writinglogg import ReadLogg

def Hello():
    print('\n---------------------\nCalcul\n---------------------\n')
    print('Запуск калькулинтра: 1')
    print('Просмотр логов: 4')
    ex = input()
    if ex == '1':
        return '1'
    if ex == '4':
        ReadLogg()
        return Hello()
    elif ex != '1' and ex != '4':
        print('Выбери 1 или 4')
        return Hello()

