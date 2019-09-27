
import random


def start():
    list_2048 = [['    ', '    ', '    ', '    '], ['    ', '    ', '    ', '    '], ['    ', '    ', '    ', '    '], ['    ', '    ', '    ', '    ']]
    i = 0
    while i < 2:
        x = random.randint(0,3)
        y = random.randint(0,3)
        if list_2048[y][x] == '    ':
            list_2048[y][x] = '%4d'%2
            i += 1
    for row in list_2048:
        for number in row:
            print(number,end='|')
        print()



start()




