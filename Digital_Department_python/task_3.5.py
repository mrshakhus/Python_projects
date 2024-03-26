#Через сколько итераций функция random.randint(1,10) выдаст повтор

from random import randint

random_numbers = []

for _ in range(10):
    random_numbers.append(randint(1,10))

iteration_number = 0
index = 0
while index != 10:
    number_from_list = random_numbers[index]
    for index_to_check in range(10):
        if index == index_to_check:
            continue
        elif number_from_list == random_numbers[index_to_check]:
            iteration_number = index_to_check - index 

