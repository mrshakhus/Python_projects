import operator
ops = {'+': operator.add, '-': operator.sub}

def arithmetic_arranger(problems, show_answers=False):

    #Checking whether number of problems exceed 5
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_number = ''
    second_number = ''
    operation = ''
    result = ''
    top_line = ''
    middle_line = ''
    dash_line = ''
    bottom_line = ''
    final_result = ''

    for expression in problems:
        first_number = expression.split()[0]
        operation = expression.split()[1]
        second_number = expression.split()[2]

        if operation != '+' and operation != '-':
            return "Error: Operator must be '+' or '-'."
        elif not(first_number.isdigit() and second_number.isdigit()):
            return 'Error: Numbers must only contain digits.'
        elif len(first_number) > 4 or len(second_number) > 4:
                return 'Error: Numbers cannot be more than four digits.'

        dash_count = max(len(first_number),len(second_number)) + 2 

        if show_answers:
            result = ops[operation](int(first_number), int(second_number))
            bottom_line += str(result).rjust(dash_count) + 4*' '

        top_line += first_number.rjust(dash_count) + 4*' '
        second_number = operation + second_number.rjust(dash_count - 1)
        middle_line += second_number + 4*' '
        dash_line += '-' * dash_count + 4*' '
        new_line = '\n'

    top_line = top_line[0:len(top_line)-4]
    middle_line = middle_line[0:len(middle_line)-4]
    dash_line = dash_line[0:len(dash_line)-4]

    final_result = top_line + new_line + middle_line + new_line + dash_line

    if not show_answers:
        return final_result
    
    bottom_line = bottom_line[0:len(bottom_line)-4]

    #returns if show_answers == True
    final_result += new_line + bottom_line
    return final_result

if __name__ == '__main__':
    print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
    print(f'\n{arithmetic_arranger(["1 + 2", "1 - 9380"])}')
    print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')
    print(f'\n{arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])}')
    print(f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}')
    print(f'\n{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])}')
    print(f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}')
    print(f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}')
    print(f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
    print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')