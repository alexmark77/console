# str = 'Aleksandr'
# print(str[5:2:-1])
# print(str.ljust(13))
# print(str.rjust(13, '*'))

# print("Первый аргумент: {0:+06d}, "
# "второй аргумент: {второй:>+9d}".format(-1, 3, второй=-25,))

dic = {'name': 'Alex', 'age': 44}
# a = dic.popitem()
# print(dic.get('name'))
# print(a)
print(dic.keys())

# Добавим коментарии
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, folder_change
from game import game
import sys


def info_help():
    print('Помощь:')
    print('list - список файлов и папок')
    print('listf - список только папок')
    print('crfi name text - создать файл name с текстом')
    print('crfo name - создать папку')
    print('delf name - удалить папку или файл')
    print('copy name newname - копировать')
    print('chdr name or .. - сменить текущую папку')
    print('game - поиграть')


save_info('Старт')

try:
    command = sys.argv[1]
except IndexError:
    info_help()
else:
    if command == 'list':
        get_list()
    elif command == 'listf':
        get_list(True)

    elif command == 'crfi':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Укажите имя файла')
        else:
            try:
                text = sys.argv[3]
            except IndexError:
                text = None
            create_file(name, text)

    elif command == 'crfo':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Укажите имя папки')
        else:
            create_folder(name)

    elif command == 'delf':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Укажите имя папки/файла для удаления')
        else:
            delete_file(name)

    elif command == 'copy':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Укажите имя папки/файла для копирования')
        else:
            try:
                new_name = sys.argv[3]
            except IndexError:
                print('Укажите новое имя папки/файла')
            else:
                copy_file(name, new_name)

    elif command == 'help':
        info_help()

    elif command == 'chdr':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Укажите имя папки или ..')
        else:
            folder_change(name)

    elif command == 'game':
        game()
    else:
        info_help()
save_info('Конец')
