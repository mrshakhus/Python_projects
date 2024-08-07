'''
Создайте входной файл numbers.txt и запишите туда N целых чисел, каждое в отдельной строке. Напишите программу, которая выводит сумму этих чисел в выходной файл answer.txt.

Пример:

Содержимое файла numbers.txt:

1

2

3

4

10

Содержимое файла answer.txt

20
'''

numbers = []

with open('numbers.txt', 'r+') as numbers_file:
    numbers_file.write('1\n2\n3\n4\n10\n')
    numbers = numbers_file.readlines()
    numbers = [int(number) for number in numbers]
    numbers_sum = sum(numbers)

with open('answer.txt', 'r+') as answer_file:
    answer_file.write(str(numbers_sum))
    answer_file.read()
    

'''
При работе с файлами и файловой системой нередко можно столкнуться с такими понятиями как абсолютный путь и относительный путь. 

Представим, что у нас есть файл test.py. Этот файл лежит в какой-то папке (директории) на компьютере. Чтобы до файла добраться, нужно зайти в диск C, папка PycharmProjects, папка Stepik, папка module_5 и здесь будет лежать файл. Тогда абсолютный путь до файла будет выглядеть так:


Теперь представим всё то же самое, но как будто мы уже находимся в папке Stepik и ищем файл начиная с этой папки. Тогда относительный путь до файла будет выглядеть так:


Для работы с операционной системой в Питоне используется специальный модуль os. С его помощью можно писать универсальные скрипты, которые при переносе будут работать на любой системе.

Для работы с путями и их генерацией из модуля os используется специальный подмодуль path.

Напишите программу, которая выводит на экран относительный и абсолютный пути до файла numbers.txt, созданный в предыдущей задаче. Для этого используйте  os.path.join и  os.path.abspath. Документацию можно найти здесь. 
'''

import os.path

path = os.path.abspath('numbers.txt')
path_list = list(path.split('\\'))
print(path)

relative_path = list(path_list[i] for i in range(3,4))

path = os.path.join('Python_projects', *relative_path)
print(path)

# relative_path = []
# count = 0
# while True:
#     compensater = 2
#     count = compensater
#     relative_path[count - compensater] = path[count]
#     count += 1
#     if count + compensater == len(path):
#         break