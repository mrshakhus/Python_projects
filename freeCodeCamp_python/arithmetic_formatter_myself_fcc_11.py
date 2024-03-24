def arithmetic_arranger(problems, show_answers=False):
    result1 = ''
    result2 = ''
    result3 = ''

    #1 error
    if len(problems) > 5:
        return 'Error: Too many problems.'

    #Extracting numbers from string
    for problems_index in range(len(problems)):
        number1 = ''
        number2 = ''
        operation = ''
        expression = []
        index = 0

        #Placing string in a list
        for char in problems[problems_index]:
            expression.append(char)

        is_number1 = True

        #Placing each number into its own string
        while index != len(expression):
            if expression[index] != ' ' and is_number1:
                number1 += expression[index]
            elif not is_number1:
                number2 += expression[index]
            else:
                index += 1
                operation = expression[index]

                #2 error
                if operation != '+' and operation != '-':
                    return 'Error: operator must be "+" or "-".'
                    
                index += 1
                is_number1 = False

            index += 1
        
        dash_count = max(len(number1), len(number2)) + 2
        mult_num_1 = dash_count - len(number1)
        mult_num_2 = dash_count - len(number2) - 2

        if len(number1) > 4 or len(number2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        elif number1.isdigit() and number2.isdigit:
            number1 = int(number1)
            number2 = int(number2)
        else:
            return 'Error: Number must only contain digits.'
        
        
        if True:
            result1 += f'{mult_num_1*' '}{number1}    '
            result2 += f'{operation} {mult_num_2*' '}{number2}    '
            result3 += f'{'-'*dash_count}    '


    return result1 +'\n'+ result2 +'\n'+ result3

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')