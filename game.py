import random


def game():
    print('Загадайте число от 1 до 100 и запомните его')
    number_min = 1
    number_max = 100
    input('Начнем?')

    while True:
        number = random.randint(number_min, number_max)
        #    print(number_min, number, number_max)
        print(f'Загаданое цисло >, < или = {number} ?')
        user_answer = input('Выбирите > < = :')
        if user_answer == '=':
            print(f'Победа! Вы загадали {number}')
            break
        elif user_answer == '>':
            #        print(f'загаданное число больше {number}')
            number_min = number + 1
        elif user_answer == '<':
            #        print(f'загаданное число меньше {number}')
            number_max = number - 1
        else:
            print('Не понял.')
