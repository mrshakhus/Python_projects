# from random import randint

# number = randint(0, 100)

# while True:
#     user_answer = input('Введите число: ')

#     if not user_answer or user_answer == 'exit':
#         break

#     if not user_answer.isdigit():
#         print('Печатать можно лишь цифры!')
#         continue

#     user_number = int(user_answer)

#     if user_answer == number:
#         print('Совершенно верно!')
#         break
#     elif user_answer < number:
#         print('Загаданное число больше')
#     elif user_answer > number:
#         print('Загаданное число меньше')

'''
Игра «Угадай число»

Напишите программу, которая генерирует случайное целое число в диапазоне от 1 до 10 и запрашивает у пользователя число до тех пор, пока он его не отгадает. Выводите сообщения в соответствии с примером.

Пример (сгенерировали число 6):

Введите число: 3

Число меньше, чем нужно. Попробуйте ещё раз!

Введите число: 10

Число больше, чем нужно. Попробуйте ещё раз!

Введите число: 8

Число больше, чем нужно. Попробуйте ещё раз!

Введите число: 7

Вы угадали! Число попыток: 4
'''
        
from random import randint

number = randint(0,10)

count = 0

while True:
    user_answer = input('Введите число: ')

    if not user_answer.isdigit():
        print('Вводить можно лишь цифры!')

    user_number = int(user_answer)

    count += 1
    if not user_answer or user_answer == 'exit':
        break

    if number > user_number:
        print('Число меньше, чем нужно. Попробуте еще раз!')
    elif number < user_number:
        print('Число больше, чем нужно. Попробуте еще раз!')
    else:
        print(f'Вы угадали! Число попыток: {count}')
        break


'''
Игра «Компьютер угадывает число»

В этот раз мы поменяем пользователя и компьютер из прошлой задачи местами. Теперь пользователь в уме загадывает число между 1 и 100 (включительно). Компьютер может спросить у пользователя: «Твое число больше, равно или меньше, чем число N?», где N — число, которое хочет проверить компьютер. Пользователь отвечает одним из соответствующих вариантов: “больше”, “равно” или “меньше”. 

Напишите программу, которая с помощью цепочки таких вопросов и ответов пользователя угадывает число. Ответы должны не зависеть от регистра, т.е. “больше”, “БОЛЬШЕ”, “БоЛьШе” - это один и тот же ответ.
'''

# from random import randint

print('Загадай число от 0 до 100\nЕсли загадал, то нажми Enter')
input()
bottom_range = 0
upper_range = 100
while True:
    number_from_computer = randint(bottom_range,upper_range)

    answer_from_user = input(f'Твое число это {number_from_computer}?\nТвой ответ: ')

    if not answer_from_user or answer_from_user == 'exit':
        break

    if answer_from_user.lower() == 'меньше':
        upper_range = number_from_computer - 1
    elif answer_from_user.lower() == 'больше':
        bottom_range = number_from_computer + 1
    elif answer_from_user.lower() == 'да':
        print('Ура! Я угадал!')
        break
    else:
        print('Нужно печатать либо "меньше" либо "больше" либо "равно"')

    


