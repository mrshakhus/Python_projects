import sys

def print_stairs(number_of_stairs):
    number_of_stairs = str(number_of_stairs)

    if not number_of_stairs.isdigit():
        print('Вводить можно лишь цифры!')
        return
    elif not number_of_stairs:
        print('Введите число!')
        return
    
    number_of_stairs = int(number_of_stairs)

    hash_char = '#'
    space_char = ' ' 
    for hash_multiplier in range(1, number_of_stairs + 1, 1):
        space_multiplier = number_of_stairs
        if hash_multiplier == 0:
            continue
        space_multiplier -= hash_multiplier
        print(space_char*space_multiplier+hash_char*hash_multiplier)

number_of_stairs = sys.argv[1]

if __name__ == '__main__':
    print_stairs(number_of_stairs)