'''
Дано целое число N. Напишите программу, которая формирует список из нечётных чисел от 1 до N.

Пример 1:

Введите число: 1

Список из нечётных чисел от 1 до N: [1]

Пример 2:

Введите число: 14

Список из нечётных чисел от 1 до N: [1, 3, 5, 7, 9, 11, 13]
'''
while False:
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

    # 1-й способ
    # array_of_N = sorted(array_of_N)
    # print('Отсортированный список: ', array_of_N)

    # 2-й способ
    sorted_array = list(range(N))
    smallest_number_in_array = array_of_N[0]
    greatest_number_in_array = array_of_N[0]
    index1 = 0

    while index1 != N:

        for number_in_array in array_of_N:
            if number_in_array == smallest_number_in_array:
                continue
            elif number_in_array < smallest_number_in_array:
                smallest_number_in_array = number_in_array
            else:
                greatest_number_in_array = number_in_array

        for index_to_delete, number_in_array in enumerate(array_of_N ):
            if smallest_number_in_array == number_in_array:
                array_of_N[index_to_delete] = greatest_number_in_array

        sorted_array[index1] = smallest_number_in_array
        smallest_number_in_array = 0
        index1 += 1
    
    print('Отсортированный список: ', sorted_array)

        






# def merge_sort(unordered_list):
#     if len(unordered_list <=1):
#         return
    
#     middle_index = len(unordered_list)//2
#     left_array = unordered_list[:middle_index]
#     right_array = unordered_list[middle_index:]

#     merge_sort(left_array)
#     merge_sort(right_array)

#     if 

    





