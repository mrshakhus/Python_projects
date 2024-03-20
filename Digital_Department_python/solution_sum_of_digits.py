import sys

def sum_digits_in_number(digit_parametr):
    digit_string = str(digit_parametr)

    if not digit_string.isdigit():
        print('Вводить можно лишь цифры!')
        return
    
    if not digit_string:
        print('Введите число!')
        return

    sum_of_digits = 0

    for digit in digit_string:
        sum_of_digits += int(digit)
    print(sum_of_digits)

digit_string = sys.argv[1]
if __name__ == '__main__':
    sum_digits_in_number(digit_string)
