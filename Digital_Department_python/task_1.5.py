# Даны две точки: A и B c координатами (1, 2) и (5, 6). Напишите программу, которая по заданным двум точкам находит расстояние между ними в декартовых координатах и выводит ответ на экран. Затем вставьте полученный ответ в окно ответа внизу. Расстояние рассчитывается по теореме Пифагора: гипотенуза равна корню квадратному из суммы квадратов катетов. Примечание: корень квадратный можно обозначить как степень 0.5. Пример ответа: 5.0

#Task 1
x_first = 1
x_second = 5
y_first = 2
y_second = 6

distance_between = ((x_second - x_first)**2 + (y_second - y_first)**2)**0.5
print(distance_between)


#Task 2
expression = (-10+2*(7**2+3/2)-3+4**3**2)/(3+4*10)
print(expression)


#Task 3
four_digit_number = int(input("Enter a four digit number: "))
first_digit = int(four_digit_number/1000)
print(first_digit)

first_digit = first_digit*10
second_digit = int(four_digit_number/100) - first_digit
print(second_digit)

first_digit = first_digit*10
second_digit = second_digit*10
third_digit = int(four_digit_number/10) - second_digit - first_digit
print(third_digit)

first_digit = first_digit*10
second_digit = second_digit*10
third_digit = third_digit*10
fourth_digit = four_digit_number - third_digit - second_digit - first_digit
print(fourth_digit)


#Task 4
#Наша фирма дала нам задачу модифицировать календарь, который используется в приложении этой фирмы. Пользователь берёт любой год, а нам нужно определить, високосный этот год или нет и вывести сообщение об этом на экран. Реализуйте такую программу. Напоминание: для ввода используйте команду int(input()). Год будет високосным, когда он одновременно кратен 4 и НЕ кратен 100 ЛИБО если он просто кратен 400.

year_by_user = int(input("Enter a year to check: "))

is_leap = (year_by_user % 4 == 0 and year_by_user % 100 != 0 or year_by_user % 400 == 0)
print(is_leap)


#Task 5
#Напишите программу, которая получает на вход строку и выполняет с ней следующие действия:
#считает количество символов в ней
#приводит всю строку к нижнему регистру (подсмотрите метод)
#выводит оба ответа на экран

string_from_user = input("Enter anything: ")
print(len(string_from_user))
print(string_from_user.lower())


#Task 6
#Пользователь вводит текст. Напишите программу, 
# которая выводит каждый символ текста в отдельной строке и 10 раз. Используйте цикл for, показанный в видео.


string_from_user = input("Enter anything: ")
count = 1 
for letter in string_from_user:
    for count in range(10):
        print(letter, end='')
    print('\n')  
    


#Task 7
'''
alphabet = 'абвгдеёжзи'

Напишите программу, которая выводит на экран 10 вот таких результатов:

1. Копия строки

2. Элементы строки в обратном порядке

3. Каждый второй элемент строки (включая самый первый)

4. Каждый второй элемент строки после первого

5. Все элементы до пятого (не включая)

6. Все элементы в диапазоне индексов от 2 до 6 (не включая 6)

7. Последние три элемента строки

8. Все элементы в диапазоне индексов от 3 до 4 в обратном порядке.

Для получения и вывода результатов используйте только команду print и срезы.
'''

alphabet = 'абвгдеёжзи'

print(alphabet) #1

alphabet_reversed = alphabet [::-1]
print(alphabet_reversed) #2

alphabet_odd_indexed = alphabet[::2]
print(alphabet_odd_indexed) #3

alphabet_even_indexed = alphabet[1::2]
print(alphabet_even_indexed) #4

alphabet_first_four = alphabet[:4:] 
print(alphabet_first_four) #5

alphabet_from_2_to_5 = alphabet[1:5:] 
print(alphabet_from_2_to_5) #6

alphabet_last_three = alphabet[-1:-4:-1] 
print(alphabet_last_three) #7

alphabet_from_3_to_4_reversed = alphabet[-3:-5:-1] 
print(alphabet_from_3_to_4_reversed) #8