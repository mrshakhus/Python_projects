'''
Дано целое число N. Напишите программу, которая формирует список из нечётных чисел от 1 до N.

Пример 1:

Введите число: 1

Список из нечётных чисел от 1 до N: [1]

Пример 2:

Введите число: 14

Список из нечётных чисел от 1 до N: [1, 3, 5, 7, 9, 11, 13]
'''
def print_from_0_to_N():
    while True:
        N = input('Введите число: ')

        if not N:
            print('Введите число!')
            break
        elif N == 'exit':
            print('Программа завершена')
            break
        elif not N.isdigit():
            print('Вводить можно лишь цифры!')
            break
        
        N = int(N) + 1
        from_0_to_N = list(range(N))
        print(f'Список из нечетных чисел от 1 до N: {from_0_to_N[1:N:2]}')



'''
В программировании существует важный подраздел, который называется “Структуры данных и алгоритмы” (в технических университетах этому даже посвящается отдельный предмет). Этот подраздел тесно связан с оптимизацией времени выполнения кода, а также занимаемой им памяти. Одной из “классических” тем здесь является сортировка.

Дан список из N чисел. Напишите программу, которая сортирует элементы списка по возрастанию и выводит его на экран. Дополнительный список не использовать.

Решите задачу двумя способами: первый - с использованием встроенной функции для сортировки; второй - без использования этой функции. Во втором случае постарайтесь придумать и написать как можно более эффективный алгоритм сортировки.

Пример:

Изначальный список: [2, 6, -4, 11, 0, 15, -7]

Отсортированный список: [-7, -4, 0, 2, 6, 11, 15]
'''
from random import randint

def sort_array():
    while True:
        N = input('Введите число: ')

        if not N:
            print('Введите число!')
            break
        elif N == 'exit':
            print('Программа завершена')
            break
        elif not N.isdigit():
            print('Вводить можно лишь цифры!')
            break
        
        N = int(N)
        array_of_N = list(range(N))
        for index in range(N):
            array_of_N[index] = randint(-N, N)
        print('Изначальный список: ', array_of_N)

        #1-й способ
        array_of_N_sorted = sorted(array_of_N)
        print('1-й способ: отсортированный список: ', array_of_N_sorted)

        # 2-й способ
        sorted_array = list(range(N))
        smallest_number_in_array = array_of_N[0]
        greatest_number_in_array = array_of_N[0]
        index1 = 0

        while index1 < N:
            count_same_numbers = 0

            for number_in_array in array_of_N:
                if number_in_array == smallest_number_in_array:
                    continue
                elif number_in_array < smallest_number_in_array:
                    smallest_number_in_array = number_in_array
                elif number_in_array  > greatest_number_in_array:
                    greatest_number_in_array = number_in_array

            for index_to_ignore, number_in_array in enumerate(array_of_N ):
                if smallest_number_in_array == number_in_array:
                    count_same_numbers += 1
                    array_of_N[index_to_ignore] = N + 1

            for _ in range(count_same_numbers):
                sorted_array[index1] = smallest_number_in_array
                index1 += 1

            smallest_number_in_array = greatest_number_in_array
            
        
        print('2-й способ: отсортированный список: ', sorted_array)



'''
В базе данных магазина одежды хранится список названий товаров и сколько они стоят:

shop = [['футболка', 800], ['кроссовки', 5000], ['штаны', 500], ['шорты', 960], ['штаны', 450], ['кепка', 600], ['куртка', 9000], ['кроссовки', 2000], ['штаны', 870]]

Напишите программу, которая запрашивает у пользователя товар, считает их количество, а также общую стоимость.

Пример:

Название товара: штаны

Кол-во товаров - 3  

Общая стоимость - 1820
'''
import string
import re

def show_clothing_price():
    while True:
        shop = [['футболка', 800], ['кроссовки', 5000], ['штаны', 500], ['шорты', 960], ['штаны', 450], ['кепка', 600], ['куртка', 9000], ['кроссовки', 2000], ['штаны', 870]]

        clothing = input('\nВведите название одежды: ')

        all_characters = string.ascii_letters + string.digits + string.punctuation
        is_exception = False

        if clothing == '':
            print('Введите название одежды!')
            is_exception = True
        elif clothing == 'exit':
            break
        elif re.search(fr'[{all_characters}]', clothing):
            print('Можно вводить лишь кириллицу!')
            is_exception = True
        

        total_price = 0
        number_of_item = 0
        is_there = False

        for list in shop:
            if list[0] == clothing:
                total_price += list[1]
                number_of_item += 1
                is_there = True
        
        if not is_there and not is_exception:
            print('Нет в наличии')
        
        if is_there:
            print(f'Количество товаров - {number_of_item}\nОбщая стоимость - {total_price}\n')