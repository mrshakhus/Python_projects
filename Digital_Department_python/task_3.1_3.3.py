'''
Дан словарь beatles_map, в котором ключ - это имя музыканта, а значение - это инструмент, на котором играет музыкант

beatles_map = {'Paul': 'Bass', 'John': 'Guitar', 'George': 'Guitar'}

Напишите код, который выполняет действия со словарём в следующем порядке:

Добавить в словарь музыканта Ringo, который играет на барабанах (“Drums”)

В отдельную переменную записать инструмент, на котором играет John и удалить этого музыканта из словаря

Вывести на экран значения словаря и новой переменной

Результат должен получиться такой:

{'Paul': 'Bass', 'George': 'Guitar', 'Ringo': 'Drums'}

'Guitar'
'''

beatles_map = {'Paul': 'Bass', 'John': 'Guitar', 'George': 'Guitar'}
beatles_map['Ringo'] = 'Drums'
John = beatles_map['John']
del beatles_map['John']
print(beatles_map)
print(John)



'''
Создайте два списка, в каждом из которых лежит 10 случайных букв алфавита (могут повторяться). Затем для каждого списка создайте словарь из пар «индекс — значение» и выведите оба словаря на экран.

Для генерации случайных букв можно использовать модуль random.

Пример: 

Первый список: ['й', 'р', 'с', 'г', 'а', 'а', 'т', 'ж', 'е', 'к']

Второй список: ['д', 'а', 'а', 'в', 'т', 'ж', 'р', 'б', 'й', 'р']

Первый словарь: {0: 'й', 1: 'р', 2: 'с', 3: 'г', 4: 'а', 5: 'а', 6: 'т', 7: 'ж', 8: 'е', 9: 'к'}

Второй словарь: {0: 'д', 1: 'а', 2: 'а', 3: 'в', 4: 'т', 5: 'ж', 6: 'р', 7: 'б', 8: 'й', 9: 'р'}
'''

import random

cyrillic = 'ёйцукенгшщзхъфывапролджэячсмитьбю'
list_1 = [0]*10
list_2 = [0]*10
dict_1 = {}
dict_2 = {}

for index in range(10):
    list_1[index] = random.choice(cyrillic)
    list_2[index] = random.choice(cyrillic)

for index in range(10):
    dict_1[index] = list_1[index]
    dict_2[index] = list_2[index]

print('\nПервый список:',list_1)
print('Второй список:',list_2)
print('Первый словарь:',dict_1)
print('Второй словарь:',dict_2,'\n')



'''
Мы снова работаем с базой данных магазина одежды, но в этот раз структуру немного изменили. Здесь информация делится на два словаря: первый отвечает за коды (id) товаров, второй — за списки количества разнообразных товаров, которые есть в наличии в магазине:

ids = {

    't-shirt': '10',

    'sneakers': '20',

    'trousers': '30',

    'cap': '40',

    'jacket': '50'

}

 

store = {

    '10': [

        {'quantity': 50, 'price': 800},

        {'quantity': 70, 'price': 950},

    ],

    '20': [

        {'quantity': 6, 'price': 5000},

        {'quantity': 12, 'price': 6000},

        {'quantity': 18, 'price': 4500},

    ],

    '30': [

        {'quantity': 22, 'price': 1200},

        {'quantity': 50, 'price': 1150},

    ],

    '40': [

        {'quantity': 5, 'price': 600},

    ],

    '50': [

        {'quantity': 11, 'price': 15000},

    ]

}

Каждая запись второго словаря отображает, сколько и по какой цене лежит товар  (quantity - количество, price - цена за одну штуку)

Напишите программу, которая рассчитывает, на какую сумму лежит каждого товара и выводит эту информацию на экран.

Результат работы программы.

t-shirt - 120 pieces, worth 106500 rub.

sneakers - 36 pieces, worth 183000 rub.

trousers - 72 pieces, worth 83900 rub.

cap - 5 pieces, worth 3000 rub.

jacket - 11 pieces, worth 165000 rub.
'''

ids = {
    't-shirt': '10',
    'sneakers': '20',
    'trousers': '30',
    'cap': '40',
    'jacket': '50'
}

store = {
    '10': [
        {'quantity': 50, 'price': 800},
        {'quantity': 70, 'price': 950},
    ],

    '20': [
        {'quantity': 6, 'price': 5000},
        {'quantity': 12, 'price': 6000},
        {'quantity': 18, 'price': 4500},
    ],

    '30': [
        {'quantity': 22, 'price': 1200},
        {'quantity': 50, 'price': 1150},
    ],

    '40': [
        {'quantity': 5, 'price': 600},
    ],

    '50': [
        {'quantity': 11, 'price': 15000},
    ]
}

def print_quantity_price(ids, store, clothing):
    id = str(ids[clothing])
    list_with_dict = store[id]
    total_quantity = 0
    price = 0
    list_lenght = len(list_with_dict)
    for index in range(list_lenght):
        current_dict = list_with_dict[index]
        price += current_dict['quantity'] * current_dict['price']
        total_quantity += current_dict['quantity']
        
    print(f'{clothing} - {total_quantity} pieces, worth {price} rub.\n')

for clothing in ids:
    print_quantity_price(ids, store, clothing)