#Через сколько итераций функция random.randint(1,10) выдаст повтор

from random import randint

def duplicate_iteration():
    random_numbers = []

    for _ in range(10):
        random_numbers.append(randint(1,10))

    iteration_number = 0
    index = 0
    counter = 0
    is_break = False
    while index != 10:
        number_from_list = random_numbers[index]
        for index_to_check in range(10):
            if index == index_to_check:
                continue
            elif number_from_list == random_numbers[index_to_check]:
                iteration_number = index_to_check - index 
                is_break = True
                break
        if is_break:
            break
        if counter == 100:
            break
        counter += 1

    return iteration_number

#not an elegant solution, but nonetheless
    

def modified_duplicate_randint():
    random_numbers = []
    while True:
        random_number = randint(1,10)

        if random_number not in random_numbers:
            random_numbers.append(random_number)
        else:
            print(len(random_numbers) + 1)
            break

# for _ in range(100):
#     modified_duplicate_randint()

"""
Напишите программу, которая считает количество специальных символов в символьной строке. В рамках задачи к специальным символам относятся символы из набора "@!#№$%&". Набор должен храниться в виде множества.

Пример:

Введите строку: $Ан@лиз# д@нных%на% №Python!

Количество специальных символов: 8
"""

def count_special_symbols(user_answer):
    special_symbols = set("@!#№$%&")
    count = 0
    user_answer

    for symbol in user_answer:
        if symbol in special_symbols:
            count += 1

    return count

#user_answer = input('Введите строку: ')
#print('Количество специальных символов:', count_special_symbols(user_answer))

"""
Реализуйте функцию, которая в качестве аргумента получает строку и возвращает список слов этой строки. В качестве примера можно взять вот такой текст:

text = '''Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 

Aenean commodo ligula eget dolor. Aenean massa. 

Cum sociis natoque penatibus et'''

Подсказка: вспомните про методы строк, в том числе про разделение и соединение (join).
"""

def get_words(text):
    text_splited = list(text.split())
    text_splited = [word.strip('.,') for word in text_splited]
    return text_splited

text = '''Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 

Aenean commodo ligula eget dolor. Aenean massa. 

Cum sociis natoque penatibus et'''

for word in get_words(text):
    print(word)

'''
Реализуйте функцию, которая может принимать на вход 3 аргумента: имя пользователя (имя пользователя - строка, не содержащая цифр), возраст и приветствие. Имя - обязательный позиционный аргумент, остальные - со значениями по умолчанию. При корректном вводе функция выводит на экран имя, возраст и приветствие.

В основной программе вызовите функцию минимум 3 раза: только с именем; с именем и с указанием возраста; с именем и с указанием приветствия.

По умолчанию возраст - None, приветствие - “Добро пожаловать”.

Пример 1:

Введите имя: Вася2
Неверный ввод. Введите имя без цифр
Введите имя: Вася
Имя: Вася
Возраст: None
Добро пожаловать, Вася!


Пример 2:

Введите имя: Петя
Имя: Петя
Возраст: 25
Добро пожаловать, Петя!


Пример 3:

Введите имя: Катя
Имя: Катя
Возраст: None
Привет, Катя!
'''

def welcome(name, age = None, welcoming = 'Добро пожаловать'):
    if name.isdigit():
        print('Неверный ввод. Введите имя без цифр')
        return False
    
    message = f'Имя: {name}\nВозраст: {age}\n{welcoming}, {name}!'
    print(message)
    return True

name = input('Введите имя: ')
if not welcome(name):
    name = input('Введите имя: ')

name = input('Введите имя: ')
age = 25
welcome(name, age)

name = input('Введите имя: ')
welcoming = 'Привет'
welcome(name=name, welcoming=welcoming)
