from random import randint

number = randint(0, 100)

while True:
    user_answer = input('Введите число: ')

    if not user_answer or user_answer == 'exit':
        break

    if not user_answer.isdigit():
        print('Печатать можно лишь цифры!')
        continue

    user_number = int(user_answer)

    if user_answer == number:
        print('Совершенно верно!')
        break
    elif user_answer < number:
        print('Загаданное число больше')
    elif user_answer > number:
        print('Загаданное число меньше')
        




