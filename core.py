import shutil
import datetime
import os


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Папка уже существует')


def get_list(folders_only=False):
    res = os.listdir()
    if folders_only:
        res = [f for f in res if os.path.isdir(f)]
    print(res)


def delete_file(name):
    if os.path.isdir(name):
        # print('Удаляем папку')
        # os.rmdir(name) # удаляет только пустые папки
        shutil.rmtree(name)  # — это метод модуля shutil, который рекурсивно удаляет каталог и его содержимое.
    else:
        # print('Удаляем файл')
        try:
            os.remove(name)
        except FileNotFoundError:
            print(f'Файла/папки с именем {name} не существует')


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print(f'Папка с именем {new_name} уже существует')
    else:
        try:
            shutil.copy(name, new_name)
        except FileNotFoundError:
            print(f'Файла или папки с именем {name} не существует')
        except shutil.SameFileError:
            print(f'Файл с именем {new_name} уже существует')

def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def folder_change(name):
    if name != '..':
        try:
            os.chdir(name)
        except FileNotFoundError:
            print('Такой папки не существует')
    else:
        folder_full = os.getcwd()
        folder_minus, folder_name = os.path.split(folder_full)
        os.chdir(folder_minus)
    print(os.getcwd())



if __name__ == '__main__':
    create_file('test.dat')
    create_file('test.dat', 'Same text. 日本語')
    create_folder('new_f')
    get_list()
    get_list(True)
    delete_file('new_f')
    delete_file('test.dat')
    copy_file('new_f1', 'new_f3')
    copy_file('test.dat', 'test_copy.dat')
    save_info('Проверка')
