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

for _ in range(10):
    print(duplicate_iteration())

#not an elegant solution, but nonetheless
