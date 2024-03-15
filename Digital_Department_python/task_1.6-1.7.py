'''
Модифицируйте решение задачи про високосный год: теперь при проверке на високосность выводите соответствующие сообщения.

Напомним: Год будет високосным, когда он одновременно кратен 4 и НЕ кратен 100 ЛИБО если он просто кратен 400.

Пример 1 работы программы:

Введите год: 800

Год високосный

Пример 2 работы программы:

Введите год: 804

Год високосный

Пример 3 работы программы:

Введите год: 500

Год не високосный
'''
year_by_user = int(input('Введите год: '))

if (year_by_user % 4 == 0 and year_by_user % 100 != 0 or year_by_user % 400 == 0):
    print('Год високосный')
else:
    print('Год не високосный')

'''
У компании, на которую мы работаем, есть свой сайт, а также свой сервер, на котором лежат различные документы и отчёты. У каждого такого документа есть свой url-адрес, например:

https://site/subsite/documentlibrary/Sales.rdl

Нашей компании важно, чтобы файл лежал именно в папке с названием documentlibrary.

На вход в программу подаётся url-адрес в виде строки. Напишите программу, которая проверяет вхождение подстроки “documentlibrary”, а также проверяет, что url начинается на “https” (для написания такой проверки посмотрите методы строк). Выведите соответствующие сообщения.

Пример 1:

url: http://site/subsite/documentlibrary/Sales.rdl

Ошибка: адрес не начинается с https.

Пример 2:

url: https://site/subsite/document/Sales.rdl

Ошибка: подстрока documentlibrary не обнаружена.

Пример 3:

url: https://site/subsite/documentlibrary/Sales.rdl

Адрес указан верно.
'''

url = input('url: ')

if 'documentlibrary' in url and 'https' in url:
    print('Адрес указан верно')
elif 'documentlibrary' not in url:
    print('Подстрока documentlibrary не обнаружена')
elif 'https' not in url:
    print('Адрес не начинатеся с https')


'''
Пользователь вводит число N. Выведите пятую степень каждого нечётного числа в диапазоне от единицы до N включительно. Для этого используйте шаг внутри функции range. Выводите результат в соответствии с примером.

Пример:

Введите число: 5

1 ** 5 = 1

3 ** 5 = 243

5 ** 5 = 3125
'''

N = int(input('Введите число: '))

for number in range(N+1):
    if number % 2 != 0:
        print(f'{number} ** 5 = {pow(number, 5)}')


'''
Каждый день нас просят где-либо ввести пароль. Даже компьютер (если мы, конечно, этот пароль ставили). Если после ввода пароль оказался неверным, нам сообщают об этом и снова просят ввести пароль. И так до тех пор, пока мы не введём правильный пароль.

Напишите программу, которая запрашивает у пользователя пароль до тех пор, пока он не введёт верный (верным будет считать самый надёжный пароль в мире - qwerty123).

Пример:

Введите пароль: 123

Неверный пароль! Попробуйте ещё раз.

Введите пароль: qwerty

Неверный пароль! Попробуйте ещё раз.

Введите пароль: qwerty123

Пароль верный!
'''

password_by_user = input('Введите пароль: ')
actual_password = 'qwerty123'

if password_by_user == actual_password:
    print('Пароль верный!')
else:
    print('Неверный пароль! Попобуйте еще раз.')
